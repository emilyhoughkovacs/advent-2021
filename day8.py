import sys
import os

class Solution(object):
    def __init__(self):
        self.args = [arg for arg in sys.argv[1:]]

    def solution(self, args):

        # uses first command line arg if exists else inputfile.txt
        file = args[0] if args and os.path.isfile(args[0]) else 'inputday8.txt'
        f = open(file, 'r')
        lines = f.read().splitlines()
        f.close()

        lines = [line.split('|')[1].split() for line in lines]
        numSize = [[len(word) for word in line] for line in lines]

        numOccurrences = 0
        for row in numSize:
            for num in row:
                if num in (2, 4, 3, 7):
                    numOccurrences+=1
        return numOccurrences

def main():
    s = Solution()
    print(s.solution(s.args))

if __name__ == '__main__':
    main()