from lib.task_list import TaskList
from unittest.mock import Mock

def test_task_list_initially_empty():
    task_list = TaskList()
    assert task_list.tasks == []


def test_tasks_initially_not_all_complete():
    task_list = TaskList()
    assert task_list.all_complete() == False

# Unit test `#tasks` and `#all_complete` behaviour hhh

def test_add_tasks_to_task_list():
    task_list = TaskList()
    task1 = Mock()
    task2 = Mock()
    task_list.add(task1)
    task_list.add(task2)
    assert task_list.tasks == [task1, task2]

def test_all_returns_all_tasks():
    task_list = TaskList()
    task1 = Mock()
    task2 = Mock()
    task_list.add(task1)
    task_list.add(task2)
    assert task_list.all() == [task1, task2]

def test_all_complete_when_all_tasks_complete():
    task_list = TaskList()
    task1 = Mock()
    task2 = Mock()
    task_list.add(task1)
    task_list.add(task2)
    task1.is_complete.return_value = True
    task2.is_complete.return_value = True
    assert task_list.all_complete() == True


def test_all_complete_when_not_all_the_tasks_are_complete():
    task_list = TaskList()
    task1 = Mock()
    task2 = Mock()
    task_list.add(task1)
    task_list.add(task2)
    task1.is_complete.return_value = True
    task2.is_complete.return_value = False
    assert task_list.all_complete() == False
    