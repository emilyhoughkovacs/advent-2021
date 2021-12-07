import sys
import os

class Solution(object):
    def __init__(self):
        self.args = [arg for arg in sys.argv[1:]]

    def solution(self, args):

        # uses first command line arg if exists else inputfile.txt
        file = args[0] if args and os.path.isfile(args[0]) else 'inputday4.txt'
        f = open(file, 'r')
        nums = [int(x) for x in f.readline().split(',')]
        f.readline()
        cards = list()
        for line in f:
            if line!="\n":
                cards.append(line.strip())
        f.close()

        cards = [x.split() for x in cards]
        cards = [[int(y) for y in x] for x in cards]
        cards = [cards[i:i+5] for i in range(0, len(cards), 5)]

        def check_for_wins(card):
            num_xs=0
            column=0
            for row in card:
                if row==['x', 'x', 'x', 'x', 'x']:
                    return True
            for row in range(len(card)):
                for column in range(len(card[0])):
                    # print(row, column, card[row][column])
                    if card[column][row]=='x':
                        num_xs+=1
                if num_xs==5:
                    return True
                num_xs=0

            return False

        def calculate_winner(nums=nums, cards=cards):
            for m in nums:
                for i in range(len(cards)):
                    for j in range(len(cards[0])):
                        for k in range(len(cards[0][0])):
                            # test if any matches
                            if cards[i][j][k]==m:
                                cards[i][j][k]='x'
                    if check_for_wins(cards[i])==True:
                        return m, i

        m, i = calculate_winner()

        for line in cards[i]:
            print (line)

        # calculate sum of all unmarked numbers
        theSum = 0
        for line in cards[i]:
            for item in line:
                if isinstance(item, int):
                    theSum+=item

        print(theSum)
        print(m)

        # multiply by number that was just called ("m")
        return theSum*m



def main():
    s = Solution()
    print(s.solution(s.args))

if __name__ == '__main__':
    main()