import os


def Renamer(Directory, Name):
    Files = []
    os.chdir(Directory)
    for file in os.listdir():
        if file.endswith(".ipt") or file.endswith(".iam"):
            Files.append(file)
    Directory += "\\"

    for file in Files:
        if file.endswith(".ipt"):
            file = file[:len(file) - 4]
            os.rename(Directory + file + ".ipt",Directory + file + "-" + Name + ".ipt")

        elif file.endswith(".iam"):
            file = file[:len(file) - 4]
            os.rename(Directory + file + ".iam", + file + "-" + Name + ".iam")


option = input("What Directory do you want to change")

Name: str = input("What is your name")

Renamer(option, Name)
