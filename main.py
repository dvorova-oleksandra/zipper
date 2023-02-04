import PySimpleGUI as gui

label_for_files = gui.Text("Select files for to zip:")
input_files = gui.Input()
choose_button_for_files = gui.FilesBrowse("Choose")

label_for_folder= gui.Text("Select folder for saving zip:")
input_folder = gui.Input()
choose_button_for_folder = gui.FolderBrowse("Choose")

work_button = gui.Button("Zip")

window = gui.Window("Zip", layout=[[label_for_files, input_files, choose_button_for_files],
                                   [label_for_folder, input_folder, choose_button_for_folder],
                                   [work_button]])

while True:
    event, value = window.read()
    
window.close()