from pathlib import Path
import os


def createfile():
    try:
        name=input("plz tell your file name:")
        path=Path(name)
        if not path.exists():
            with open(path,"w") as fs:
                data=input("what you want to write:")
                fs.write(data)
            print("file created successfully")
            # print("Saved at:", path.resolve())    
        else:
            print("Error file name already exists")    
    except Exception as err:
        print(f"An error occured as:{err}")


def readfile():
    try:
        name=input("plz tell yuor file name-:")
        path=Path(name)
        if path.exists():
            with open(path,"r") as fs:
                content=fs.read()
                print(f"your file content is:\n{content}")
        else:
            print("Error no such file exist")
    except Exception as err:
        print(f"An error occured as:{err}")


def updatefile():
    try:
        name=input("plz tell your file name-:")
        path=Path(name)
        if path.exists():
            print("operations")
            print("1. renaming the file")
            print("2. appending the content")
            print("3. overwriting the file")
            choise=int(input("enter a opperation want to perform on a file-:"))

            if choise==1:
                newname=input("enetr your new file name-:")
                new_path=Path(newname)
                if not new_path.exists():
                    path.rename(new_path)
                    print("rename successfully")
                else:
                    print("file already exists")    
            elif choise==2:
                    with open (path,"a") as fs:
                        data=input("enetr a data you want to append-:")
                        fs.write(f"\n{data}")
                    print("file appended successfuly")
            elif choise==3:
                    with open (path,"w") as fs:
                        data=input("enetr a data you want to overwrite-:")
                        fs.write(f"\n{data}")
                    print("file overwrite successfuly")

    except Exception as err:
        print(f"An error occured as:{err}")


def deletefile():
    try:
        name=input("plz tell your file name-:")
        path=Path(name)
        if path.exist():
            path.unlink()
            print("file is successfully deleted")
        else:
            print("Error file does't exists")
    except Exception as err:
        print(f"An error occured as:{err}")


print("choose 1 for creating a file")
print("choose 2 for reading a file")
print("choose 3 for updating a file")
print("choose 4 for deleting a file")


a=int(input("\n enter your response -:"))

if a==1:
    createfile()

elif a==2:
    readfile()

elif a==3:
    updatefile()

elif a==4:
    deletefile()

