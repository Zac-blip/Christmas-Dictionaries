"""
Name: Zion Clayborn
Date:12/9/24
Name of project:To do list
Description of project: Makes an itemized to do list of what the user adds or removes from the list allowing them to
 reset or print the list as they see fit.
Class period: 5
"""
#print the welcome
print("Welcome to To-Do list manager!")
print(""
      "")
todolist = []#holds existing strings representing tasks
def save_list():
    global todolist
    with open("data.txt", "w") as file:
        file.writelines(item + "\n" for item in todolist)

def load_list():
    global todolist
    with open("data.txt", "w") as file:
        todolist = [line.strip() for line in file]
def add_item(item):
    todolist.append(item)
def remove_item(item):
    print("You choose option 2")
    for c in range(0, len(todolist)):
        print(str(c + 1) + ". " + todolist[c])
    while True:
        choice = input("Which one to remove or q to quit?")
        if choice == "q":  # quit
            break
        if choice.isdigit():
            choice = int(choice) - 1
            if choice >= len(todolist) or choice < 0:  # checks choice
                print("Invalid choice")
            else:
                todolist.pop(choice)  # removes item
        else:
            print("Invalid choice")
def print_list(todolist):
    print("You choose option 3")
    if todolist:

    else:
        print("Your list is empty.")
def reset_todo_list():
    todolist.pop()  # removes list

#menu
while True:
    print("")
    print("Menu: ")
    print("Press 1 to add an item")
    print("Press 2 to remove an item")
    print("Press 3 to print the list")
    print("Press 4 to reset the list")
    print("Press 5 to quit")
    choice = input()
    #choice 1
    add_item(choice)
    if choice == "1":
            print("Enter the item to add: ")
            todolist.append(choice)#adds an item
# print("Item "" + item + "" added to list.")
#choice 2
    remove_item(choice)
    elif choice == "2":
            print("You choose option 2")
            for c in range(0, len(todolist)):
                print(str(c + 1) + ". " + todolist[c])
            while True:
                choice = input("Which one to remove or q to quit?")
                if choice == "q":#quit
                    break
                if choice.isdigit():
                    choice = int(choice) - 1
                    if choice >= len(todolist) or choice < 0:#checks choice
                        print("Invalid choice")
                    else:
                        todolist.pop(choice)#removes item
                else:
                    print("Invalid choice")
    #choice 3 gotta work on it
    print_list(todolist)
    #choice 4
    reset_list(todolist)
        elif choice == "4":
            todolist.pop()#removes list
    #choice 5
        elif choice =="5":
            print("Bye Bye!!")
            break
        else:
            print("Invalid choice")