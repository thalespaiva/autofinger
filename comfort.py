#!/usr/bin/python

# First try with a simple genetic algorithm

# Based on my hand: (in centimeters)
DISTANCES_NATURAL = {
    (1, 2): 15, (1, 3): 19, (1, 4): 20.5,
    (1, 5): 21.5, (2, 3): 9, (2, 4): 13,
    (2, 5): 16.5, (3, 4): 8.5, (3, 5): 13,
    (4, 5): 8,
}

DISTANCES_CROSSING = {
    (1, 2): 12, (1, 3): 9, (1, 4): 6,
    (1, 5): 0.01, (2, 3): 0.01, (2, 4): 0.005,
    (2, 5): 0.0001, (3, 4): 0.01, (3, 5): 0.0001,
    (4, 5): 0.0001,
}

CLOSED_DISTANCE = {
    (1, 2): 4.5, (1, 3): 7, (1, 4): 8.6,
    (1, 5): 10.5, (2, 3): 3.3, (2, 4): 6,
    (2, 5): 8.7, (3, 4): 3.3, (3, 5): 6.1,
    (4, 5): 3.3,
}

AV_KEY_WIDTH = 1.95  # centimeters


def calculate_jump_comfort(finger_org, finger_dst, jump_in_half_tones):
    jump = jump_in_half_tones * AV_KEY_WIDTH
    key = tuple(sorted((finger_org, finger_dst)))

    if finger_org == finger_dst:
        return abs(jump)

    elif jump >= 0:
        if finger_org < finger_dst:
            dist = DISTANCES_NATURAL[key]
        else:
            dist = DISTANCES_CROSSING[key]

        diff = jump - dist
        factor = jump / dist

        if diff > 0:
            return diff
        else:
            return factor * CLOSED_DISTANCE[key]

    else:
        if finger_org > finger_dst:
            dist = DISTANCES_NATURAL[key]
        else:
            dist = DISTANCES_CROSSING[key]

        diff = jump + dist
        factor = jump / dist

        if diff < 0:
            return abs(diff)
        else:
            return factor * CLOSED_DISTANCE[key]


def calculate_comforts(fingers_org, fingers_dst, jumps):
    from itertools import product

    keys = product(fingers_org, fingers_dst, jumps)
    xs = []
    ys = []
    zs = []
    cs = []

    for key in keys:
        o, d, j = key
        xs.append(o)
        ys.append(d)
        zs.append(j)
        cs.append(calculate_jump_comfort(o, d, j))

    return (xs, ys, zs, cs)


def plot_comfort(fingers_org=range(1, 6, 1), fingers_dst=range(1, 6, 1),
                 jumps=range(-12, 13, 1)):

    import seaborn
    from mpl_toolkits.mplot3d import Axes3D
    from pylab import plt

    xs, ys, zs, cs = calculate_comforts(
        fingers_org, fingers_dst, jumps)

    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.scatter(xs, ys, zs, c=cs)
    ax.set_zlabel("Interval (half steps)", fontsize=15)
    ax.set_zlim(jumps[0], jumps[-1])
    # ax.set_zticks(jumps)

    plt.xticks(fingers_org)
    plt.xlim(fingers_org[0], fingers_org[-1])
    plt.xlabel("From finger", fontsize=15)

    plt.yticks(fingers_dst)
    plt.ylim(fingers_dst[0], fingers_dst[-1])
    plt.ylabel("To finger", fontsize=15)

    plt.title("Difficulty of finger passages", fontsize=25)

    plt.savefig('./figures/image.png', figsize=(16, 12), dpi=300)
    plt.show()


if __name__ == '__main__':
    plot_comfort()
