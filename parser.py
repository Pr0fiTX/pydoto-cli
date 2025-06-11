import argparse as ap
from datetime import datetime


# Parser block
def parseit():
    """Parse CLI flags"""
    parser = ap.ArgumentParser(
        description="Simple ToDo app written on pure python")

    parser.add_argument("-c", "--create", nargs='*', metavar=('ARGS'),
                        help="You can provide NAME, DESCRIPTION, EXPIRATION_DATE to create a new task")
    # parser.add_argument("-c", "--create", nargs='*', metavar=('NAME',
    #                     'DESCRIPTION', 'EXPIRATION_DATE'), help="Provide NAME, DESCRIPTION, EXPIRATION_DATE to create a new task")
    parser.add_argument('-r', '--remove', nargs=1,
                        metavar=('ID'), help="Mark task/tasks as deleted") # TODO: Opportunity to DELETE multiple tasks at once
    parser.add_argument('-d', '--done', nargs=1,
                        metavar=('ID'), help="Mark task/tasks as completed") # TODO: Opportunity to COMPLETE many tasks at once
    parser.add_argument('-a', '--print-tasks', action='store_true', help="Prints all tasks (excluding DELETED)")
    parser.add_argument('-A', '--print-all', action='store_true', help="Prints all tasks (including DELETED)")
    parser.add_argument('-i', '--id', action='store_true', help="Prints all tasks ID (excluding DELETED)")
    parser.add_argument('-I', '--all-id', action='store_true', help="Prints all tasks ID (including DELETED)")
    args = parser.parse_args()

    return args

def parse_expiration_date(date_string):
    try:
        exp_date = datetime.strptime(date_string, "%d-%m-%Y, %H:%M:%S")
    except ValueError:
        raise ap.ArgumentTypeError(f"!> Incorrect date format: {date_string}. Use \"DD-MM-YYYY, HH:MM:SS\" instead.")
    
    return exp_date
