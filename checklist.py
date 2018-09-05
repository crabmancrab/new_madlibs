checklist=list()
def add_item(new_item,index):
    checklist[index]=new_item   

def remove_item(index):
    checklist.pop(index)
    return checklist
    
def check_item(index):
    return checklist[index]

def create_item(new_str):
    return checklist.append(new_str)

def list_items():
    index=0
    for i in checklist:
        print("{} {}".format(index, i))
        index+=1
        
def item_completed(index):
    checklist[index]="{} {}".format('√', checklist[index])
    
def user_input(prompt):
    # the input function will display a message in the terminal 
    # and wait for user input.
    user_input = input(prompt)
    return user_input
    
def select(function_code):
    # Create item
    running=True
    while running==True:
        if function_code == "C":
            input_item = user_input("Input item:")
            create_item(input_item)
            function_code=user_input("enter new command: ")
    
        # Read item
        elif function_code == "R":
            item_index = int(user_input("Index Number?"))
    
            # Remember that item_index must actually exist or our program will crash.
            check_item(item_index)
            function_code=user_input("enter new command: ")
            
    
        # Print all items
        elif function_code == "P":
            list_items()
            function_code=user_input("enter new command: ")
            
        elif function_code == "Q":
            running=False
            
        else:
            print("Unknown Option")
            function_code=user_input("enter new command: ")
    
            

def test():
    
    from termcolor import colored
    create_item("purple sox")
    create_item("red cloak")
    
    
    print(colored(check_item(0),"green"))
    print(check_item(1))

    add_item("purple socks",0)

    remove_item(1)

    print(check_item(0))

    list_items()
    
    # Call your new function with the appropriate value
    select("C")
    # View the results
    list_items()
    # Call function with new value
    select("R")
    # View results
    list_items()
    # Continue until all code is run
        
