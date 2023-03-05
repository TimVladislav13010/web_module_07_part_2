from app_parser import arg_parser
from crud_commands import crud_commands


def handler_commands():
    arguments = arg_parser()
    commands = crud_commands()
    print(arguments)
    print(commands)
    print(arguments.get("command"))


if __name__ == "__main__":
    handler_commands()
