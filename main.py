from app_parser import arg_parser
from crud_commands import crud_commands


def handler_commands():
    arguments = arg_parser()
    commands = crud_commands()
    for command in commands.keys():
        if arguments.get("command") in command:
            return commands.get(command)()

    return f"Wrong command."


def main():
    return handler_commands()


if __name__ == "__main__":
    print(main())
