import sys
import os

class Solution(object):
    def __init__(self):
        self.args = [arg for arg in sys.argv[1:]]

    def solution(self, args):

        # uses first command line arg if exists else inputfile.txt
        file = args[0] if args and os.path.isfile(args[0]) else 'inputday1.txt'
        f = open(file, 'r')
        lines = f.read().splitlines()
        f.close()

        lines = [int(x) for x in lines]

        increased = 0
        for x in range(1, len(lines)):
            if lines[x] > lines[x-1]:
                increased+=1

        return increased

def main():
    s = Solution()
    print(s.solution(s.args))

if __name__ == '__main__':
    main()