import parser as ps
import tasksmanage as tm


def main():
    # Parse CLI flags
    args = ps.parseit()

    if args.create: # -c NAME DESCRIPTION EXPIRATION_DATE
        task = tm.Task()
        # Checking Arguments Count
        task.name = args.create[0] if len(args.create) > 0 else "Defaul Task"
        task.description = args.create[1] if len(args.create) > 1 else None
        task.expiration_date = ps.parse_expiration_date(args.create[2]) if len(args.create) > 2 else None
        # Saving Task to DB
        task.db_append()
        return
    if args.remove: # -r ID
        tm.Task.mark_deleted(args.remove[0])
        return
    if args.done: # -d ID
        tm.Task.mark_done(args.done[0])
        return
    if args.print_tasks: # -a
        tm.Task.print_tasks()
        return
    if args.print_all: # -A
        tm.Task.print_tasks_all()
        return
    if args.id: # -i
        tm.Task.print_id()
        return
    if args.all_id: # -I
        tm.Task.print_id_all()
        return
    else:
        # Execute without any flags
        # Prints only ACTIVE tasks
        tm.Task.print_active()
        return

if __name__ == '__main__':
    main()
