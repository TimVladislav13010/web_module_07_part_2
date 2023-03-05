from seeds.seeds import create, update


def create_action(model: str, value: str | int | float):
    create_func = create()

    for col in create_func.keys():
        if model in col:
            result = create_func.get(model)(value)

            return result

    return f"Wrong model..."


def show_all_action():
    return f"show_all_action "


def update_action(model, value, id_):
    update_func = update()

    for col in update_func.keys():
        if model in col:
            result = update_func.get(model)(id_, value)

            return result

    return f"Wrong model..."


def remove_action():
    return f"remove_action "


def crud_commands():
    return {
        "create": create_action,
        "list": show_all_action,
        "update": update_action,
        "remove": remove_action
    }
