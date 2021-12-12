import sys
import os

class Solution(object):
    def __init__(self):
        self.args = [arg for arg in sys.argv[1:]]

    def solution(self, args):

        # uses first command line arg if exists else inputfile.txt
        file = args[0] if args and os.path.isfile(args[0]) else 'inputday11.txt'
        f = open(file, 'r')
        lines = f.read().splitlines()
        lines = [[int(x) for x in line] for line in lines]
        f.close()

        global points
        points = {}
        for x in range(len(lines)):
            for y in range(len(lines[x])):
                points[(x, y)] = lines[x][y]

        global flashed
        flashed = []

        def get_surrounding(pos):
            global points

            global flashed

            checks = [
                [ pos[0]-1, pos[1]   ],
                [ pos[0]+1, pos[1]   ],
                [ pos[0]+1, pos[1]+1 ],
                [ pos[0]+1, pos[1]-1 ],
                [ pos[0]-1, pos[1]+1 ],
                [ pos[0]-1, pos[1]-1 ],
                [ pos[0],   pos[1]-1 ],
                [ pos[0],   pos[1]+1 ],
            ]

            for i in checks:
                idx = (i[0], i[1])
                if idx in points:
                    points[idx]+=1
                    if points[idx]>9 and idx not in flashed:
                        flashed.append(idx)
                        get_surrounding(idx)
                        points[idx] = 0
            return None

        def take_round():
            global points
            global flashed

            for i, j in points:
                points[(i, j)]+=1
                if points[(i, j)]>9:
                    flashed.append((i, j))
                    get_surrounding((i, j))
                    points[(i, j)]=0
            for a, b in flashed:
                points[(a,b)]=0
            return points

        numFlashed = 0
        numRounds = 0
        while numFlashed!=100:
            take_round()
            numRounds+=1
            numFlashed=len(flashed)
            # print("numRounds, numFlashed: ", numRounds, numFlashed)
            flashed = []

        return numRounds

def main():
    s = Solution()
    print(s.solution(s.args))

if __name__ == '__main__':
    main()