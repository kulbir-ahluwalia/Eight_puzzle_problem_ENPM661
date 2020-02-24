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


####################################################################################################
# Functions to compare nodes and stop when the goal_state is reached
####################################################################################################

# function to compare two nodes and make sure that the"node_to_checked" has not been explored before
# node from the node_explore_list is compared with the node passed to the function "compare_nodes"

def node_already_explored_or_not(node_to_be_checked, node_explore_list):
    for stored_node in node_explore_list:
        # stored_node is a node that has been explored before
        if stored_node == node_to_be_checked:
            return True
    return False
 

def goal_state_reached(node_to_be_checked_with_goal_state):
    if node_to_be_checked_with_goal_state == goal_node:
        return True

    else:
        return False

####################################################################################################
# functions to generate the required text files Nodes.txt, NodesInfo.txt and nodePath.txt
####################################################################################################

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

####################################################################################################
# SECTION TO RUN THE CODE AND USE ALL THE FUNCTIONS WE MADE 
####################################################################################################

# take input state of the eight puzzle from the user with values from [0,8]
start_node = initial_state()
print("The initial state in row wise representation is  : ", start_node)    

goal_node = [1,2,3,4,5,6,7,8,0]
print("The goal state in row wise representation is  : ", goal_node) 

# to check for repetition and solvability of the input state of the eight puzzle problem
# the program exits if any of the following functions fails

# to check for repetitive entries
repetition_check(start_node)
# to check if the input state of the eight puzzle is solvable or not
check_solvability(start_node)


# information like *index of node i* and *index of the parent of node i* is stored
Node_Index_i = 1
Parent_Node_Index_i = 0

# to initialise the list for storing information of each node
node_info = []
node_info.append([0,0])


# to initialise the list of all the nodes to be explored. It is a list of lists.
node_explore_list = []
node_explore_list.append(start_node)

for node_explore in node_explore_list:

    possibility, node_zero_unmoved, node_zero_moved = ActionMoveLeft(node_explore)











