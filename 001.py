import PySimpleGUI as sg
import random
import string

def generate_password():
    char = string.ascii_letters + string.digits + string.punctuation
    password = "".join(random.choice(char) for _ in range(random.randint(12,20)))
    return password

btn_create = sg.Button("New")
input_text = sg.InputText(default_text=generate_password(), key="password")
layout = [
    [ btn_create ], 
    [ input_text ]
]

print(input_text.DefaultText)
window = sg.Window("Password Manager", layout=layout)


while True:
    event, values =  window.read()
    if event == sg.WINDOW_CLOSED:
        print("Bye")
        break
    else:
        print(values)
        new_password =  generate_password()
        window["password"].update(new_password)
        

window.close()