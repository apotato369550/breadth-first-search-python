import Queue

def createMaze():
    maze = []

def printMaze():
    return

def valid(maze, moves):
    return

def findEnd(maze, moves):
    return

nums = Queue.Queue()
nums.put("")
add = ""
maze = createMaze()

while not findEnd(maze, add):
    add = nums.get()
    for direction in ["L", "R", "U", "D"]:
        put = add + direction
        if valid(maze, put):
            nums.put(put)