import argparse as ap


# Parser block
def parseit():
    """Parse CLI flags"""
    parser = ap.ArgumentParser(
        description="Simple ToDo app written on pure python")

    parser.add_argument("-c", "--create", nargs=2, metavar=('NAME',
                        'DESCRIPTION'), help="Provide TITLE & DESCR to create a new task")
    parser.add_argument('-r', '--remove', nargs=1,
                        metavar=('ID'), help="Remove task")
    parser.add_argument('-d', '--done', nargs=1,
                        metavar=('ID'), help="Mark task as done")
    args = parser.parse_args()

    return args
