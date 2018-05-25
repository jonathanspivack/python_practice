from collections import deque

graph = {}
graph['you'] = ["alice","bob","claire"]
graph['alice'] = ["peggy"]
graph['bob'] = ["anuj","peggy"]
graph['claire'] = ["thom","jonny"]
graph['anuj'] = {}
graph['peggy'] = {}
graph['thom'] = {}
graph['jonny'] = {}


def is_mango_seller(name):
    if name[-1] == "m":
        return True
    return False


def bfs():
    search_queue = deque()
    search_queue += graph["you"]
    seen = []
    while search_queue:
        person = search_queue.popleft()
        print(person)
        if person not in seen:
            if is_mango_seller(person):
                print(person, "person is a mango seller!")
                return True
            else:
                search_queue += graph[person]
                seen.append(person)

    return False


print(bfs())
