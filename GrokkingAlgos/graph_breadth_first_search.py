from collections import deque

def breadth_first_search(name, graph):
    search_queue = deque()  # To store unsearched person
    search_queue += graph[name]
    searched = set()    # To store searched person
    while search_queue:
        person = search_queue.popleft()
        if not person in searched:
            if person_is_seller(person):
                print(person + "is a mango seller!")
                return True
            else: 
                search_queue += graph[person]
                searched.add(person)
    return False

def person_is_seller(name):
    return name[-1] == 'm'


if __name__ == '__main__':
    graph = {}
    graph["you"] = ["alice", "bob", "claire"]
    graph["bob"] = ["anuj", "peggy"] 
    graph["alice"] = ["peggy"] 
    graph["claire"] = ["thom", "jonny"] 
    graph["anuj"] = []
    graph["peggy"] = []
    graph["thom"] = []
    graph["jonny"] = []
    
    breadth_first_search("you", graph)