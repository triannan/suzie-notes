#!/usr/bin/env python3
import os
from time import sleep
import pickle
import pyfiglet
from colorama import Fore, Back, Style

os.system('clear')
print(Fore.CYAN)
hello = pyfiglet.figlet_format("welcome to suzie!!!!!", font = "big")
print(hello)
print(Style.RESET_ALL)
sleep(1)
os.system('clear')
def loadIn():
    try:
        file = open('noteNames.pkl', 'rb')
        noteNames = pickle.load(file)
        file.close()
        return noteNames
    except:
        noteNames = []
        return noteNames

def loadTask():
    try:
        file = open('taskNames.pkl', 'rb')
        taskList = pickle.load(file)
        file.close()
        return taskList
    except:
        taskList = []
        return taskList

def title():
    print(Fore.MAGENTA)
    welcome = pyfiglet.figlet_format("greetings friend!", font = "slant")
    print(welcome)
    print(Style.RESET_ALL)

def choice1():
    os.system('clear')
    print(Fore.MAGENTA)
    notetitle = pyfiglet.figlet_format("create / delete", font = "bulbhead")
    print(notetitle)
    print(Style.RESET_ALL)
    noteChoice = input("type 'del' to delete a note\ntype 'new' to create a new note\n(type '0' to go back)\n")
    if noteChoice == 'new':
        noteName = input("\nwhat would you like to name your note? (type '0' to go back)\n")
        if noteName == '0':
            os.system('clear')
            return
        if (noteName in noteNames):
            print("\nthat name is already taken, please choose another one")
            choice1()
        else:
            noteNames.append(noteName)
            os.system('clear')
            os.system('vim '+  noteName + '.txt')
    elif noteChoice == 'del':
        os.system('clear')
        i = 1
        print("[0] back")
        for name in noteNames:
            num = str(i)
            print("["+ num + "] "+ name)
            i = i+1
        delNote = input("which note would you like to delete? (number)\n")
        if (int(delNote) <= len(noteNames)) and (int(delNote) > 0):
            os.system('rm ' + noteNames[int(delNote) - 1] +'.txt')
            noteNames.remove(noteNames[int(delNote) - 1])
            os.system('clear')
            choice1()
        elif delNote == '0':
            os.system('clear')
            return
        else:
            print("that is not a valid number")
            os.system('clear')
            choice1()
    elif noteChoice == '0':
        os.system('clear')
        return
    else:
        choice1()
    

def choice2():
    os.system('clear')
    print(Fore.MAGENTA)
    notetitle = pyfiglet.figlet_format("notes list", font = "bulbhead")
    print(notetitle)
    print(Style.RESET_ALL)
    i = 1
    print("[0] back")
    for name in noteNames:
        num = str(i)
        print("["+ num + "] "+ name)
        i = i+1
    openNote = input("\nwhich notes would you like to edit?\n")
    if (openNote.isnumeric()) and (int(openNote) <= len(noteNames)):
        numm = int(openNote)
        if numm == 0:
            os.system('clear')
            return
        else:
            os.system('clear')
            os.system('vim '+ noteNames[numm - 1]+ ".txt")
    else:
        print("please enter a valid number")
        choice2()

def choice3():
    os.system('clear')
    print(Fore.MAGENTA)
    todolist = pyfiglet.figlet_format("to-do list :)", font = "bulbhead")
    print(todolist)
    print(Style.RESET_ALL)
    print("[0] back")
    num = 1
    for task in taskList:
        print("["+ str(num) + "] "+ task)
        num = num+1
    task = input("\ntype 'new' to create a new task\ntype 'del' to delete a task\n")
    if task == 'new':
        taskname = input("\nwhat would you like to name your task? (type '0' to go back)\n")
        if taskname in taskList:
            print("that task is already on the list")
            os.system('clear')
            choice3()
        else:
            taskList.append(taskname)
            choice3()
        if taskname == '0':
            os.system('clear')
            return
    elif task == 'del':
        deltask = input("which task would you like to delete? (number)\n")
        if (int(deltask) <= len(taskList)) and (int(deltask) > 0):
            taskList.remove(taskList[int(deltask) - 1])
            choice3()
        else:
            print("that is not a valid number")
            os.system('clear')
            choice3()
    elif task.isnumeric():
        if task == '0':
            os.system('clear')
            return
    else:
        os.system('clear')
        choice3()



def choice4():
    try:
        file = open('noteNames.pkl', 'wb')
        pickle.dump(noteNames, file)
        file.close()
        print("saving the following notes:")
        for name in noteNames:
            print(name)
    except Exception as e:
        print(e)
        print("\nerror, i can't save")

    try:
        file = open('taskNames.pkl', 'wb')
        pickle.dump(taskList, file)
        file.close()
        print("saving the following tasks:")
        for task in taskList:
            print(task)
    except Exception as e:
        print(e)
        print("\nerror, i can't save")
    

noteNames = loadIn()
taskList = loadTask()
#main program
choice = ''
while choice != '4':
    title()
    choice = input("\nwould you like to:\n[1] create a new note / delete a note\n[2] edit an existing note\n[3] to-do list\n[4] quit\n")

    if choice == '1':
        choice1()

    elif choice == '2':
        choice2()
    
    elif choice == '3':
        choice3()

    elif choice == '4':
        choice4()
        os.system('clear')
        quit()
    else:
        print("\nplease enter a valid number")
        os.system('clear')