import argparse as ap
from datetime import datetime


# Parser block
def parseit():
    """Parse CLI flags"""
    parser = ap.ArgumentParser(description="Simple ToDo app written on pure python")

    parser.add_argument(
        "-c",
        "--create",
        nargs="*",
        metavar=("ARGS"),
        help="You can provide NAME, DESCRIPTION, EXPIRATION_DATE to create a new task",
    )
    parser.add_argument(
        "-f",
        "--db-create",
        action="store_true",
        help="Create a new DB file (if doesn't exist yet)",
    )
    parser.add_argument(
        "-r", "--remove", nargs=1, metavar=("ID"), help="Mark task/tasks as deleted"
    )
    parser.add_argument(
        "-d", "--done", nargs=1, metavar=("ID"), help="Mark task/tasks as completed"
    )
    parser.add_argument(
        "-a",
        "--print-tasks",
        action="store_true",
        help="Prints all tasks (excluding DELETED)",
    )
    parser.add_argument(
        "-A",
        "--print-all",
        action="store_true",
        help="Prints all tasks (including DELETED)",
    )
    parser.add_argument(
        "-i",
        "--id",
        action="store_true",
        help="Prints all tasks ID (excluding DELETED)",
    )
    parser.add_argument(
        "-I",
        "--all-id",
        action="store_true",
        help="Prints all tasks ID (including DELETED)",
    )
    parser.add_argument(
        "-S",
        "--cloud-save",
        action="store_true",
        help="Save .conf & .json files into your Cloud method, provided in .conf",
    )
    parser.add_argument(
        "-L",
        "--cloud-load",
        action="store_true",
        help="Load .conf & .json files from your Cloud method, provided in .conf",
    )

    args = parser.parse_args()

    return args


def parse_expiration_date(date_string):
    try:
        exp_date = datetime.strptime(date_string, "%d-%m-%Y, %H:%M:%S")
    except ValueError:
        raise ap.ArgumentTypeError(
            f'!> Incorrect date format: {date_string}. Use "DD-MM-YYYY, HH:MM:SS" instead.'
        )

    return exp_date
