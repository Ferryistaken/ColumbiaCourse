import sys
import time
from domino import Domino
from domino import Node
import queue
# Sample Input:
# Max size of the frontier
# Max Depth/Max states/Max runtime
# Set of dominoes
# Flag determining the type of output

if len(sys.argv) != 2:
    print("Not enough or too many arguments")
    print("Usage: solve.py <path to input file>")
    print("Example: $ solve.py ../input.txt")
    sys.exit(1)

# get the input file path as a command line argument
inputPath = sys.argv[1]
with open(inputPath, 'r') as file:
    input = file.read().replace('\n', '|')

# if the file has an empty line at the bottom delete it
if input[-1] == "|":
    input = input[:-1]

input = input.split("|")

maxFrontierSize = input[0]
maxDepth = input[1]

if input[2] == 0:
    verbose = False
else:
    verbose = True

dominoesNumber = input[3]
# from line 4 to end of file
rawDominoes = input[4:]

'''
print("Max frontier size: " + maxFrontierSize)
print("Max State number: " + maxStateNumber)
print("Verbose: " + str(verbose))
print("Number of dominoes: " + dominoesNumber)
print("Dominoes: ")
print(dominoes)
'''
# dict containig <Domino Name> : <Domino Object>
dominoes = {}
# serialize dominoes and store them in the dominoes dict
for i in range(0, int(dominoesNumber)):
    tempDomino = rawDominoes[i].split(" ")
    tempDomino.pop(0)
    dominoes["D" + str(i)] = Domino(tempDomino[0], tempDomino[1])

'''
for i in dominoes:
    print(i)
    print(dominoes[i])
'''

def bfs(dominoes, maxFrontierSize, maxDepth, verbose, dominoesNumber):
    maxFrontierSize = int(maxFrontierSize)
    frontier = queue.Queue()
    explored = set()
    depth = 0
    # first element is the difference, second is the "position" of the difference (top or bottom)
    initialState = Node()
    # check if initial state is the goal state
    frontier.put(initialState)
    while True:
        if frontier.qsize() > maxFrontierSize:
            print("Reached frontier limit")
            sys.exit(1)
        elif frontier.qsize() == 0:
            print("No more items in frontier")
            sys.exit(1)
        node = frontier.get()
        for i in dominoes:
            # node with parent node=<node>, addedDomino= domino in for loop, and empy addedDomino list
            childNode = Node(node, dominoes[i], node.addedDominoList)
            childNode.addedDominoList.append(i)
            if childNode.state not in explored or childNode.state not in queue:
                if childNode.state.isASolution():
                    print("Found A Solution!")
                    print(childNode.addedDominoList)
                    print(childNode.backtrack())
                    return False
                else:
                    frontier.put(childNode)
                    print("Viable Node: ")
                    print(childNode.addedDomino)
        explored.add(node.state)


bfs(dominoes, maxFrontierSize, maxDepth, verbose, dominoesNumber)
