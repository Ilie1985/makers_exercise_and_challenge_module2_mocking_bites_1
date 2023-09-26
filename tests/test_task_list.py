# from lib.task_list import TaskList


# def test_task_list_initially_empty():
#     task_list = TaskList()
#     assert task_list.tasks == []


# def test_tasks_initially_not_all_complete():
#     task_list = TaskList()
#     assert task_list.all_complete() == False

# Unit test `#tasks` and `#all_complete` behaviour

from lib.task_list import TaskList
from unittest.mock import Mock

def test_adds_tasks_to_list():
    task_list = TaskList()
    task_1 = Mock()  # Create a mock Task object
    task_2 = Mock()  # Create another mock Task object
    task_list.add(task_1)
    task_list.add(task_2)
    assert task_list.tasks == [task_1, task_2]

def test_marks_tasks_as_complete():
    task_list = TaskList()
    task_1 = Mock()
    task_2 = Mock()
    task_list.add(task_1)
    task_list.add(task_2)
    
    # Mock the mark_complete method for both tasks
    task_1.mark_complete.return_value = True
    task_2.mark_complete.return_value = True
    
    task_1.mark_complete()
    task_2.mark_complete()
    
    # Mock the is_complete method to return True for both tasks
    task_1.is_complete.return_value = True
    task_2.is_complete.return_value = True

    assert task_list.all_complete() == True
