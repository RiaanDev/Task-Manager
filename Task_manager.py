import sys

# Saves variables that would be used in the log in system as false to be turned as true 
close = False
login = False
user_names = ""
user_passwords = ""
logged_in = False

# Opening files
tasks = open("tasks.txt","r")
users = open("user.txt","r")

# Strip and splits the file content to be more recognizing for the system
for line in users:
    temp = line.strip()
    temp = temp.split(", ")
    user_names += temp[0]
    user_passwords += temp[1]

# Closes files
tasks.close()
users.close()

#Greets the user
print ("Welcome to task manager \n")

# Logging in
# Lets the user enter his username an password while logged in is false and if it is correct logged in becomes true
while logged_in == False:           
    username = input("Username: ")
    password = input("Password: ")

    # If the user is not recognized it wil tel the user what is in correct his username or password and gives him a chance to re-enter
    if username not in user_names:
        print("\nThe username you entered does not exist")
    elif password not in user_passwords:
        print("\nThe password you entered is incorrect")
    else:
        logged_in = True # If the user is recognized and password and username is correct logged in is true which opens the menu

def register ():
    user_ds = 0     # Saves user_ds as 0
    if username != "Admin" and password != "Adm1n": # If the username that the user has used is not equal to Admin as well as with the password not equal to Adm1n
        print ("Sorry you are not Authorized")      # This message is printed out which denies the user from accesing
        # If the username and password is equal to Admin and Adm1n the admin stuff can continue adding a new user
    else:
        name = input("Enter a username: ")
        passw = input ("Enter a password: ")
        confirm = input ("Confirm your password: ")
        with open ('user.txt','r+') as file:
            user_in_file = False  
            while user_in_file == False:
                if name in file:
                    print ("Username already exists")
                    break

                elif passw in file:
                    print ("Password already exists")
                    break
                else:
                    user_in_file = True
            
        if user_in_file == True:
            if confirm  == passw:                           # If the confirmed password matches the password he first entered...
                with open ('user.txt','a') as file:         # The input is stored in a file
                    file.write(name + ", " + passw + "\n" ) # The new content is saved as Username, Password
                    user_ds += 1                            # If a user is added one is being added to user_ds
            else:
                print ("Passwords does not match")          # If the confirmed password and password doesn't atch the content cant be saved

# If the users choice is a he can add a task to a user with a description and a due date and tell if it is completed or not
def add_task():
    task_ds = 0     # Saves task_ds as 0
    name  = input ("Enter the username to who the task is assigned: ")
    descr = input ("Give a description of the task: ")
    due   = input ("What is the due date of the task? ")
    compl = input ("Is it completed Yes or No? ")
    today = input ("What is the current date? ")

    with open ('tasks.txt','a') as file:            # Saves the users input in a file
        file.write (name + ", " + descr + ", " + due + ", " + today + ", " + compl + "\n") # in the file it would be saved as the imput given name, discr, due, today, compl
        task_ds += 1    # If as task is added one is counted by task_ds

# If the users choice is va all the tasks would be readable
def view_all():                 
    tasks = open('tasks.txt','r+')  # Opens the right file
    for line in tasks:
    # Splits and strips the content so that it is recognizable for the system  
        temp = line.strip()         
        temp = temp.split(", ")
    # Prints the content that I manipulized to print readable 
        print ("Username   : ", temp[0])
        print ("Description: ", temp[1])
        print ("Due date   : ", temp[2])
        print ("Date       : ", temp[3])
        print ("Complete   : ", temp[4])
            
    tasks.close()                   # Closes the file again
            
            
# If the users choice is vm the user which is logged in wil see his own tasks
def view_my():
    num = ""
    tasks = open ('tasks.txt','r') 
    for line in tasks:
        if username in line:            # Checks if the username that is signed in is in the folder and if they have tasks
                
            temp = line.strip()         # Splits and strips the content so that it is recognizable 
            temp = temp.split(", ")
               
                # Prints the users tasks
            print ("Username   : ", temp[0])
            print ("Description: ", temp[1])
            print ("Due date   : ", temp[2])
            print ("Date       : ", temp[3])
            print ("Complete   : ", temp[4])                
        elif username not in line:  
            print("There is no tasks assigned to you") # If the username cant be found there is no tasks assigned to him
            
        if num == -1:
            print ("Please select on of the following options: ")
            print ("r  -  register user")
            print ("a  -  add task") 
            print ("va -  view all tasks")
            print ("vm -  view my tasks")
            print ("gr -  generate reports")
            print ("ds -  display statistics")
            print ("e  -  exit")
            print ("\n")
            choice = input ("")

                
    tasks.close()

# If the users choice is e the program exits
def exit():       
    sys.close()

# If the user chooses ds the amount of tasks and users is being displayed
def display(): 
    print ("Total amount of users is " + str (user_ds))
    print ("Total amount of tasks is " + str (task_ds))


def total_tasks():
    with open ('tasks.txt','r+') as file:
        content = file.read()
        CoList  = content.split("\n")
        num     = 1
        for line in CoList:
            while username in line:
                num += 1
                break
        with open ('user_overview.txt','a') as file:
            file.write (str(num) + "\n")
        with open ('user_overview.txt','r') as file:
            for line in file:
                print (line)
    
def all_tasks():
    with open ('tasks.txt','r+') as file:
        num = 1
        content = file.read()
        CoList  = content.split("\n")
        for i in CoList:
            if i:
               num += 1
        with open ('task_overview.txt', 'a') as file:
            file.write (str(num) + "\n")
        with open ('task_overview.txt','r') as file:
            for line in file:
                print (line)
    
def all_completed():
    with open ('tasks.txt','r+') as file:
        temp = file.read()
        temp = temp.strip()        
        temp = temp.split(", ")
        num  = 0
        for line in temp:
            while temp[4] == "Yes":
                num += 1
                break
        with open ('task_overview.txt', 'a') as file:
            file.write (str(num) + "\n")
        with open ('task_overview.txt','r') as file:
            for line in file:
                print (line)

def all_non_completed():
    with open ('tasks.txt','r+') as file:
        temp = file.read()
        temp = temp.strip()        
        temp = temp.split(", ")
        num  = 0
        for line in temp:
            while temp[4] == "No":
                num += 1
                break
        with open ('task_overview.txt', 'a') as file:
            file.write (str(num) + "\n")
        with open ('task_overview.txt','r') as file:
            for line in file:
                print (line)
# If the user is reconized the menu is shown with choices of what the user can choose
if logged_in == True:
    print ("\n")
    print ("Please select one of the following options: ")
    print ("r  -  register user")
    print ("a  -  add task") 
    print ("va -  view all tasks")
    print ("vm -  view my tasks")
    print ("gr -  generate reports")
    print ("ds -  display statistics")
    print ("e  -  exit")
    print ("\n")
    choice = input ("") # Users choice is being saved as a variable called choice to be used

    if choice == "r":
        print(register())
    
    if choice == "a":
        print (add_task())

    if choice == "va":
        print (view_all())

    if choice == "vm":
        print (view_my())

    if choice == "e":
        print (exit())

    if choice == "ds":
        print (display())

    if choice =="gr":
        print ("Users tasks: ", total_tasks())
        print ("All Tasks: ", all_tasks())
        print ("All Completed tasks: ", all_completed())
        print ("All non Completed tasks: ", all_non_completed())