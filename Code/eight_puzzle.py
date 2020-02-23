# Code to take initial state of the eight puzzle problem

def initial_state():
    print("Enter the initial state of the eight puzzle problem element wise")
    start_node = [0,0,0, 0,0,0, 0,0,0]
    for i in range(9):
        value = int(input("Enter the " + str(i+1) + "th value of the eight puzzle\n"))
        if value >8 or value<0:
            print("Enter a value from 0 to 8 only, Run program again please")
            exit(0)
          
        else:
            start_node[i] = value
            
    print("The initial state in row wise representation is : ", start_node) 


initial_state()