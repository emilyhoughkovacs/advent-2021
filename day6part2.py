import sys
import os

class Solution(object):
    def __init__(self):
        self.args = [arg for arg in sys.argv[1:]]

    def solution(self, args):

        # uses first command line arg if exists else inputfile.txt
        file = args[0] if args and os.path.isfile(args[0]) else 'inputday6.txt'
        f = open(file, 'r')
        line = f.read().split(',')
        f.close()

        line = [int(x) for x in line]
        # testfishes
        # fishes = [0, 1, 1, 2, 1, 0, 0, 0, 0]

        numFish = dict()
        for x in line:
            if x in numFish:
                numFish[x]+=1
            else:
                numFish[x]=1

        fishes = [0 for x in range(9)]

        for x in numFish:
            fishes[x] = numFish[x]

        print(fishes)


        def take_day(fishList=fishes):
            numZeroes=fishList[0]
            for x in range(8):
                fishList[x] = fishList[x+1]
            fishList[6]+=numZeroes
            fishList[8]= numZeroes
            return fishList

        print("day 0:", sum(fishes), fishes)
        for x in range(256):
            fishes = take_day()
            print("day", x+1, ":", sum(fishes), fishes)


def main():
    s = Solution()
    print(s.solution(s.args))

if __name__ == '__main__':
    main()