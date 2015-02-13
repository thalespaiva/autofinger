#!/usr/bin/python

import random
from numpy import sqrt
from random import choice, randint

import comfort


class Autofingerer(object):

    base_weights_2sd_lo = (0.4, 0.25, 0.15, 0.12, 0.08)
    base_weights_1sd_lo = (0.2, 0.4, 0.2, 0.1, 0.1)
    base_weights_med = (0.1, 0.2, 0.4, 0.2, 0.1)
    base_weights_1sd_hi = (0.1, 0.1, 0.2, 0.4, 0.2)
    base_weights_2sd_hi = (0.08, 0.12, 0.15, 0.25, 0.4)

    all_fingers = [1, 2, 3, 4, 5]

    def __init__(self, score):
        super(Autofingerer, self).__init__()
        self.score = score
        self.units = score.get_units()

    def weighted_choice(self, choices, weights):
        total = sum([weights[i - 1] for i in choices])
        adj_weights = [weights[i - 1] / total for i in choices]

        r = random.random()
        m = adj_weights[0]
        for i in range(len(choices) - 1):
            if r <= m:
                return choices[i]
            m += adj_weights[i + 1]
        return choices[-1]

    def fitness(self, fingering):
        fitness = 0
        finger_org = fingering[0]

        for i in range(1, len(fingering)):
            finger_dst = fingering[i]
            jump = self.units[i].notes[0].pitch - \
                self.units[i - 1].notes[0].pitch
            if finger_org is None or finger_dst is None:
                pass
            else:
                fitness += comfort.calculate_jump_comfort(
                    finger_org, finger_dst, jump)
            finger_org = finger_dst
        return fitness

    def gen_random_finger(self, available_fingers, note, bar):
        diff = abs(note.pitch - bar.center)
        sd = sqrt(bar.var)

        if diff > 2 * sd:
            if note.pitch < bar.center:
                return self.weighted_choice(available_fingers,
                                            self.base_weights_2sd_lo)
            else:
                return self.weighted_choice(available_fingers,
                                            self.base_weights_2sd_hi)
        if diff > 1 * sd:
            if note.pitch < bar.center:
                return self.weighted_choice(available_fingers,
                                            self.base_weights_1sd_lo)
            else:
                return self.weighted_choice(available_fingers,
                                            self.base_weights_1sd_hi)
        else:
            return self.weighted_choice(available_fingers,
                                        self.base_weights_med)

    def gen_random_fingering(self, unit, bar):

        if len(unit.notes) == 1:
            if (unit.notes[0].not_pause()):
                return (self.gen_random_finger(self.all_fingers,
                                               unit.notes[0], bar))
            else:
                return (None)

        fingering = []

        n = len(unit.notes)
        available_fingers = self.all_fingers.copy() + [None]  # extremely ugly
        f = 0
        for i in range(len(unit.notes)):
            f = self.gen_random_finger(
                available_fingers[f:-n + i], unit.notes[i], bar)
            fingering.append(f)
        return tuple(fingering)

    def generate_base_population(self, size=100):
        population = []

        for i in range(size):
            subject = []
            for line in self.score.lines:
                for bar in line:
                    for unit in bar.units:
                        f = self.gen_random_fingering(
                            unit, bar)
                        subject.append(f)
            population.append((self.fitness(subject), subject))
        return population

    def selection(self, population):
        population.sort(key=lambda sbj: sbj[0])
        return population[0:int(10)]

    def cross_parents(self, this_parent, that_parent):
        i = randint(1, len(this_parent))
        this_child = this_parent[:i] + that_parent[i:]
        that_child = that_parent[:i] + this_parent[i:]

        return [this_child, that_child]

    def generate_descendents(self, parents):
        descendents = []

        for i in range(len(parents)):
            for j in range(i + 1, len(parents)):
                c1, c2 = self.cross_parents(parents[i][1], parents[j][1])
                descendents.append((self.fitness(c1), c1))
                descendents.append((self.fitness(c2), c2))
        return descendents

    def mutate_subject(self, subject):
        mut_genes = random.sample(range(len(subject)), int(len(subject)*0.05))
        for i in mut_genes:
            subject[i] = choice(self.all_fingers)
        return subject

    def mutate_population(self, population):
        for sbj in random.sample(population, 20):
            new = self.mutate_subject(sbj[1].copy())
            population.append((self.fitness(new), new))

    def find_best_fit_fingering(self, population_size=1000, n_iterations=1000):
        population = self.generate_base_population(population_size)
        best = population[0]
        for i in range(n_iterations):
            parents = self.selection(population)
            descendents = self.generate_descendents(parents)
            population = population[0:population_size]
            population += descendents
            if best[0] > parents[0][0]:
                best = parents[0]
            self.mutate_population(population)
        return [best, self.selection(population)]

if __name__ == "__main__":
    from score import Score
    s = Score.parse('./tests/test_files/jsbach_inventio1.xml')
    a = Autofingerer(s)
    #p = a.generate_base_population()
