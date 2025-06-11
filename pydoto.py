import parser as ps
import tasksmanage as tm


def main():
    # Parse CLI flags
    args = ps.parseit()

    if args.create: # -c NAME DESCRIPTION EXPIRATION_DATE
        task = tm.Task()
        # Chacking Arguments Count
        task.name = args.create[0] if len(args.create) > 0 else "Defaul Task"
        task.description = args.create[1] if len(args.create) > 1 else None
        task.expiration_date = ps.parse_expiration_date(args.create[2]) if len(args.create) > 2 else None
        # Saving Task to DB
        task.db_append()
        return
    if args.remove: # -r ID
        pass
    if args.done: # -d ID
        pass
    if args.print_tasks: # -a
        pass
    if args.print_all: # -A
        pass
    if args.id: # -i
        pass
    if args.all_id: # -I
        pass
    else:
        # Execute witheout any flags
        # Prints only ACTIVE tasks
        tm.Task.print_active()
        return

if __name__ == '__main__':
    main()
