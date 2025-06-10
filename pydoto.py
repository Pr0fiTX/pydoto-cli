import parser as ps
import tasksmanage as tm


def main():
    # Parse CLI flags
    args = ps.parseit()

    if args.create:
        # task = tm.Task(args.create[0])
        task = tm.Task()
        task.name = args.create[0] if len(args.create) > 0 else "Defaul Task"
        task.description = args.create[1] if len(args.create) > 1 else None
        task.expiration_date = ps.parse_expiration_date(args.create[2]) if len(args.create) > 2 else None
        task.save_to_json()
        return
    if args.remove:
        pass
    if args.done:
        pass
    else:
        tm.Task.print_active()
        return

if __name__ == '__main__':
    main()
