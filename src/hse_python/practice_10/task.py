import enum

from hse_python.utils.errors import WrongTaskStatusError, WrongSubtaskError


class TaskStatus(enum.Enum):
    OPEN = 1
    IN_WORKING = 2
    DONE = 3


class Task:
    def __init__(self, id: int = None, name: str = "", description: str = ""):
        self.id = id
        self.name = name
        self.description = description
        self.status = TaskStatus.OPEN

    def mark_in_working(self):
        if self.status == TaskStatus.OPEN:
            self.status = TaskStatus.IN_WORKING
        else:
            raise WrongTaskStatusError()

    def mark_done(self):
        if self.status == TaskStatus.IN_WORKING:
            self.status = TaskStatus.DONE
        else:
            raise WrongTaskStatusError()


class Subtask(Task):
    def __init__(self, parent_id: int = None, id: int = None, name: str = "", description: str = ""):
        super().__init__(id, name, description)
        self.parent_id = parent_id


class ComplexTask(Task):
    def __init__(self, id: int = None, name: str = "", description: str = "", subtasks=None):
        super().__init__(id, name, description)
        self.subtasks = subtasks or []

    def add_subtask(self, subtask: Subtask):
        if subtask.parent_id != self.id:
            raise WrongSubtaskError(f"Subtask has incorrect parent id: {self.id} != {subtask.parent_id}")
        self.subtasks.append(subtask)

    def mark_in_working(self):
        super().mark_in_working()
        for subtask in self.subtasks:
            subtask.mark_in_working()

    def mark_done(self):
        super().mark_done()
        for subtask in self.subtasks:
            subtask.mark_done()
