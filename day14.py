import sys
import os
from collections import Counter

class Solution(object):
    def __init__(self):
        self.args = [arg for arg in sys.argv[1:]]

    def solution(self, args):

        # uses first command line arg if exists else inputfile.txt
        file = args[0] if args and os.path.isfile(args[0]) else 'inputday14.txt'
        f = open(file, 'r')
        lines = f.read().splitlines()
        f.close()

        polymer_template = lines[0]

        global pair_insertion
        pair_insertion = {line.split(" -> ")[0]:line.split(" -> ")[1] for line in lines[2:]}

        def polymerize(curString=polymer_template):
            newString = ''
            for i in range(len(curString)-1):
                segment = curString[i:i+2]
                if segment in pair_insertion.keys():
                    segment = curString[i]+pair_insertion[curString[i:i+2]]+curString[i+1]
                newString+=segment[0:2]
            if len(segment)==3:
                newString+=segment[2]

            return newString


        blah = polymerize()
        for i in range(2, 11):
            blah = polymerize(blah)
            print(i, blah)

        counter = Counter(blah)
        print(counter)

        maxVal = max(counter.values())
        minVal = min(counter.values())

        return maxVal-minVal

def main():
    s = Solution()
    print(s.solution(s.args))

if __name__ == '__main__':
    main()