def create_action():
    return f"create_action "


def show_all_action():
    return f"show_all_action "


def update_action():
    return f"update_action "


def remove_action():
    return f"remove_action "


def crud_commands():
    return {
        "create": create_action,
        "list": show_all_action,
        "update": update_action,
        "remove": remove_action
    }
