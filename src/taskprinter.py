class TaskPrinter:
    COMPLETED_M = "[x]"
    DELETED_M = "[d]"
    EXPIRED_M = "[e]"
    ACTIVE_M = "[ ]"

    @classmethod
    def mark_choser(cls, task) -> str:
        """Returns pretty thing:3"""
        match task.status.value:
            case "active":
                return cls.ACTIVE_M
            case "deleted":
                return cls.DELETED_M
            case "expired":
                return cls.EXPIRED_M
            case "completed":
                return cls.COMPLETED_M
            case _:
                return " "

    @classmethod
    def print_tasks_all(cls, tasks):
        for task in tasks:
            cls.task_out(task, 1, 0, 1, 1, 1)

    @classmethod
    def print_tasks(cls, tasks):
        for task in tasks:
            if task.status.value == "deleted":
                continue

            cls.task_out(task, 1, 0, 1, 1, 1)

    @classmethod
    def print_id_all(cls, tasks):
        for task in tasks:
            cls.task_out(task, 1, 1, 1, 1, 1)

    @classmethod
    def print_id(cls, tasks):
        for task in tasks:
            if task.status.value == "deleted":
                continue

            cls.task_out(task, 1, 1, 1, 1, 1)

    @classmethod
    def print_active(cls, tasks):
        for task in tasks:
            if task.status.value != "active":
                continue

            cls.task_out(task, 1, 0, 1, 1, 1)

    @classmethod
    def task_out(cls, task, sta=0, id=0, nam=0, des=0, exp=0):
        """Task output template, out tasks ONLY via this function!"""
        print(
            f"{cls.mark_choser(task)}" if sta else "",
            f'| "{task.creation_date}" |' if id else "",
            f"{task.name}" if nam else "",
            f"| {task.description} " if task.description and des else "",
            f"| {task.expiration_date}" if task.expiration_date and exp else "",
        )
