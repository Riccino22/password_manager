import PySimpleGUI as sg
import random
import string
import read_csv

def generate_password():
    char = string.ascii_letters + string.digits + string.punctuation.replace(",","")
    password = "".join(random.choice(char) for _ in range(random.randint(12,20)))
    return password

btn_create = sg.Button("New")
btn_add = sg.Button("Add")
btn_generate = sg.Button("Generate")
name_site = sg.InputText(key="name")
url_site = sg.InputText(key="url")
password = sg.InputText(key="password")

layout = [
    [ sg.Text("Name: ") ],
    [ name_site ],
    [ sg.Text("Url: ") ],
    [ url_site ],
    [ sg.Text("Password: ") ],
    [ password ],
    [ btn_create , btn_add , btn_generate ]
]

print(password.DefaultText)
window = sg.Window("Password Manager", layout=layout)


while True:
    event, values =  window.read()
    match event:

        case sg.WINDOW_CLOSED:
            break

        case "New":
            window["name"].Update("")
            window["url"].Update("")
            window["password"].Update("")

        case "Generate":
            window["password"].Update(generate_password())

        case "Add":
            read_csv.data.append([values["name"], values["url"], values["password"]])
            print(read_csv.data)
            read_csv.write_on_csv(read_csv.data)
        

window.close()