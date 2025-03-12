import functions
import FreeSimpleGUI

label = FreeSimpleGUI.Text("Type in a to-do")
input_box = FreeSimpleGUI.InputText(tooltip="Enter todo",key = "Todo")
add_button = FreeSimpleGUI.Button("Add")
list_box = FreeSimpleGUI.Listbox(values=functions.get_todos("todos.txt"),key='todos',
                                enable_events=True,size=[45,10])
edit_button = FreeSimpleGUI.Button("Edit")

window = FreeSimpleGUI.Window('My To-Do App',layout = [[label],[input_box,add_button],[list_box,edit_button]],
                              font=('Helvetica',20))

while True:
   event,values = window.read()  # The window.read() gives a tuple in response which have event as button and values is dictionary
   print(event)
   print(values)
   match event:
       case "Add":
           todos = functions.get_todos("todos.txt")
           todos.append(values['Todo']+'\n')
           functions.write_todos(todos,"todos.txt")
           window['todos'].update(values=todos)

       case "Edit":
           todo_to_edit = values['todos'][0]
           new_todo = values['Todo']+'\n'
           todos = functions.get_todos("todos.txt")
           index = todos.index(todo_to_edit)
           todos[index] = new_todo
           functions.write_todos(todos,"todos.txt")
           window['todos'].update(values = todos)
       case 'todos':
           window['Todo'].update(value = values['todos'][0])
       case FreeSimpleGUI.WIN_CLOSED:
           break
window.close()

