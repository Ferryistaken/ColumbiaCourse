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
    sys.exit(66)

# get the input file path as a command line argument
inputPath = sys.argv[1]
with open(inputPath, 'r') as file:
    input = file.read().replace('\n', '|')

# if the file has an empty line at the bottom delete it
if input[-1] == "|":
    input = input[:-1]

input = input.split("|")

maxFrontierSize = input[0]
maxExploredSize = input[1]

if input[2] == "0":
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

maxFrontierSize = int(maxFrontierSize)
maxExploredSize = int(maxExploredSize)

def depthLimitedSearch(dominoes, state, limit):
    return recursiveDls(dominoes, state, limit)

def recursiveDls(dominoes, state, limit):
    if state.isASolution():
        # TODO: make the solutionset
        return "success"
    elif limit == 0:
        return "Limit Reached"
    else:
        limitReached = False
        for i in dominoes:
            childNode = Node(state, dominoes[i], state.addedDominoList)
            result = recursiveDls(dominoes, childNode, limit-1)
            if result == "Limit Reached":
                limitReached = True
            elif result == "success":
                return result
        if limitReached:
            return "Limit Reached"
        else:
            return "No solution Found"

def iterativeDeepening(state, limit):
    for depth in range(0, limit):
        result = depthLimitedSearch(dominoes, state, depth)
        if result == "Limit Reached":
            return result
        elif result == "success":
            return result
    return "Limit Reached"

solutionSet = []
bfsResult = ""
frontier = queue.Queue()


def bfs(dominoes, maxFrontierSize, maxExploredSize, verbose):
    global bfsResult
    global frontier
    global solutionSet
    explored = set()
    # first element is the difference, second is the "position" of the difference (top or bottom)
    initialState = Node()
    # check if initial state is the goal state
    # test
    frontier.put(initialState)
    while True:
        if frontier.qsize() > maxFrontierSize:
            bfsResult = "Failure"
            print("Reached frontier limit")
            break
        elif len(explored) > maxExploredSize:
            bfsResult = "Failure"
            print("Reached explored nodes limit")
            sys.exit(1)
        else:
            node = frontier.get()
            for i in dominoes:
                # node with parent node=<node>, addedDomino= domino in for loop, and empy addedDomino list
                childNode = Node(node, dominoes[i], node.addedDominoList)
                # add the key to the added domino list (not the actual domino object)
                childNode.addedDominoList.append(i)
                #  solutionSet.append(i)
                if childNode.state not in explored:
                    if childNode.state == "invalid":
                        continue
                    elif childNode.state.isASolution():
                        bfsResult == "Solution"
                        print("Found A Solution!")
                        print(childNode.addedDominoList)
                        sys.exit(0)
                    else:
                        frontier.put(childNode)
                        explored.add(str(childNode))
                        if verbose:
                            print("Found a viable Node: " + str(childNode.addedDominoList))
                            print("Object: " + str(childNode.addedDomino))
            if len(explored) == 0 and frontier.qsize() == 0:
                bfsResult = "Failure"
                print("No solution possible")
                sys.exit(1)
            if len(explored) != 0 and frontier.qsize() == 0:
                bfsResult = "Failure"
                print("Explored is more than 0, but frontier is empty")
                sys.exit(1)

bfs(dominoes, maxFrontierSize, maxExploredSize, verbose)

def getIterableFrontier(q):
    l = []
    while q.qsize() > 0:
        l.append(q.get())
    return l


if bfsResult == "Failure":
    pass

if bfsResult != "Solution":
    limitReached = False
    # you cannot iterate a queue without removing items from it, so I iterate over a copy of it
    iterableFrontier = getIterableFrontier(frontier)
    for state in iterableFrontier:
        print("Iterable Fonteir")
        print(state)
        result = iterativeDeepening(state, maxExploredSize)
        if result == "success":
            break
        elif result == "Limit Reached":
            limitReached = True
    if result != "success":
        if limitReached == False:
            result = "failure"
        else:
            result = "Limit Reached"



if result == "success":
    pass
elif result == "Failure":
    print("No solution")
else:
    print("Limit Reached")


