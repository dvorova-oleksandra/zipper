import PySimpleGUI as gui
from zip import make_zip

#Creating Graphic User Interface elements
label_for_files = gui.Text("Select files for to zip:")
input_files = gui.Input()
choose_button_for_files = gui.FilesBrowse("Choose", key='file')
label_for_folder= gui.Text("Select folder for saving zip:")
input_folder = gui.Input()
choose_button_for_folder = gui.FolderBrowse("Choose", key='folder')
label_for_name = gui.Text("Enter name for zip file")
input_text = gui.Input( key="name")
work_button = gui.Button("Zip")
exit_button = gui.Button("Exit")

#Create window and adding GUI
window = gui.Window("Zip", layout=[[label_for_files, input_files, choose_button_for_files],
                                   [label_for_folder, input_folder, choose_button_for_folder],
                                   [label_for_name, input_text],
                                   [work_button, exit_button]])
#Functionality
while True:
    event, value = window.read()
    filepath = value["file"].split(";")
    folder = value["folder"]
    name = value['name']
#action
    match event:
        case "Zip":
            make_zip(filepath, folder, name)
#exit
        case gui.WIN_CLOSED | 'Exit':
            break





window.close()