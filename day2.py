import sys
import os

class Solution(object):
    def __init__(self):
        self.args = [arg for arg in sys.argv[1:]]

    def solution(self, args):

        # uses first command line arg if exists else inputfile.txt
        file = args[0] if args and os.path.isfile(args[0]) else 'inputday2.txt'
        f = open(file, 'r')
        lines = f.read().splitlines()
        f.close()

        lines = [x.split(' ') for x in lines]
        lines = [(x[0], int(x[1])) for x in lines]
        xVal = 0
        yVal = 0

        xVal = sum([x[1] for x in lines if x[0]=='forward'])

        yVal = sum(x[1] for x in lines if x[0]=='down')-sum([x[1] for x in lines if x[0]=='up'])

        return xVal*yVal


def main():
    s = Solution()
    print(s.solution(s.args))

if __name__ == '__main__':
    main()