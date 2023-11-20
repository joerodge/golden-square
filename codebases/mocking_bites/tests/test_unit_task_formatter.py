from lib.task import TaskFormatter
from unittest.mock import Mock

def test_create_task_formatter():
    test_task = Mock()
    task_formatter = TaskFormatter(test_task)
    assert task_formatter.task == test_task

def test_format_of_incomplete_task():
    test_task = Mock()
    task_formatter = TaskFormatter(test_task)
    test_task.title = 'Test Task'
    test_task.is_complete.return_value = False
    assert task_formatter.format() == '- [ ] Test Task'

def test_format_of_completed_task():
    test_task = Mock()
    task_formatter = TaskFormatter(test_task)
    test_task.title = 'Test Task'
    test_task.is_complete.return_value = True
    assert task_formatter.format() == '- [x] Test Task'


