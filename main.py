from app_parser import arg_parser
from crud_commands import crud_commands


def handler_commands():
    arguments = arg_parser()
    commands = crud_commands()
    print(arguments)
    for command in commands.keys():
        if arguments.get("command") in command and len(arguments) == 3:
            return commands.get(command)(arguments.get("column"), arguments.get("value"))
        elif arguments.get("command") in command and len(arguments) == 2:
            return commands.get(command)(arguments.get("column"))
        elif arguments.get("command") in command and len(arguments) == 4:
            return commands.get(command)(arguments.get("column"), arguments.get("value"), arguments.get("id"))
    return f"Wrong command."


def main():
    print(handler_commands())


if __name__ == "__main__":
    main()
