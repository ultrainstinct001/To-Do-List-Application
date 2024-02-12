tasks= []


def addTask():
    task= input("Enter the task: ")
    tasks.append(task)
    print(f"Task '{task}' added to the list.")



def listTasks():
    if not tasks:
        print("there are no tasks currently.")

    else:
        print("current tasks: ")
        for index, task in enumerate(tasks,start=1):
            print(f"task #{index}. {task}")


def  deleteTask():
    listTasks()
    try:
        tasktodelete=int(input("choose the number of the task to delete: "))
        if tasktodelete >=1 and tasktodelete< len(tasks):
            tasks.pop(tasktodelete+1)
            print(f"Task {tasktodelete} has been removed")
        else:
            print(f"Task #{tasktodelete} was not found")
    except:
        print("Invalid input.")




if __name__=="__main__":
    print("Welecome to the To Do List")
    while True:
        # print("\n")
        print("\nPlease select one of the following options")
        print("------------------------------------------")
        print("1. Add a new task")
        print('2. Delete a task')
        print("3. List a task")
        print("4. Quit")


        choice=input("Enter your choice: ")

        if (choice=="1"):
            addTask()

        elif (choice=="2"):
            deleteTask()


        elif (choice=="3"):
            listTasks()


        elif (choice=="4"):
            break

        else:
            print("invalid input. Please try again.")
        
    print("Goodbye")