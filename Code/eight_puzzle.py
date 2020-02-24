# EIGHT PUZZLE PROBLEM
# Kulbir Ahluwalia

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
        return possibility, node_zero_unmoved, node_zero_moved
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
        return possibility, node_zero_unmoved, node_zero_moved
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
        return possibility, node_zero_unmoved, node_zero_moved
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
        return possibility, node_zero_unmoved, node_zero_moved
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
Parent_Node_Index_start_node = 0 #initialised with zero since the first node does not have a parent

# to initialise the list for storing information of each node
# the information is stored as [Node_Index_i, Parent_Node_Index_i]
node_info = []
node_info.append([Node_Index_i,Parent_Node_Index_start_node])  #initialised with zero

# to initialise the list of all the nodes to be explored. It is a list of lists.
node_explore_list = []
node_explore_list.append(start_node)

print("Working on finding the solution. Be patient for 2 minutes! :)")

# for the subsequently generated nodes, parent index is 1 for the first generation of generated nodes
Parent_Node_Index_i = 1

for node_i in node_explore_list:
    
    # we will shift the zero tiles in the order left, up, right and then down
    # we will also check if the movement is feasible or not
    
    ###########################################################################################
    # SHIFT ZERO TILE TO THE LEFT
    ###########################################################################################
    possibility, node_zero_unmoved, node_zero_moved = ActionMoveLeft(node_i)    
    # check if the new node has been explored before
    node_explored_or_not = node_already_explored_or_not(node_zero_moved, node_explore_list)
       
    if (possibility == True) and (node_explored_or_not == False):        
        #increment node index i for the new unexplored node
        Node_Index_i = Node_Index_i + 1
        # store the node index and its parent node's index
        node_info.append([Node_Index_i, Parent_Node_Index_i])
        # add the new node to the list of explored nodes        
        node_explore_list.append(node_zero_moved)
        
    if (goal_state_reached(node_zero_moved) == True):
        print("Goal state has been reached:  ", node_zero_moved)
        break
            
    
    
    ###########################################################################################
    # SHIFT ZERO TILE TO THE UP
    ###########################################################################################
    possibility, node_zero_unmoved, node_zero_moved = ActionMoveUp(node_i)    
    # check if the new node has been explored before
    node_explored_or_not = node_already_explored_or_not(node_zero_moved, node_explore_list)
       
    if (possibility == True) and (node_explored_or_not == False):        
        #increment node index i for the new unexplored node
        Node_Index_i = Node_Index_i + 1
        # store the node index and its parent node's index
        node_info.append([Node_Index_i, Parent_Node_Index_i])
        # add the new node to the list of explored nodes        
        node_explore_list.append(node_zero_moved)
        
    if (goal_state_reached(node_zero_moved) == True):
        print("Goal state has been reached:  ", node_zero_moved)
        break
    

    ###########################################################################################
    # SHIFT ZERO TILE TO THE RIGHT
    ###########################################################################################
    possibility, node_zero_unmoved, node_zero_moved = ActionMoveRight(node_i)    
    # check if the new node has been explored before
    node_explored_or_not = node_already_explored_or_not(node_zero_moved, node_explore_list)
       
    if (possibility == True) and (node_explored_or_not == False):        
        #increment node index i for the new unexplored node
        Node_Index_i = Node_Index_i + 1
        # store the node index and its parent node's index
        node_info.append([Node_Index_i, Parent_Node_Index_i])
        # add the new node to the list of explored nodes        
        node_explore_list.append(node_zero_moved)
        
    if (goal_state_reached(node_zero_moved) == True):
        print("Goal state has been reached:  ", node_zero_moved) 
        break 
            
            
    ###########################################################################################
    # SHIFT ZERO TILE TO THE DOWN
    ###########################################################################################
    possibility, node_zero_unmoved, node_zero_moved = ActionMoveDown(node_i)    
    # check if the new node has been explored before
    node_explored_or_not = node_already_explored_or_not(node_zero_moved, node_explore_list)
       
    if (possibility == True) and (node_explored_or_not == False):        
        #increment node index i for the new unexplored node
        Node_Index_i = Node_Index_i + 1
        # store the node index and its parent node's index
        node_info.append([Node_Index_i, Parent_Node_Index_i])
        # add the new node to the list of explored nodes        
        node_explore_list.append(node_zero_moved)
        
    if (goal_state_reached(node_zero_moved) == True):
        print("Goal state has been reached:  ", node_zero_moved)
        break
    
    # Increment the index for the parent node after every possible movement for the zero tile is achieved
    Parent_Node_Index_i = Parent_Node_Index_i + 1
              
# generate final path to goal
final_path_to_goal = []
# start the list with the node input by the user
final_path_to_goal.append(start_node)
# end the list with the goal node
final_path_to_goal.append(goal_node)

# find the total number of nodes generated for use in backtracking
total_numer_of_nodes = len(node_info)
# BACKTRACKING to generate the final path from start node to the goal node
backtrack = node_info[total_numer_of_nodes-1][1]

while backtrack != 1:
    # to find the parent nodes
    #print(backtrack)
    final_path_to_goal.insert(1, node_explore_list[backtrack])
    backtrack = node_info[backtrack][1]


####################################################################################################
# functions to generate the required text files Nodes.txt, NodesInfo.txt and nodePath.txt
####################################################################################################

# function to write all the explored states in Nodes.txt
# we write it in the column wise format

def nodes_explored(node_explored):
    if os.path.exists("Nodes.txt"):
        os.remove("Nodes.txt")
    
    f = open('Nodes.txt', 'w') 
    for node in node_explored:
        for i in range(3):
            for j in range(i,9,3):
                f.write(str(node[j]) + ' ')
        f.write("\n")
    
    f.close()

# function to write child node index, parent node index and cost in NodesInfo.txt
# we write it in the column wise format
def node_info_print(node_info):
    if os.path.exists("NodesInfo.txt"):
        os.remove("NodesInfo.txt")

      
    
    f = open('NodesInfo.txt', 'w') 
    for node in node_info:
        for i in [0,1]:
            f.write(str(node[i]) + ' ')
        f.write(str(0))
        f.write("\n")
    f.close()

# function to store all the steps from the start state to goal state in nodePath.txt
# we write it in the column wise format

def final_path_for_solving(node_path):
    if os.path.exists("nodePath.txt"):
        os.remove("nodePath.txt")
    
    f = open('nodePath.txt', 'w') 
    for node in node_path:
        for i in range(3):
            for j in range(i,9,3):
                f.write(str(node[j]) + ' ')
        f.write("\n")
    f.close()



nodes_explored(node_explore_list)
node_info_print(node_info)
final_path_for_solving(final_path_to_goal)





