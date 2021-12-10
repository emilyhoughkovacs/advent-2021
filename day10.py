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

        corrupted = list()
        for line in newLines:
            if re.search(r"\]|\}|\)|>", line):
                corrupted.append(line)

        badChars = list()
        for line in corrupted:
            for i in range(len(line)):
                if re.match(r"\]|\}|\)|>", line[i]):
                    badChars.append(line[i])
                    break

        scoring = {
            ')' : 3,
            ']' : 57,
            '}' : 1197,
            '>' : 25137
        }

        return sum(scoring[n] for n in badChars)

def main():
    s = Solution()
    print(s.solution(s.args))

if __name__ == '__main__':
    main()