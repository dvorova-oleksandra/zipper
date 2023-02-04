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
output_label = gui.Text(key="change")

#Create window and adding GUI
window = gui.Window("Zip", layout=[[label_for_files, input_files, choose_button_for_files],
                                   [label_for_folder, input_folder, choose_button_for_folder],
                                   [label_for_name, input_text],
                                   [work_button, exit_button, output_label]])
#Functionality
while True:
    event, value = window.read()
    filepath = value["file"].split(";")
    folder = value["folder"]
    name = value['name']
#action
    match event:
        case "Zip":
            try:
                 make_zip(filepath, folder, name)
                 window['change'].update(value="Zip is done!")
            except FileNotFoundError:
                window['change'].update(value="Wrong input. Check input isn't empty")
                continue
#exit
        case gui.WIN_CLOSED | 'Exit':
            break





window.close()