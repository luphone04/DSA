#MAZE FINDING THE SHORTEST PATH


# relative distance of above, below, left, and right cells
adj = [(0,-1),(0,1),(-1,0),(1,0)]
#bunch of tuples representing different directions x and y
# (0, -1) represents a movement in the negative y direction (upward).
# (0, 1) represents a movement in the positive y direction (downward).
# (-1, 0) represents a movement in the negative x direction (left).
# (1, 0) represents a movement in the positive x direction (right).

def valid(r,c): #checks whether a given position (r, c) is a valid cell within a 10x10 grid and whether 
               #that cell has not been visited before (based on the steps matrix). 
    
    
    global steps #can be accessed and modified within the function.
    
    if r >= 0 and r < 10 and c >= 0 and c < 10: #checks if r and c are within the bounds of a 10x10 grid
        if steps[r][c] == 0: #checks if the cell has been visited before. 0 represents an unvisited cell.
            return True 
    return False
# checks whether a given position (r, c) is a valid cell within a 10x10 grid and whether that cell has not 
# been visited before (based on the steps matrix). 
#r represents the row and c represents the column

# return True if coordinate (r,c) is not outside the matrix
    # and is not a part of a wall

'''
maze:  the input maze
ends:  the list of source and destination coordinates
steps: matrix that stores the minimum number of steps from
       the source coordinate to each visited maze cell.
       = -1 if the cell is part of a wall.
'''

# Read input maze
maze = [] #list of strings representing the maze (10x10)
ends = [] #list of tuples representing the source and destination coordinates
for r in range(10):
    maze.append(input()) #adds the input to the maze list (10x10) 

# Set up the steps matrix
#creates a 10x10 grid where all elements are initialized to zero.
steps = [[0]*10 for r in range(10)] #[[0] * 10] creates a list containing ten zeros: [0, 0, 0, 0, 0, 0, 0, 0, 0, 0].
                                    #the outer [ ] creates a list of these lists, repeating it ten times. 
for r in range(10): #for each row in the 10x10 grid
    for c in range(10): #for each column in the 10x10 grid
        #maze[r][c] represents the character at row r and column c in the maze. The syntax is used to access row and column of 
        # a 2D list.
        if maze[r][c] == '#': 
            steps[r][c] = -1
        if maze[r][c] == 'X':
            ends.append((r,c)) #ends is a list of coordinates representing endpoints or goal positions in your maze
            #To keep track of this endpoint, it creates a tuple (r, c) representing the row and column indices of the 
            # endpoint and appends this tuple to the ends list.

# Breadth-First Search       
Queue = [] #list of tuples representing the coordinates of the cells to be visited
# Fill in the code below

Queue.append((ends[0],0)) #adds the first endpoint from the ends list along with a distance or level 
                         #value of 0. 0 represents the initial distance or level associated with the starting position
                         # used in BFS to keep track of how far away each position is from the starting point. 
while Queue != []: # continues as long as the Queue is not empty. The BFS algorithm continues until 
                    #all nodes or positions have been explored.
    # In each iteration of the loop, it dequeues the front node (position) from the Queue
    #(r, c) represents the coordinates of the current position, and d represents the distance or level 
    # associated with this position.
    (r,c),d = Queue.pop(0) # tuple unpacking
    steps[r][c] = d #It updates the steps matrix with the distance or level value for the current position (r, c)
    for dr,dc in adj: #dr is the change in row and dc is the change in column
        if valid(r+dr,c+dc): #checks if the neighboring position is valid
            # r + dr and c + dc represent relative position changes:
            # r and c are the current row and column indices, respectively.
            # dr and dc represent changes or offsets in the row and column indices, respectively. 
            # These changes indicate the direction or movement you want to apply from the current position.
            # By adding dr to r and dc to c, you calculate the new row and column indices that result from 
            # moving in the specified direction. This is a common technique in grid-based algorithms to
            # navigate neighboring positions.

            Queue.append(((r+dr,c+dc),d+1))
            # enqueues that position along with an incremented distance (d + 1) to the Queue. 
            # This step represents the BFS process of moving to neighboring positions and marking their 
            # distances or levels accordingly.

            #(r + dr, c + dc) represents the coordinates of the neighboring position, and d + 1 represents 
            # the distance or level associated with the new position. In the context of breadth-first search 
            # (BFS) or similar algorithms, this value is typically incremented by 1 from the distance (d) 
            # associated with the current position. It indicates that you're moving one step further from 
            # the current position.

# Print the steps matrix
# for r in range(10):
#     for c in range(10):
#         print("%3d" % steps[r][c],end='')
#     print()

#print the minimum number of steps from the source to the destination
print(steps[ends[1][0]][ends[1][1]])


# adj = [(0, -1), (0, 1), (-1, 0), (1, 0)]

# def valid(r, c):
#     global steps
#     if r >= 0 and r < 10 and c >= 0 and c < 10:
#         if steps[r][c] == 0:
#             return True
#     return False

# maze = []
# ends = []
# for r in range(10):
#     maze.append(input())

# steps = [[0] * 10 for r in range(10)]

# for r in range(10):
#     for c in range(10):
#         if maze[r][c] == '#':
#             steps[r][c] = -1
#         if maze[r][c] == 'X':
#             ends.append((r, c))

# Queue = []
# Queue.append((ends[0], 0))

# while Queue != []:
#     (r, c), d = Queue.pop(0)
#     steps[r][c] = d #rear 
#     for dr, dc in adj:
#         if valid(r + dr, c + dc):
#             Queue.append(((r + dr, c + dc), d + 1))

# print(steps[ends[1][0]][ends[1][1]])






    


                


        

