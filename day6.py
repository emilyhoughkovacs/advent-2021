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

        def take_day(line=line):
            line = [fish-1 for fish in line]
            numNew = line.count(-1)
            line = [6 if fish==-1 else fish for fish in line]
            line = line+[8 for x in range(numNew)]
            return line

        print("day 0:", len(line), line)
        for x in range(80):
            line = take_day(line)
            print("day", x+1, ":", len(line))


def main():
    s = Solution()
    print(s.solution(s.args))

if __name__ == '__main__':
    main()