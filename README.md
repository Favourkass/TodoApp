This is a todo program used to remind and store our tasks to be done in future

Recommendation:- Download Python-3 in system and add path to our computer system

This program mainly run in command prompt or powershell window

Step to run this program:-

1.first open powershell window/command prompt window in main program directory by clicking shift+right mouse button and then click on open powershell window/Command Prompt window in dropdown menu
2.Than this has to be ensured that path location should be "D:\algorithm Testing" so that it can easily find the path of the created files for storing the data.

the codes for testing are given below:

```
 $python .\todo.py --show            #To list all todo items
 $python .\todo.py --add           #To add new item in todo list
 $python .\todo.py --remove        #To remove already existed item
 $python .\todo.py --mark         #To update the information that respective activity is done and also remove it from todo todolist
 $python .\todo.py --report        #To report the final progress of todo list
 $python .\todo.py --show_done       #To show all done todo task
$python .\todo.py --edit     #To edit the todo task
$python .\todo.py --reset   #To reset all todo files and clear all the data

 ```