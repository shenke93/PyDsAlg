from os import listdir, getcwd
from os.path import isfile, join
from collections import deque 

def printnames_bfs(start_dir):
    search_queue = deque()
    search_queue.append(start_dir)
    while search_queue:
        dir = search_queue.popleft()
        for file in sorted(listdir(dir)):
            fullpath = join(dir, file)
            if isfile(fullpath):
                print(file)
            else:
                search_queue.append(fullpath)

def printnames_dfs(start_dir):
    for file in sorted(listdir(dir)):
        fullpath = join(dir, file)
        if isfile(fullpath):
            print(file)
        else:
            printnames_dfs(fullpath)

if __name__ == '__main__':
    printnames_bfs(getcwd())
    print("\n")
    printnames_bfs(getcwd())