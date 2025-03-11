# from functions import get_todos,write_todos
import functions
import time
print(time.strftime("%b %d, %Y %H:%M:%S"))


while True:
    user_choice = input("Enter one of the options between add,show,edit,complete or exit ")

    if user_choice.startswith("add"):
       user_input = user_choice[4:] +"\n"
       # file = open('todos.txt','r')
       # todos = file.readlines()
       # file.close()
       file = "todos.txt"
       todos = functions.get_todos(file = "todos.txt")
       todos.append(user_input)

       # file = open('todos.tx t','w')
       # file.writelines(todos)
       # file.close()
       functions.write_todos(todos,file)

    elif user_choice.startswith("show"):
        file = "todos.txt"
        todos = functions.get_todos(file)
        # new_todos = []
        # for item in todos:
        #     new_item = item.strip('\n')
        #     new_todos.append(new_item)

        new_todos = [item.strip('\n') for item in todos]

        for j,i in enumerate(new_todos):
            print(f"{j+1}.{i}")

    elif user_choice.startswith("edit"):
       try:
           num = int(user_choice[5:])
           num = num - 1
           new_task = input("Enter the new task ")
           file = "todos.txt"
           todos = functions.get_todos(file)
           todos[num] = new_task+'\n'
           functions.write_todos(todos,file )
       except ValueError:
           print("Enter a proper command")

    elif user_choice.startswith("complete"):
      try:
        num = int(user_choice[9:])
        num = num - 1
        file = "todos.txt"
        todos = functions.get_todos(file)
        todos.pop(num)
        functions.write_todos(todos,file)
      except ValueError:
          print("Enter the proper command")
      except IndexError:
          print("Enter the index within the given range")

    elif "exit" in user_choice:
        break
