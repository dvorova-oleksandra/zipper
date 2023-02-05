import zipfile
import pathlib

#checking that name for zip file
def zip_name(name):
    file = "zip"
    checking = []
    checking.append(not("/" in name))
    checking.append(not(":" in name))
    checking.append(not("*" in name))
    checking.append(not("?" in name))
    checking.append(not('"' in name))
    checking.append(not("<" in name))
    checking.append(not(">" in name))
    checking.append(not ("|" in name))
    if all(checking) == True:
        file = name
    return file

#create path(path for creating zip file)
def create_path(dir, name):
    file = name+".zip"
    dir = pathlib.Path(dir, file)
    return dir

#create a zip with choosen files
def make_zip(filepath, directory, name):
    with zipfile.ZipFile(create_path(directory, name), 'w') as archive:
        for file in filepath:
            archive.write(file)

