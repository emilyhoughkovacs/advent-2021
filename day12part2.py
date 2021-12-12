import sys
import os

class Solution(object):
    def __init__(self):
        self.args = [arg for arg in sys.argv[1:]]

    def solution(self, args):

        # uses first command line arg if exists else inputfile.txt
        file = args[0] if args and os.path.isfile(args[0]) else 'inputday12.txt'
        f = open(file, 'r')
        lines = f.read().splitlines()
        f.close()

        lines = [line.split('-') for line in lines]

        global graph
        graph = {}
        for x, y in lines:
            if x not in graph:
                graph[x] = [y]
            else:
                graph[x] += [y]
            if y not in graph:
                graph[y] = [x]
            else:
                graph[y] += [x]

        for key, val in graph.items():
            print(key, val)

        def is_small_cave(node):
            if node.lower()==node:
                return True
            else:
                return False

        def find_all_paths(graph=graph, start='start', end='end', path=[]):
            path = path + [start]
            if start == end:
                return [path]
            if start not in graph:
                return []
            paths = []

            for node in graph[start]:
                smallNodes = [cave for cave in path if cave.lower()==cave ]
                # print("smallNodes:", smallNodes)

                if node.upper()==node or node not in path or len(smallNodes) == len(set(smallNodes)):
                    newpaths = find_all_paths(graph, node, end, path)
                    for newpath in newpaths:
                        paths.append(newpath)
            return paths 

        all_paths = [x for x in find_all_paths() if x.count('start')==1]
            
        return len(all_paths)

def main():
    s = Solution()
    print(s.solution(s.args))

if __name__ == '__main__':
    main()