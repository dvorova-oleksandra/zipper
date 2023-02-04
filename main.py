import PySimpleGUI as gui

#Creating Graphic User Interface elements
label_for_files = gui.Text("Select files for to zip:")
input_files = gui.Input()
choose_button_for_files = gui.FilesBrowse("Choose", key='file')
label_for_folder= gui.Text("Select folder for saving zip:")
input_folder = gui.Input()
choose_button_for_folder = gui.FolderBrowse("Choose", key='folder')
work_button = gui.Button("Zip")
exit_button = gui.Button("Exit")

#Create window and adding GUI
window = gui.Window("Zip", layout=[[label_for_files, input_files, choose_button_for_files],
                                   [label_for_folder, input_folder, choose_button_for_folder],
                                   [work_button, exit_button]])
#Functionality
while True:
    event, value = window.read()
    filepath = value["file"].split(";")
    folder = value["folder"]
    print(filepath, folder)
#action
    match event:
#exit
        case gui.WIN_CLOSED | 'Exit':
            break





window.close()