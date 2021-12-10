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

        def get_left(arr, x, y):
            if y>0:
                return arr[x][y-1]

        def get_right(arr, x, y):
            if y<len(arr[0])-1:
                return arr[x][y+1]

        def get_above(arr, x, y):
            if x>0:
                return arr[x-1][y]

        def get_below(arr, x, y):
            if x<len(arr)-1:
                return arr[x+1][y]

        def in_bounds(arr, x, y):
            if x>=0 and y>=0 and x<len(arr) and y<len(arr[0]):
                return True
            else:
                return False

        basin = [[2, 2]]
        def get_adjacent(arr, x, y):
            if get_left(arr, x, y) and arr[x][y-1]>arr[x][y] and arr[x][y-1]<9 and arr[x][y-1] not in basin:
                basin.append([x, y-1])
                get_adjacent(arr, x, y-1)
            if get_right(arr, x, y) and arr[x][y+1]>arr[x][y] and arr[x][y+1]<9 and arr[x][y+1] not in basin:
                basin.append([x, y+1])
                get_adjacent(arr, x, y+1)
            if get_above(arr, x, y) and arr[x-1][y]>arr[x][y] and arr[x-1][y]<9 and arr[x-1][y] not in basin:
                basin.append([x-1, y])
                get_adjacent(arr, x-1, y)
            if get_below(arr, x, y) and arr[x+1][y]>arr[x][y] and arr[x+1][y]<9 and arr[x+1][y] not in basin:
                basin.append([x+1, y])
                get_adjacent(arr, x+1, y)

            return basin

        theSum = 0
        lowPoints = list()
        for i in range(len(lines)):
            for j in range(len(lines[0])):
                currentSpot = lines[i][j]
                if i==0:
                    if j==0:
                        # top left
                        if currentSpot < get_right(lines, i, j) and currentSpot < get_below(lines, i, j):
                            lowPoints.append([i, j])
                            theSum+=currentSpot+1
                    elif j==len(lines[0])-1:
                        # top right
                        if currentSpot < get_below(lines, i , j) and currentSpot < get_left(lines, i, j):
                            lowPoints.append([i, j])
                            theSum+=currentSpot+1
                    elif currentSpot < get_below(lines, i , j) and currentSpot < get_left(lines, i, j) and currentSpot < get_right(lines, i, j):
                        # rest of top
                        lowPoints.append([i, j])
                        theSum+=currentSpot+1
                elif i==len(lines)-1:
                    if j==0:
                        # bottom left
                        if currentSpot < get_above(lines, i, j) and currentSpot < get_right(lines, i, j):
                            lowPoints.append([i, j])
                            theSum+=currentSpot+1
                    elif j==len(lines[0])-1:
                        # bottom right
                        if currentSpot < get_above(lines, i, j) and currentSpot < get_left(lines, i, j):
                            lowPoints.append([i, j])
                            theSum+=currentSpot+1
                    elif currentSpot < get_above(lines, i, j) and currentSpot < get_left(lines, i, j) and currentSpot < get_right(lines, i, j):
                        # rest of bottom
                        lowPoints.append([i, j])
                        theSum+=currentSpot+1
                elif j==0:
                    # left except top and bottom
                    if currentSpot < get_above(lines, i, j) and currentSpot < get_below(lines, i , j) and currentSpot < get_right(lines, i, j):
                        lowPoints.append([i, j])
                        theSum+=currentSpot+1
                elif j==len(lines[0])-1:
                    # right except top and bottom
                    if currentSpot < get_above(lines, i, j) and currentSpot < get_below(lines, i , j) and currentSpot < get_left(lines, i, j):
                        lowPoints.append([i, j])
                        theSum+=currentSpot+1
                elif currentSpot < get_above(lines, i, j) and currentSpot < get_below(lines, i , j) and currentSpot < get_left(lines, i, j) and currentSpot < get_right(lines, i, j):
                    # interior
                    lowPoints.append([i, j])
                    theSum+=currentSpot+1

        def unique(list1):
            unique_list = list()
            for x in list1:
                if x not in unique_list:
                    unique_list.append(x)

            return unique_list

        # print(lowPoints)
        
        lengths = list()
        for x in lowPoints:
            basin = [x]
            lengths.append(len(unique(get_adjacent(lines, x[0], x[1]))))
        lengths = sorted(lengths, reverse=True)

        return lengths[0]*lengths[1]*lengths[2]

def main():
    s = Solution()
    print(s.solution(s.args))

if __name__ == '__main__':
    main()