import sys
import os

class Solution(object):
    def __init__(self):
        self.args = [arg for arg in sys.argv[1:]]

    def solution(self, args):

        # uses first command line arg if exists else inputfile.txt
        file = args[0] if args and os.path.isfile(args[0]) else 'inputday3.txt'
        f = open(file, 'r')
        lines = f.read().splitlines()
        f.close()

        lines = [x for x in lines]
        gamma = ''
        epsilon = ''

        length = len(lines)

        for i in range(len(lines[0])):
            theSum=0
            theSum= sum([int(x[i]) for x in lines])
            if theSum > length/2:
                gamma = gamma+'1'
            else:
                gamma = gamma+'0'

        for x in gamma:
            if x=='1':
                epsilon+='0'
            else:
                epsilon+='1'

        return int(gamma, 2)*int(epsilon, 2)


def main():
    s = Solution()
    print(s.solution(s.args))

if __name__ == '__main__':
    main()