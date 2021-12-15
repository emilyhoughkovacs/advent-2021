import sys
import os
from collections import Counter
from collections import defaultdict

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

        global pairs
        pairs = {line.split(" -> ")[0]:line.split(" -> ")[1] for line in lines[2:]}
        for key in pairs.keys():
            pairs[key] = key[0]+pairs[key]+key[1]

        polymer_dict =defaultdict(int)
        for i in range(len(polymer_template)-1):
            segment = polymer_template[i:i+2]
            polymer_dict[segment]+=1
        lastSeg = segment

        def polymerize(polyDict=polymer_dict):
            newDict = defaultdict(int)
            for x in polyDict.keys():
                if x in pairs.keys():
                    newDict[pairs[x][0:2]] += polyDict[x]
                    newDict[pairs[x][1:3]] += polyDict[x]
                else:
                    print("hello")
                    newDict[x] += polyDict[x]+1

            return newDict

        def count_polymer(polyDict, template=polymer_template):
            counts = defaultdict(int)
            for x in polyDict.keys():
                counts[x[0]] += polyDict[x]
            counts[template[-1]] += 1
            return counts

        poly = polymerize()
        for i in range(2, 41):
            poly = polymerize(poly)


        print("=======")
        print(count_polymer(poly))
        print(max(count_polymer(poly).values()))
        print(min(count_polymer(poly).values()))

        maxVal = max(count_polymer(poly).values())
        minVal = min(count_polymer(poly).values())
        print("=======")

        return maxVal-minVal

def main():
    s = Solution()
    print(s.solution(s.args))

if __name__ == '__main__':
    main()