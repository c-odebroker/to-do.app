import FreeSimpleGUI as sg

import functions


label = sg.Text("Type in a to-do")
input_box = sg.InputText(tooltip="Enter todo", key='todo', )
list_box = sg.Listbox(values=functions.get_todos(), key='todos',
                      enable_events=True, size=(45,10))

add_button = sg.Button("ADD")
edit_button = sg.Button("Edit")
complete_button = sg.Button("Complete")
exit_button = sg.Button("Exit")
strikethrough_button = sg.Button("Strike")

window = sg.Window('My To-Do App',
                   layout=[[label],
                           [input_box, add_button],
                           [list_box, edit_button, complete_button, strikethrough_button],
                           [exit_button]],
                   font=('Helvetica', 20))
while True:
    event, values = window.read()
    print(1, event)
    print(2, values['todo'])
    print(3, values['todos'])
    match event:
        case "ADD":
            todos = functions.get_todos()
            new_todo = values['todo'] + "\n"
            todos.append(new_todo)
            functions.write_todos(todos)
            window['todos'].update(values=todos)
            window['todo'].update(value='')

        case "Edit":
            todo_to_edit = values['todos'][0]
            new_todo = values['todo']

            todos= functions.get_todos()
            index = todos.index(todo_to_edit)
            todos[index] = new_todo
            functions.write_todos(todos)
            window['todos'].update(values=todos)

        #case "Strike":
        #    todo_to_markoff = values['todos'][0]
        #
        #    todos = functions.get_todos()
        #    index = todos.index(todo_to_markoff)
        #    todos[index] = functions.strike(todo_to_markoff)
        #    functions.write_todos(todos)
        #
        #    window['todos'].update(values=todos)
        #    window['todo'].update(value='')

        case "Complete":
            todo_to_complete = values['todos'][0]
            todos = functions.get_todos()
            todos.remove(todo_to_complete)
            functions.write_todos(todos)
            window['todos'].update(values=todos)
            window['todo'].update(value='')

        case "Exit":
            break

        case 'todos':
            window['todo'].update(value=values['todos'][0])


        case sg.WIN_CLOSED:
            break


window.close()