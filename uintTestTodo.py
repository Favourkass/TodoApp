from .todo import CreateTodoList
import unittest



class UnitTestCreateTodoList(unittest.TestCase):

    def test_add_todo(self):
        todo = CreateTodoList()
        todo.add_todo()
        self.assertEqual(len(todo.items), 1)


class UnitTestReadTodoList(unittest.TestCase):

    def test_read_todo(self):
        todo = CreateTodoList()
        todo.show_todo()
        self.assertEqual(len(todo.items), 1)

class UnitTestRemoveTodoList(unittest.TestCase):

    def test_remove_todo(self):
        todo = CreateTodoList()
        todo.remove_todo()
        self.assertEqual(len(todo.items), 0)

class UnitTestMarkTodoList(unittest.TestCase):

    def test_mark_todo(self):
        todo = CreateTodoList()
        todo.mark_todo_done()
        self.assertEqual(len(todo.done_items), 1)

