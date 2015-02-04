#!/usr/bin/python

# First try with a simple genetic algorithm


class ComfortCalculator(object):

    # Based on my hand:
    DISTANCES_NATURAL = {
        (1, 2): 15, (1, 3): 19, (1, 4): 20.5,
        (1, 5): 21.5, (2, 3): 9, (2, 4): 13,
        (2, 5): 16.5, (3, 4): 8.5, (3, 5): 13,
        (4, 5): 8,
    }

    DISTANCES_CROSSING = {
        (1, 2): 12, (1, 3): 9, (1, 4): 6,
        (1, 5): 3, (2, 3): 0.6, (2, 4): 0.3,
        (2, 5): 0, (3, 4): 0.2, (3, 5): 0,
        (4, 5): 0,
    }

    CLOSED_DISTANCE = {
        (1, 2): 4.5, (1, 3): 7, (1, 4): 8.6,
        (1, 5): 10.5, (2, 3): 3.3, (2, 4): 6,
        (2, 5): 8.7, (3, 4): 3.3, (3, 5): 6.1,
        (4, 5): 3.3,
    }

    AV_KEY_WIDTH = 1.95  # centimeters

    def calculate_jump_comfort(finger_org, finger_dst, jump_in_half_tones):
        jump = jump_in_half_tones * ComfortCalculator.AV_KEY_WIDTH
        key = tuple(sorted((finger_org, finger_dst)))

        if finger_org == finger_dst:
            return abs(jump)

        elif jump >= 0:
            if finger_org < finger_dst:
                dist = ComfortCalculator.DISTANCES_NATURAL[key]
            else:
                dist = ComfortCalculator.DISTANCES_CROSSING[key]

            diff = jump - dist
            factor = jump/dist

            if diff > 0:
                return diff
            else:
                return factor*ComfortCalculator.CLOSED_DISTANCE[key]

        else:
            if finger_org > finger_dst:
                dist = ComfortCalculator.DISTANCES_NATURAL[key]
            else:
                dist = ComfortCalculator.DISTANCES_CROSSING[key]

            diff = jump + dist
            factor = jump/dist

            if diff < 0:
                return abs(diff)
            else:
                return factor*ComfortCalculator.CLOSED_DISTANCE[key]
