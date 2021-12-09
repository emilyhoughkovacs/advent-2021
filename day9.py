import sys
import os

class Solution(object):
    def __init__(self):
        self.args = [arg for arg in sys.argv[1:]]

    def solution(self, args):

        # uses first command line arg if exists else inputfile.txt
        file = args[0] if args and os.path.isfile(args[0]) else 'inputday9.txt'
        f = open(file, 'r')
        lines = f.read().splitlines()
        f.close()

        lines = [list(x) for x in lines]
        lines = [[int(y) for y in line] for line in lines]

        for line in lines:
            print(line)

        theSum = 0
        for i in range(len(lines)):
            for j in range(len(lines[0])):
                if i==0:
                    if j==0:
                        # top left
                        if lines[i][j] < lines[i+1][j] and lines[i][j] < lines[i][j+1]:
                            print(i, j, lines[i][j])
                            theSum+=lines[i][j]
                            theSum+=1
                    elif j==len(lines[0])-1:
                        # top right
                        if lines[i][j] < lines[i+1][j] and lines[i][j] < lines[i][j-1]:
                            print(i, j, lines[i][j])
                            theSum+=lines[i][j]
                            theSum+=1
                    elif lines[i][j] < lines[i+1][j] and lines[i][j] < lines[i][j-1] and lines[i][j] < lines[i][j+1]:
                        # rest of top
                        print( i, j, lines[i][j])
                        theSum+=lines[i][j]
                        theSum+=1
                elif i==len(lines)-1:
                    if j==0:
                        # bottom left
                        if lines[i][j] < lines[i-1][j] and lines[i][j] < lines[i][j+1]:
                            print(i, j, lines[i][j])
                            theSum+=lines[i][j]
                            theSum+=1
                    elif j==len(lines[0])-1:
                        # bottom right
                        if lines[i][j] < lines[i-1][j] and lines[i][j] < lines[i][j-1]:
                            print(i, j, lines[i][j])
                            theSum+=lines[i][j]
                            theSum+=1
                    elif lines[i][j] < lines[i-1][j] and lines[i][j] < lines[i][j-1] and lines[i][j] < lines[i][j+1]:
                        # rest of bottom
                        print(i, j, lines[i][j])
                        theSum+=lines[i][j]
                        theSum+=1
                elif j==0:
                    # left except top and bottom
                    if lines[i][j] < lines[i-1][j] and lines[i][j] < lines[i+1][j] and lines[i][j] < lines[i][j+1]:
                        print(i, j, lines[i][j])
                        theSum+=lines[i][j]
                        theSum+=1
                elif j==len(lines[0])-1:
                    # right except top and bottom
                    if lines[i][j] < lines[i-1][j] and lines[i][j] < lines[i+1][j] and lines[i][j] < lines[i][j-1]:
                        print(i, j, lines[i][j])
                        theSum+=lines[i][j]
                        theSum+=1
                elif lines[i][j] < lines[i-1][j] and lines[i][j] < lines[i+1][j] and lines[i][j] < lines[i][j-1] and lines[i][j] < lines[i][j+1]:
                    # interior
                    print(i, j, lines[i][j])
                    theSum+=lines[i][j]
                    theSum+=1


        return theSum

def main():
    s = Solution()
    print(s.solution(s.args))

if __name__ == '__main__':
    main()