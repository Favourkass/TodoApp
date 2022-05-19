import argparse
import datetime
import os

def getdate():
    return datetime.datetime.now().strftime("%Y-%m-%d")

z=getdate()

Total=0

class CreateTodoList(object):
    x=os.getcwd()
    FILE_LOCATION = fr"{x}\todo.txt"
    Done_Location= fr"{x}/done.txt"
    
    def __init__(self):
        self.items = open(self.FILE_LOCATION, "r").readlines()
        self.done_items = open(self.Done_Location, "r").readlines()


    def add_todo(self):
        todo = input("Enter a todo: ")
        with open(self.FILE_LOCATION, "a+") as f:
            f.writelines(f" {todo} {z}\n")
        print("Added item: " + todo)

    def remove_todo(self):
        todo_index_to_remove = int(input("Enter the index of the todo you want to remove: "))

        try:
            doneTask = self.items.pop(todo_index_to_remove - 1)

            print("Completed task no. " +
                str(todo_index_to_remove) +
                " (%s), deleted todo" % doneTask.strip()
            )
            print(f"Deleted item:{doneTask}")

            with open(self.FILE_LOCATION, "w") as f:
                for item in self.items:
                    f.writelines(item)
        except Exception as e:
            print(f"Error: todo {todo_index_to_remove} does not exist. Nothing deleted.")
    
    def edit_todo(self):
        todo_index_to_edit = int(input("Enter the index of the todo you want to edit: "))
        try:
            edit_to_do = input("Enter the new todo: ")
            save_new_todo = self.items[todo_index_to_edit - 1] = edit_to_do
            print(f"Edited item:{save_new_todo}")
            with open(self.FILE_LOCATION, "w") as f:
                for item in self.items:
                    f.writelines(item)
        except Exception as e:
            print(f"Error: todo {todo_index_to_edit} does not exist. Nothing deleted.")

    def show_todo(self):
        if not self.items:
            print("No tasks to be done.\n")
        else:
            for serialno, item in enumerate(self.items):
                print(str(serialno+1) + ". " + item)

    

    def mark_todo_done(self):
        todo_index_to_mark = int(input("Enter the index of the todo you want to mark as done: "))
        try:
            doneTask = self.items.pop(todo_index_to_mark - 1)
            
            print(f"Completed item:{doneTask}")
            with open(self.FILE_LOCATION, "w") as f:
                for item in self.items:
                    f.writelines(item)
            with open(self.Done_Location, "a+") as f:
                f.writelines(f"{doneTask}")

        except Exception as e:
            print(f"Error: todo {todo_index_to_mark} does not exist. Nothing deleted.")
        
    def load_done(self):
        if not self.done_items:
            print("No tasks completed.\n")
        else:
            for serialno, item in enumerate(self.done_items):
                print(str(serialno+1) + ". " + item)

    def report_for_day(self):
        counter =0
        for item in self.done_items:
            counter +=1
            print(f"{counter} {item}")
        print(f"Total completed tasks: {counter}")
        print(f"Total tasks Left: {len(self.items)}")

    def reset_files(self):
        with open(self.FILE_LOCATION, 'w') as f:
            f.write('')
        with open(self.Done_Location, 'w') as f:
            f.write('')

        print("Todo Lists reset.")

    def show_menu(self):
        print("""
        1. --add: Add a todo
        2. --remove: Remove a todo
        3. --show: Show todos
        4. --mark: Mark a todo as done
        5. --show_done: Show done
        6. --reset: Reset files
        7. --report: Report for day
        8. --edit: Edit a todo
        """)
    

if __name__ == "__main__":

    description = "Todo, for when you need to do."

    parser = argparse.ArgumentParser(description = description)

    parser.add_argument("--add", action = "store_true", help = "Add a todo")
    parser.add_argument("--remove", action = "store_true", help = "Remove a todo")
    parser.add_argument("--show", action = "store_true", help = "Show todos")
    parser.add_argument("--mark", action = "store_true", help = "Mark a todo as done")
    parser.add_argument("--show_done", action = "store_true", help = "Show done")
    parser.add_argument("--reset", action = "store_true", help = "Reset files")
    parser.add_argument("--report", action = "store_true", help = "Report for day")
    parser.add_argument("--edit", action = "store_true", help = "Edit a todo")


    args = parser.parse_args()

    todo = CreateTodoList()

    if args.add:
        todo.add_todo()
    elif args.remove:
        todo.remove_todo()
    elif args.show:
        todo.show_todo()
    elif args.mark:
        todo.mark_todo_done()
    elif args.show_done:
        todo.load_done()
    elif args.reset:
        todo.reset_files()
    elif args.report:
        todo.report_for_day()
    elif args.edit:
        todo.edit_todo()

    else:
        todo.show_menu()


