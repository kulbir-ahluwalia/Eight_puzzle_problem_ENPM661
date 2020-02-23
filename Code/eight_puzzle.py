import numpy as np
import os

##############################################################################################################
# Functions to get the initial state of the eight puzzle from the user, check for repitition and solvability
##############################################################################################################

# Code to take initial state of the eight puzzle problem
def initial_state():
    print("Enter the initial state of the eight puzzle problem row wise")
    start_node = [0,0,0, 0,0,0, 0,0,0]
    for i in range(9):
        value = int(input("Enter the " + str(i+1) + "th value of the eight puzzle\n"))
        if value >8 or value<0:
            print("Enter a value from 0 to 8 only, Run program again please")
            exit(0)
          
        else:
            start_node[i] = value            
    return start_node

# Code to check for repetition of numbers
def repetition_check(node_for_check):  
    for x in range(9):  
        no_of_repetition = 0      
        entry = node_for_check[x]
        for y in range(9):
            if entry == node_for_check[y]:
                no_of_repetition = no_of_repetition + 1
             
        if no_of_repetition >= 2:
            print("An entry for the eight puzzle has been repeated, Please restart program")
            exit(0)

# test code to check if the eight puzzle is solvable or not
def check_solvability(node_check):
    inversions = 0
    for x in range(len(node_check)):
        for y in range(len(node_check[(x+1):])):
            # Uncomment following line to see the values being compared
            #print(node_check[x],"  ", node_check[x+y+1])
            # to ignore the blank tile
            if node_check[x+y+1]>0:
                if node_check[x] > node_check[x+y+1]:
                    inversions = inversions + 1
    #print(inversions) #to check the number of inversions
    
    if inversions % 2 == 0:
        return True
    else:
        return False

# Uncomment the following test code to print all the combinations for solvability check along with indexes
# for x in range(len(start_node)):
#     print("x is", x)
#     for y in range(len(start_node[(x+1):])):
#         print("y is", y)
#         print("Upper range of y", len(start_node[(x+1):]))
#         print(start_node[x],start_node[x+y+1])
#         print("x+y+1 is: ",x+y+1)
#         print("---------")

####################################################################################################
# Functions to find the location of the blank tile, move it to the left, right, up and down
####################################################################################################

# function to calculate the location of the zero tile and return the location as zero_position 
def BlankTileLocation(input_node):  
    for i in range(0,len(input_node)):           
            if (input_node[i] == 0):
                zero_position = i
    return zero_position

# function to move the blank (zero) tile left
def ActionMoveLeft(node_zero_unmoved):
    zero_position = BlankTileLocation(node_zero_unmoved)
    node_zero_moved = list(node_zero_unmoved)
    if zero_position in [0,3,6]:
        possibility = False
        return possibility, node_zero_moved
    else:
        node_zero_moved[zero_position] = node_zero_moved[zero_position-1]
        node_zero_moved[zero_position-1] = 0
        possibility = True
        return possibility, node_zero_unmoved, node_zero_moved

# function to move the blank (zero) tile right
def ActionMoveRight(node_zero_unmoved):
    zero_position = BlankTileLocation(node_zero_unmoved)
    node_zero_moved = list(node_zero_unmoved)
    if zero_position in [2,5,8]:
        possibility = False
        return possibility, node_zero_moved
    else:
        node_zero_moved[zero_position] = node_zero_moved[zero_position+1]
        node_zero_moved[zero_position+1] = 0
        possibility = True
        return possibility, node_zero_unmoved, node_zero_moved

# function to move the blank (zero) tile up
def ActionMoveUp(node_zero_unmoved):
    zero_position = BlankTileLocation(node_zero_unmoved)
    node_zero_moved = list(node_zero_unmoved)
    if zero_position in [0,1,2]:
        possibility = False
        return possibility, node_zero_moved
    else:
        node_zero_moved[zero_position] = node_zero_moved[zero_position-3]
        node_zero_moved[zero_position-3] = 0
        possibility = True
        return possibility, node_zero_unmoved, node_zero_moved

# function to move the blank (zero) tile down
def ActionMoveDown(node_zero_unmoved):
    zero_position = BlankTileLocation(node_zero_unmoved)
    node_zero_moved = list(node_zero_unmoved)
    if zero_position in [6,7,8]:
        possibility = False
        return possibility, node_zero_moved
    else:
        node_zero_moved[zero_position] = node_zero_moved[zero_position+3]
        node_zero_moved[zero_position+3] = 0
        possibility = True
        return possibility, node_zero_unmoved, node_zero_moved























start_node = initial_state()
print("The initial state in row wise representation is  : ", start_node)    

repetition_check(start_node)


goal_node = [1,2,3,4,5,6,7,8,0]
print("The goal state in row wise representation is  : ", goal_node) 


# function to write all the explored states in Nodes.txt
def nodes_explored(node_explored):
    if os.path.exists("Nodes.txt"):
      os.remove("Nodes.txt")
    
    f = open('Nodes.txt', 'r+') 
    for node in node_explored:
        f.write(str(data) + '\n')
    f.close()

# function to write child node index, parent node index and cost in NodesInfo.txt
def node_info(node_info):
    if os.path.exists("NodesInfo.txt"):
      os.remove("NodesInfo.txt")
    
    f = open('NodesInfo.txt', 'r+') 
    for node in node_info:
        f.write(str(data) + '\n')
    f.close()

# function to store all the steps from the start state to goal state in nodePath.txt
def final_path_for_solving(node_path):
    if os.path.exists("nodePath.txt"):
      os.remove("nodePath.txt")
    
    f = open('nodePath.txt', 'r+') 
    for node in node_path:
        f.write(str(data) + '\n')
    f.close()






