import sys
import os
import re

class Solution(object):
    def __init__(self):
        self.args = [arg for arg in sys.argv[1:]]

    def solution(self, args):

        # uses first command line arg if exists else inputfile.txt
        file = args[0] if args and os.path.isfile(args[0]) else 'inputday17.txt'
        f = open(file, 'r')
        lines = f.readline()
        f.close()

        lines = re.split(r", | |=|\.\.", lines)

        targetArea = [[int(lines[3]), int(lines[4])], [int(lines[6]), int(lines[7])]]

        pos = [0, 0]

        def take_step(pos, xMove, yMove):
            pos[0]+=xMove
            pos[1]+=yMove
            if xMove>0:
                xMove-=1
            elif xMove<0:
                xMove+=1
            yMove-=1
            return pos, xMove, yMove

        def pos_inside_target(pos, targetArea=targetArea):
            if pos[0]>=targetArea[0][0] and pos[0]<=targetArea[0][1] and pos[1]>=targetArea[1][0] and pos[1]<=targetArea[1][1]:
                return True
            return False

        valid_points = []

        for a in range(targetArea[0][1]+1):
            for b in range(targetArea[1][0], -1*targetArea[1][0]):
                pos = [0, 0]
                maxY = b
                pos, x, y = take_step(pos, a, b)
                while not pos_inside_target(pos) and pos[1] >= targetArea[1][0] and pos[0]<=targetArea[0][1]:
                    pos, x, y = take_step(pos, x, y)
                    if pos[1]> maxY:
                        maxY = pos[1]
                if pos_inside_target(pos):
                    valid_points.append([a, b])
                print("===============")

        return len(valid_points)

def main():
    s = Solution()
    print(s.solution(s.args))

if __name__ == '__main__':
    main()