import sys
import os

class Solution(object):
    def __init__(self):
        self.args = [arg for arg in sys.argv[1:]]

    def solution(self, args):

        # uses first command line arg if exists else inputfile.txt
        file = args[0] if args and os.path.isfile(args[0]) else 'inputday5.txt'
        f = open(file, 'r')
        lines = f.read().splitlines()
        f.close()

        lines = [line.split(' -> ') for line in lines]
        lines = [[x.split(',') for x in line] for line in lines]
        lines = [[[int(y) for y in x] for x in line] for line in lines]

        spots = list()

        for point1, point2 in lines:
            if point1[0]==point2[0]:
                spots+= [(point1[0], y) for y in range(point1[1], point2[1]+1)]
                if point1[1]>point2[1]:
                    spots+=[(point1[0], y) for y in range(point2[1], point1[1]+1)]
            if point1[1]==point2[1]:
                spots+= [(x, point1[1]) for x in range(point1[0], point2[0]+1)]
                if point1[0]>point2[0]:
                    spots+=[(x, point1[1]) for x in range(point2[0], point1[0]+1)]

        numSpots = dict()
        for x in spots:
            if x in numSpots:
                numSpots[x]+=1
            else:
                numSpots[x]=1

        numTwoOrMore = 0
        for x in numSpots.values():
            if x>= 2:
                numTwoOrMore+=1

        return numTwoOrMore

def main():
    s = Solution()
    print(s.solution(s.args))

if __name__ == '__main__':
    main()