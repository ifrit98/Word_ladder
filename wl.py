from graph import Graph
import sys

def buildGraph(file):
    """
    Creates buckets for each word that differs by one letter
    Adds edges to graph from completed buckets
    :param wordFile: Dictionary filename
    :return: Completed graph
    """
    dict = {}
    graph = Graph()
    wfile = open(file,'r')
    for line in wfile:
        word = line[:-1]
        for i in range(len(word)):
            bucket = word[:i] + '_' + word[i+1:]
            if bucket in dict:
                dict[bucket].append(word)
            else:
                dict[bucket] = [word]
    for bucket in dict.keys():
        for word1 in dict[bucket]:
            for word2 in dict[bucket]:
                if word1 != word2:
                    graph.addEdge(word1,word2)
    return graph

def BFS(start, end):
    """
    Traditional BFS using a list as a queue
    Searches through all neighbors to build path to target word if one exists
    :param start: starting word
    :param end: target word
    :return: path to target or None
    """
    queue = []
    queue.append(start)
    predecessors = {}
    predecessors[start] = None

    while len(queue):
        current = queue.pop(0)
        if current == end:
            break
        for neighbor in current.getConnections():
            if neighbor not in predecessors:
                predecessors[neighbor] = current
                queue.append(neighbor)

    if end in predecessors:
        path = []
        current = end
        while current != start:
            path.insert(0, current)
            current = predecessors[current]
        path.insert(0, start)
        return path
    else:
        return None

def main():
    assert len(sys.argv) > 1, 'Usage: length of argv must be > 1'
    wordFile = 'exampleWords.txt'
    g = buildGraph(wordFile)
    start = g.getVertex(sys.argv[1])
    end = g.getVertex(sys.argv[2])
    paths = []
    paths.append(BFS(start, end))
    paths.append(BFS(g.getVertex('small'), g.getVertex('short')))
    paths.append(BFS(g.getVertex('brook'), g.getVertex('drunk')))

    for current in paths:
        print('Path: ')
        if current is None:
            print('No path to word was found.')
        else:
            for vertex in current:
                print(vertex.id)
        print()

if __name__ == '__main__':
    main()