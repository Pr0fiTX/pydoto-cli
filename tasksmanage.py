import json as js
import os
from datetime import datetime
from enum import Enum


DB_NAME = 'pydoto.json'

class TaskStatus(Enum):
    ACTIVE = 'active'
    COMPLETED = 'completed'
    EXPIRED = 'expired'
    DELETED = 'deleted'


class Task:
    def __init__(self, name="Default Task", description=None, expiration_date=None):
        self.name = name
        self.description = description
        self.creation_date = datetime.now()
        self.expiration_date = expiration_date
        self.status = TaskStatus.ACTIVE

    def check_expiration(self): # WARN:
        if (self.expiration_date and self.expiration_date < datetime.now() and self.status == TaskStatus.ACTIVE):
            self.status = TaskStatus.EXPIRED

        return self.status

    def complete(self):
        self.check_expiration()
        if (self.status == TaskStatus.DELETED):
            raise ValueError("!> You can't complite deleted task")
        else:
            self.status = TaskStatus.COMPLETED

        return self.status

    def to_dict(self):
        return {
            "name": self.name,
            "description": self.description,
            "status": self.status.value,
            "creation_date": self.creation_date.isoformat(),
            "expiration_date": self.expiration_date.isoformat() if self.expiration_date else None
        }

    def save_to_json(self):
        """Load and save to json"""
        tasks = []

        if os.path.exists(DB_NAME):
            try:
                with open(DB_NAME, 'r', encoding='utf-8') as f:
                    tasks = js.load(f)
                    if not isinstance(tasks, list):
                        tasks = [tasks]
            except (js.JSONDecodeError, IOError) as e:
                print(f"!> Can't read the file {DB_NAME}: {e}")

        tasks.append(self.to_dict())

        try:
            with open(DB_NAME, 'w', encoding='utf-8') as f:
                js.dump(tasks, f, ensure_ascii=False, indent=4)
        except IOError as e:
            print(f"!> Can't write to the file {DB_NAME}: {e}")

    @classmethod
    def update_expiration_statuses(cls):
        tasks = []
        tasks_new = []

        if os.path.exists(DB_NAME):
            try:
                with open(DB_NAME, 'r', encoding='utf-8') as f:
                    tasks = js.load(f)
                    if not isinstance(tasks, list):
                        tasks = [tasks]
            except (js.JSONDecodeError, IOError) as e:
                print(f"!> Can't read the file {DB_NAME}: {e}")

            for task in tasks:
                task = cls.from_dict(task)
                if (task.expiration_date and task.status == TaskStatus.ACTIVE and task.expiration_date < datetime.now()):
                    task.status = TaskStatus.EXPIRED

                tasks_new.append(task.to_dict())

            try:
                with open(DB_NAME, 'w', encoding='utf-8') as f:
                    js.dump(tasks_new, f, ensure_ascii=False, indent=4)
            except IOError as e:
                print(f"!> Can't write to the file {DB_NAME}: {e}")

    @classmethod
    def from_dict(cls, data):
        expiration_date = datetime.fromisoformat(data['expiration_date']) if data['expiration_date'] else None
        task = cls(data['name'], data['description'], expiration_date)
        task.creation_date = datetime.fromisoformat(data['creation_date'])
        task.status = TaskStatus(data['status'])

        return task

    @classmethod
    def load_from_json(cls):
        if not os.path.exists(DB_NAME):
            print(f"!> File {DB_NAME} doesn't exist")

            return []
        
        try:
            with open(DB_NAME, "r", encoding='utf-8') as f:
                tasks_data = js.load(f)
                if not isinstance(tasks_data, list):
                    tasks_data = [tasks_data]

                return [cls.from_dict(task_data) for task_data in tasks_data]

        except (js.JSONDecodeError, IOError) as e:
            print(f"!> Can't read {DB_NAME}: {e}")

            return []

    @classmethod
    def print_active(cls): # TODO: Prettier Output
        tasks = cls.load_from_json()
        if not tasks:
            print("!> You don't have any active tasks")
            return

        print("=== ACTIVE TASKS ===")
        for i, task in enumerate(tasks, 1):
            cls.update_expiration_statuses()
            if (task.status != TaskStatus.ACTIVE):
                continue

            print(f"{task.name}\t",
                  f"{task.description}\t" if task.description else "-\t",
                  f"{task.expiration_date}\t" if task.expiration_date else "-\t")

        return
