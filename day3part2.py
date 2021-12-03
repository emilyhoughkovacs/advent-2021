import sys
import os

class Solution(object):
    def __init__(self):
        self.args = [arg for arg in sys.argv[1:]]

    def bitOxygen(self, args):
        length = len(args)
        theSum = 0
        theSum= sum(args)
        if theSum >= length/2:
            return '1'
        else:
            return '0'


    def bitCo2(self, args):
        length = len(args)
        theSum = 0
        theSum= sum(args)
        if theSum < length/2:
            return '1'
        else:
            return '0'

    def solution(self, args):

        # uses first command line arg if exists else inputfile.txt
        file = args[0] if args and os.path.isfile(args[0]) else 'inputday3.txt'
        f = open(file, 'r')
        lines = f.read().splitlines()
        f.close()

        lines = [x for x in lines]
        oxyLines = lines
        co2Lines = lines
        oxygen = ''
        co2 = ''

        length = len(lines)

        for i in range(len(oxyLines[0])):
            keep = self.bitOxygen([int(x[i]) for x in oxyLines])
            oxyLines = [x for x in oxyLines if x[i]==keep]
            if len(oxyLines)==1:
                oxygen=oxyLines[0]

        for i in range(len(co2Lines[0])):
            keep = self.bitCo2([int(x[i]) for x in co2Lines])
            co2Lines = [x for x in co2Lines if x[i]==keep]
            if len(co2Lines)==1:
                co2=co2Lines[0]

        return int(oxygen, 2)*int(co2, 2)


def main():
    s = Solution()
    print(s.solution(s.args))

if __name__ == '__main__':
    main()