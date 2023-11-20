from lib.task_list import TaskList
from lib.task import Task, TaskFormatter


def test_adds_tasks_to_list():
    task_list = TaskList()
    task_1 = Task("Walk the dog")
    task_2 = Task("Walk the cat")
    task_list.add(task_1)
    task_list.add(task_2)
    assert task_list.tasks == [task_1, task_2]

def test_all_complete_when_tasks_arent_complete():
    task_list = TaskList()
    task_1 = Task("Walk the dog")
    task_2 = Task("Walk the cat")
    task_list.add(task_1)
    task_list.add(task_2)
    assert task_list.all_complete() == False

def test_marks_tasks_as_complete():
    task_list = TaskList()
    task_1 = Task("Walk the dog")
    task_2 = Task("Walk the cat")
    task_list.add(task_1)
    task_list.add(task_2)
    task_1.mark_complete()
    task_2.mark_complete()
    assert task_list.all_complete() == True


def test_task_formatter_with_incomplete_task():
    task_1 = Task("Walk the dog")
    task_formatter = TaskFormatter(task_1)
    assert task_formatter.format() == "- [ ] Walk the dog"

def test_task_formatter_with_complete_task():
    task_1 = Task("Walk the dog")
    task_1.mark_complete()
    task_formatter = TaskFormatter(task_1)
    assert task_formatter.format() == "- [x] Walk the dog"


def test_task_format_with_multiple_tasks_in_task_list():
    task_list = TaskList()
    task_1 = Task("Walk the dog")
    task_2 = Task("Walk the cat")
    task_3 = Task("Feed the elephant")
    task_list.add(task_1)
    task_list.add(task_2)
    task_list.add(task_3)
    task_1.mark_complete()
    task_3.mark_complete()
    assert ([TaskFormatter(task).format() for task in task_list.all()]
            == ["- [x] Walk the dog",
                "- [ ] Walk the cat",
                "- [x] Feed the elephant"
                ]
            )
