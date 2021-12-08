import sys
import os

class Solution(object):
    def __init__(self):
        self.args = [arg for arg in sys.argv[1:]]

    def solution(self, args):

        # uses first command line arg if exists else inputfile.txt
        file = args[0] if args and os.path.isfile(args[0]) else 'inputday7.txt'
        f = open(file, 'r')
        line = f.read().split(',')
        f.close()

        line = [int(x) for x in line]

        line = sorted(line)


        def distance(line, pos):
            totalDistance = 0
            for x in line:
                distance=abs(x-pos)
                totalDistance+= sum([x for x in range(1, distance+1)])
            return totalDistance

        minDistance = distance(line, line[0])

        for p in range(line[0]+1, line[-1]+1):
            dist = distance(line, p)
            if dist < minDistance:
                minDistance=dist

        return minDistance        

def main():
    s = Solution()
    print(s.solution(s.args))

if __name__ == '__main__':
    main()