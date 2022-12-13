import unittest
from hse_python.practice_10 import *


class TaskManagerTestCase(unittest.TestCase):
    def test_get_all(self):
        task_manager = TaskManager()
        task1 = Task(name="name", description="description")
        task2 = ComplexTask(name="name", description="description")
        task_manager.create_task(task1)
        task_manager.create_complex_task(task2)
        self.assertEqual(task_manager.get_tasks(), [task1])
        self.assertEqual(task_manager.get_subtasks(), [])
        self.assertEqual(task_manager.get_complex_tasks(), [task2])

    def test_get_by_id(self):
        task_manager = TaskManager()
        task1 = Task(name="name1", description="description1")
        task2 = Task(name="name2", description="description2")
        task_manager.create_task(task1)
        task_manager.create_task(task2)
        self.assertEqual(task_manager.get_tasks_by_id(-1), None)
        self.assertEqual(task_manager.get_tasks_by_id(task1.id), task1)
        self.assertEqual(task_manager.get_tasks_by_id(task2.id), task2)

    def test_remove_all(self):
        task_manager = TaskManager()
        task1 = Task(name="name1", description="description1")
        task2 = Task(name="name2", description="description2")
        task_manager.create_task(task1)
        task_manager.create_task(task2)
        task_manager.remove_tasks()
        self.assertEqual(task_manager.get_tasks(), [])

    def test_remove_by_id(self):
        task_manager = TaskManager()
        task1 = Task(name="name1", description="description1")
        task2 = Task(name="name2", description="description2")
        task_manager.create_task(task1)
        task_manager.create_task(task2)
        task_manager.remove_task_by_id(task1.id)
        self.assertEqual(task_manager.get_tasks(), [task2])
        task_manager.remove_task_by_id(task2.id)
        self.assertEqual(task_manager.get_tasks(), [])

    def test_update_status(self):
        task_manager = TaskManager()
        task1 = Task(name="name1", description="description1")
        task2 = Task(name="name2", description="description2")
        task_manager.create_task(task1)
        task_manager.create_task(task2)
        task1.mark_in_working()
        task2.mark_in_working()
        task2.mark_done()
        self.assertEqual(task_manager.get_tasks_by_id(task1.id).status, TaskStatus.IN_WORKING)
        self.assertEqual(task_manager.get_tasks_by_id(task2.id).status, TaskStatus.DONE)

    def test_complex_tasks(self):
        task_manager = TaskManager()
        task0 = ComplexTask(name="name0", description="description0")
        task_manager.create_complex_task(task0)
        task1 = Subtask(parent_id=task0.id, name="name1", description="description1")
        task2 = Subtask(parent_id=task0.id, name="name2", description="description2")
        task_manager.create_subtask(task1)
        task_manager.create_subtask(task2)
        task0.add_subtask(task1)
        task0.add_subtask(task2)
        task0.mark_in_working()
        task0.mark_done()
        self.assertEqual(task_manager.get_complex_tasks_by_id(task0.id).status, TaskStatus.DONE)
        self.assertEqual(task_manager.get_subtasks_by_id(task1.id).status, TaskStatus.DONE)
        self.assertEqual(task_manager.get_subtasks_by_id(task2.id).status, TaskStatus.DONE)


if __name__ == '__main__':
    unittest.main()
