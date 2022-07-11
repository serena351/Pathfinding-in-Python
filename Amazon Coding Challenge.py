#Setting up my environment:
from pathfinding.core.grid import Grid; #to create a grid
from pathfinding.core.diagonal_movement import DiagonalMovement #to allow diagonal movement
from pathfinding.finder.a_star import AStarFinder #importing A* pathfinding algorithm (this takes weights into
#account so all walkable nodes will be given the same weight)
import random #to generate random locations for the additional obstacles

#Phase 1
#Setting up a 10x10 grid with starting point, delivery point and 4 obstacles at 
#(0,0), (9,9), (9,7), (8,7), (7,7) and (6,8) respectively:

matrix = []
for i in range(10):
  matrix.append([1, 1, 1, 1, 1, 1, 1, 1, 1, 1])
matrix[7][7] = 0
matrix[6][8] = 0   #nodes with obstacles are given weight 0 as they are not walkable
matrix[8][7] = 0
matrix[9][7]= 0
#Calculating a valid path to the delivery point, avoiding obstacles:
def find_path(matrix):
  grid = Grid(matrix=matrix)
  start = grid.node(0, 0) 
  end = grid.node(9, 9)   
  finder = AStarFinder(diagonal_movement = DiagonalMovement.always)
  path, runs = finder.find_path(start, end, grid)
  if path != []:
    print('number of steps required: ', len(path))
    print('nodes visited: ', path)
  else:
    print("Unable to reach delivery point")

#Print path and number of steps required:
#solution format: [(x1, y1), (x2, y2), ...]

find_path(matrix) #already have print statement inside function to make code neater

#Phase 2
#Adding 20 randomly placed obstacles, ensuring they do not overlap existing ones:

obstacle_coords = []
while len(obstacle_coords) < 21:
  coord = (random.randint(0, 9), random.randint(0, 9))
  if coord != (6,8) and (7,7) and (8,7) and (9,7) and (0,0) and (9, 9):
    obstacle_coords.append(coord)
print('20 additional obstacles at: ',obstacle_coords)  #printing locations of new obstacles:
#Change 1s in these locations in matrix to 0s to represent obstacles:
for coord in obstacle_coords:
  matrix[coord[0]][coord[1]] = 0

#Calculate valid path to delivery point avoiding obstacles and print coordinates:

find_path(matrix)

