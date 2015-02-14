#!/usr/bin/python3


class State:

    def __init__(self, key, finger):
        self.key = key
        self.finger = finger

    def __str__(self):
        return "[f = %-2s k = %-3s]" % (self.finger, self.key)

    def possible_org_states():
        for key in KEYS:
            for finger in FINGERS:
                yield State(key, finger)

    def possible_dst_states():
        for rel_octave in REL_OCTAVES:
            for key in KEYS:
                for finger in FINGERS:
                    yield State(key + rel_octave, finger)


KEYS = ['c', 'c#', 'd', 'd#', 'e', 'f', 'f#', 'g', 'g#', 'a', 'a#', 'b']
FINGERS = ['1', '2', '3', '4', '5']
REL_OCTAVES = ['+0', '+1', '+2', '-1', '-2']


def gen_transition_file(output_filename):

    fout = open(output_filename, 'a')
    for org_state in State.possible_org_states():
        for rel_octave in REL_OCTAVES:
            for key in KEYS:
                total = 0
                probs = []
                for finger in FINGERS:
                    dst_state = State(key + rel_octave, finger)
                    p = input(str(org_state) + ' -> ' + str(dst_state) + ': ')
                    total += float(p)
                    probs.append(p)
                probs = [float(p) / total for p in probs]

                for i in range(len(FINGERS)):
                    finger = FINGERS[i]
                    dst_state = State(key + rel_octave, finger)

                    line = '(\'%s\', \'%s\') -> (\'%s\', \'%s\') : \'%f\'' % (
                        org_state.key, org_state.finger, dst_state.key,
                        dst_state.finger, probs[i])

                    fout.write(line + '\n')
    fout.close()

if __name__ == "__main__":
    import sys

    gen_transition_file(sys.argv[1])
