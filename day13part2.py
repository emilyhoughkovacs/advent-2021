import sys
import os

class Solution(object):
    def __init__(self):
        self.args = [arg for arg in sys.argv[1:]]

    def solution(self, args):

        # uses first command line arg if exists else inputfile.txt
        file = args[0] if args and os.path.isfile(args[0]) else 'inputday13.txt'
        f = open(file, 'r')
        lines = f.read()
        f.close()

        lines = lines.split('\n\n')
        dots = lines[0].split('\n')
        instructions = lines[1].split('\n')
        dots = [x.split(',') for x in dots]
        dots = [[int(x[0]), int(x[1])]for x in dots]

        instructions = [x.split(' ')[2] for x in instructions]
        instructions = [x.split('=') for x in instructions]
        instructions = [[x[0], int(x[1])] for x in instructions]

        # instruction = instructions[0]

        def fold(instruction, dots=dots):
            for i in range(len(dots)):
                if instruction[0]=='y':
                    if dots[i][1]>instruction[1]:
                        subtract = (dots[i][1]-instruction[1])*2
                        dots[i] = [dots[i][0], dots[i][1]-subtract]
                if instruction[0]=='x':
                    if dots[i][0]>instruction[1]:
                        subtract = (dots[i][0]-instruction[1])*2
                        dots[i] = [dots[i][0]-subtract, dots[i][1]]
            return dots

        def show_dots(dots=dots):
            x = 0
            y = 0
            for i, j in dots:
                if i>x:
                    x = i
                if j>y:
                    y = j

            line = ''
            for b in range(y+1):
                for a in range(x+1):
                    if [a, b] in dots:
                        line+=("#")
                    else:
                        line+=(".")
                line+="\n"
            return line

        for line in instructions:
            dots = fold(line)

        return show_dots()

def main():
    s = Solution()
    print(s.solution(s.args))

if __name__ == '__main__':
    main()