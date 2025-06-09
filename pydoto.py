import parser as ps
import tasksmanage as tm


def main():
    # Parse CLI flags
    args = ps.parseit()

    if args.create:
        task = tm.Task(args.create[0], args.create[1]).save_to_json()
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
