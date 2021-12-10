import sys
import os
import re

class Solution(object):
    def __init__(self):
        self.args = [arg for arg in sys.argv[1:]]

    def solution(self, args):

        # uses first command line arg if exists else inputfile.txt
        file = args[0] if args and os.path.isfile(args[0]) else 'inputday10.txt'
        f = open(file, 'r')
        lines = f.read().splitlines()
        f.close()

        newLines = list()
        for line in lines:
            while re.search(r"\[\]|\(\)|\{\}|<>", line):
                line = re.sub(r"\[\]|\(\)|\{\}|<>", "", line)
            newLines.append(line)

        incomplete = list()
        for line in newLines:
            if not re.search(r"\]|\}|\)|>", line):
                incomplete.append(line)

        incomplete = [x[::-1] for x in incomplete]

        scoring = {
            '(' : 1,
            '[' : 2,
            '{' : 3,
            '<' : 4
        }

        scores = list()
        for row in incomplete:
            score = 0
            for char in row:
                score = score*5
                score+=scoring[char]
            scores.append(score)

        scores = sorted(scores)
        middle = int(len(scores)/2)
        return scores[middle]

def main():
    s = Solution()
    print(s.solution(s.args))

if __name__ == '__main__':
    main()