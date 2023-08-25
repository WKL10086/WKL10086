def is_input_valid(user_input: str) -> bool:
    if len(user_input) != 5:
        return False
    return True


def format_input(user_input: str) -> str:
    return user_input.lower()
