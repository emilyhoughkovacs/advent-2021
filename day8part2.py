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

        lines = [line.replace('|', '').split(' ') for line in lines]
        lines = [[''.join(sorted(word)) for word in line] for line in lines]
        [line.remove('') for line in lines]

        def getOneFourSevenEight(arr):
            for word in arr:
                if len(word)==2:
                    one = word
                if len(word)==3:
                    seven = word
                elif len(word)==4:
                    four = word
                elif len(word)==7:
                    eight = word
            return one, four, seven, eight

        def getSegmentZero(arr, one, seven):
            return [x for x in seven if x not in one][0]

        def getSegmentsTwoAndFive(arr, one):
            zeroSixNine = [x for x in arr if len(x)==6]
            for seg in one:
                if len([x for x in zeroSixNine if seg in x])==2:
                    segTwo = seg
            segFive = [x for x in one if x!=segTwo][0]
            six = [x for x in zeroSixNine if segTwo not in x][0]
            return segTwo, segFive, six

        def getSegmentsOneAndFour(arr, six):
            twoThreeFive = [x for x in arr if len(x)==5]
            segs = [[letter for letter in six if letter not in x] for x in twoThreeFive]
            for letters, nums in zip(segs, twoThreeFive):
                if len(letters)==1:
                    segFour = letters[0]
                    five = nums
            for letters, nums in zip(segs, twoThreeFive):
                if len(letters)==2 and segFour in letters:
                    three = nums
                    segOne = [letter for letter in letters if letter!=segFour][0]
                if len(letters)==2 and segFour not in letters:
                    two = nums

            return segOne, segFour, two, three, five

        theSum = 0

        for line in lines:
            segments = list(['' for _ in range(7)])

            one, four, seven, eight = getOneFourSevenEight(line)
            segments[0] = getSegmentZero(line[0:10], one, seven)
            segments[2], segments[5], six = getSegmentsTwoAndFive(line[0:10], one)
            segments[1], segments[4], two, three, five = getSegmentsOneAndFour(line[0:10], six)
            
            nums = [one, two, three, four, five, six, seven, eight]

            zeroAndNine = [num for num in line[0:10] if num not in nums]
            zero = [num for num in zeroAndNine if segments[4] in num][0]
            zeroAndNine.pop(zeroAndNine.index(zero))
            nums.insert(0, zero)
            nums.append(zeroAndNine[0])

            translated = int(''.join([str(nums.index(n)) for n in line[10:]]))
            print(translated)
            theSum+=translated

        print(theSum)

def main():
    s = Solution()
    print(s.solution(s.args))

if __name__ == '__main__':
    main()