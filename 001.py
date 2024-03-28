import PySimpleGUI as sg

label = sg.Text("")

window = sg.Window("Password Manager", layout=[[label]])
window.read()