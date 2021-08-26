def moveTower(height, fromPole, toPole, withPole):
    if height >= 1:
        moveTower(height-1, fromPole, withPole, toPole)  # 二层移到中间
        moveDisk(fromPole, toPole)  # 三层移到目标
        moveTower(height-1, withPole, toPole, fromPole)  # 二层移到三层上


def moveDisk(fp, tp):
    print('move disk from {} to {}'.format(fp, tp))


moveTower(3, 'A', "B", "C")
