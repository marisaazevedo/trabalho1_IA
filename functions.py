from auxFunctions import Puzzle
from collections import deque

def dfs(root: list[int], final: list[int]) -> Puzzle: #retornar a configuracao ou seja o puzzle??
    stack = deque() #criar uma pilha
    stack.append(Puzzle(root)) # adicionar a matriz atual a pilha
    visited = set() # criar um tuplo para as matrizes visitadas

    while len(stack):
        puzzle = stack.pop() # atribuir à variável puzzle o último elemento da pilha
        print(puzzle.array, len(visited))

        if tuple(puzzle.array) in visited: #verificar se puzzle já visitamos
            continue
        visited.add(tuple(puzzle.array))

        if puzzle.array == final: #comparar a configuração atual com a pretendida
            return puzzle.depth

        if tuple(puzzle.left())not in visited:
            stack.append(Puzzle(puzzle.left(), depth = puzzle.depth + 1))
        if tuple(puzzle.right())not in visited:
            stack.append(Puzzle(puzzle.right(), depth = puzzle.depth + 1))
        if tuple(puzzle.up())not in visited:
            stack.append(Puzzle(puzzle.up(), depth = puzzle.depth + 1))
        if tuple(puzzle.down())not in visited:
            stack.append(Puzzle(puzzle.down(), depth = puzzle.depth + 1))

    raise Exception("Puzzle cannot be solved")

def bfs(root: list[int], final: list[int]):
    queue = deque()
    queue.append(Puzzle(root))
    visited = set()

    while len(queue):
        puzzle = queue.popleft() # atribuir à variável puzzle o último elemento da pilha
        print(puzzle.array, len(visited))

        if tuple(puzzle.array) in visited: #verificar se puzzle já visitamos
            continue
        visited.add(tuple(puzzle.array))

        if puzzle.array == final: #comparar a configuração atual com a pretendida
            return puzzle.depth

        if tuple(puzzle.left())not in visited:
            queue.append(Puzzle(puzzle.left(), depth = puzzle.depth + 1))
        if tuple(puzzle.right())not in visited:
            queue.append(Puzzle(puzzle.right(), depth = puzzle.depth + 1))
        if tuple(puzzle.up())not in visited:
            queue.append(Puzzle(puzzle.up(), depth = puzzle.depth + 1))
        if tuple(puzzle.down())not in visited:
            queue.append(Puzzle(puzzle.down(), depth = puzzle.depth + 1))

    raise Exception("Puzzle cannot be solved")

def idfs(i,f):
    return 0

def aStar_misplaced(i,f):
    return 0
def aStar_manhattan(i,f):
    return 0

def greedy_misplaced(i,f):
    return 0
def greedy_manhattan(i,f):
    return 0

##1: GeneralSearchAlgorithm(QueueingFunction,configInicial,configFinal)
##2: if thereIsNoSolution(configInicial,configFinal) then
##3:    return “It is impossible to reach a solution”
##4: end if
##5: queue = configInicial
##6: while queue not empty do
##7:    node = removeFrontNodeFrom(queue)
##8:    if node is solution then
##9:        return Path to solution
##10:   end if
##11:   descendantList = MakeDescendants(node)
##12:   insert(descendantList,queue,QueueingFunction)
##13: end while
##14: return “solution not found”
