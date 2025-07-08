import json as js
import os
import taskprinter as tp
from datetime import datetime
from enum import Enum


DB_NAME = "pydoto.json"


class TaskStatus(Enum):
    ACTIVE = "active"
    COMPLETED = "completed"
    EXPIRED = "expired"
    DELETED = "deleted"


class Task:
    def __init__(self, name="Default Task", description=None, expiration_date=None):
        self.name = name
        self.description = description
        self.creation_date = datetime.now()
        self.expiration_date = expiration_date
        self.status = TaskStatus.ACTIVE

    def to_dict(self) -> dict:
        """Class -> Dictionary; For future save into .json"""
        return {
            "name": self.name,
            "description": self.description,
            "status": self.status.value,
            "creation_date": self.creation_date.isoformat(),
            "expiration_date": self.expiration_date.isoformat()
            if self.expiration_date
            else None,
        }

    def db_append(self):
        """Append task to DB"""
        tasks = []
        tasks = Task.db_load()
        tasks.append(self)
        Task.db_dump(tasks)

    @classmethod
    def mark_done(cls, task_id):
        """Set task.status = COMPLETED"""
        tasks = cls.db_load()

        for task in tasks:
            if str(task.creation_date) == task_id:
                if task.status != TaskStatus.DELETED:
                    task.status = TaskStatus.COMPLETED
                    cls.db_dump(tasks)
                    return
                else:
                    raise ValueError("!> You can't complete deleted task")

        print("!> Incorrect task ID")

    @classmethod
    def mark_deleted(cls, task_id):
        """task.status = DELETED"""
        tasks = cls.db_load()

        for task in tasks:
            if str(task.creation_date) == task_id:
                task.status = TaskStatus.DELETED
                cls.db_dump(tasks)
                return

        print("!> Incorrect task ID")

    @classmethod
    def update_expiration_statuses(cls):
        """Load from .json -> Update exp. statuses -> Save to .json"""
        tasks = []
        tasks_new = []

        tasks = cls.db_load()

        for task in tasks:
            if (
                task.expiration_date
                and task.status == TaskStatus.ACTIVE
                and task.expiration_date < datetime.now()
            ):
                task.status = TaskStatus.EXPIRED

            tasks_new.append(task)

        cls.db_dump(tasks_new)

    @classmethod
    def from_dict(cls, data):
        """Convert ONE Dict -> Class"""
        expiration_date = (
            datetime.fromisoformat(data["expiration_date"])
            if data["expiration_date"]
            else None
        )
        task = cls(data["name"], data["description"], expiration_date)
        task.creation_date = datetime.fromisoformat(data["creation_date"])
        task.status = TaskStatus(data["status"])

        return task

    @classmethod
    def db_load(cls) -> list:
        """Load tasks from .json into list (AS CLASSES)"""
        if not os.path.exists(DB_NAME):
            print(
                f"!> File {DB_NAME} doesn't exist. Use -f flag to create DB or move existing."
            )
            exit(1)

        try:
            with open(DB_NAME, "r", encoding="utf-8") as f:
                tasks_data = js.load(f)
                if not isinstance(tasks_data, list):
                    tasks_data = [tasks_data]
                return [cls.from_dict(task_data) for task_data in tasks_data]
        except (js.JSONDecodeError, IOError) as e:
            print(f"!> Can't read {DB_NAME}: {e}")
            exit(1)

    @classmethod
    def db_dump(cls, data):
        """Save tasks from list -> .json"""
        data_dict = []

        for task in data:
            data_dict.append(cls.to_dict(task))

        if not os.path.exists(DB_NAME):
            print(f"!> File {DB_NAME} doesn't exist. Check --help menu.")
            exit(1)

        try:
            with open(DB_NAME, "w", encoding="utf-8") as f:
                js.dump(data_dict, f, ensure_ascii=False, indent=4)
        except IOError as e:
            print(f"!> Can't write to the file {DB_NAME}: {e}")
            exit(1)

    @classmethod
    def print_active(cls):
        """Print only ACTIVE to stdout"""
        cls.update_expiration_statuses()
        tasks = cls.db_load()
        if not cls.check_for_emptiness(tasks):
            tp.TaskPrinter.print_active(tasks)

    @classmethod
    def print_id(cls):
        """Print only NOT DELETED with ID column"""
        cls.update_expiration_statuses()
        tasks = cls.db_load()
        if not cls.check_for_emptiness(tasks):
            tp.TaskPrinter.print_id(tasks)

    @classmethod
    def print_id_all(cls):
        """Print ALL TASKS with ID column"""
        cls.update_expiration_statuses()
        tasks = cls.db_load()
        if not cls.check_for_emptiness(tasks):
            tp.TaskPrinter.print_id_all(tasks)

    @classmethod
    def print_tasks(cls):
        """Print only NOT DELETED from .json"""
        cls.update_expiration_statuses()
        tasks = cls.db_load()
        if not cls.check_for_emptiness(tasks):
            tp.TaskPrinter.print_tasks(tasks)

    @classmethod
    def print_tasks_all(cls):
        """Prints ALL TASKS from .json"""
        cls.update_expiration_statuses()
        tasks = cls.db_load()
        if not cls.check_for_emptiness(tasks):
            tp.TaskPrinter.print_tasks_all(tasks)

    @classmethod
    def create_db(cls):
        """Creates DB file (if doesn't exist)"""
        with open(DB_NAME, "w"):
            task = []
            task.append(Task())
            cls.db_dump(task)

        if os.path.exists(DB_NAME):
            print("=> DB succesfuly created")
        else:
            print("!> Can't create DB")

    @staticmethod
    def check_for_emptiness(tasks) -> bool:
        """Is .json empty?"""
        if not tasks:
            print("!> You don't have any tasks")
            return True
        return False
