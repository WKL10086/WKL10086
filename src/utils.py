import os


class Context:
    def __init__(
        self, title: str, user_name: str, access_token: str, mode: str
    ) -> None:
        self.title = title
        self.user_name = user_name
        self.access_token = access_token
        self.mode = mode


def get_env_var() -> Context:
    title = os.environ.get("TITLE", "")
    # TODO: parse title, remove "wkldle-"

    user_name = os.environ.get("USER_NAME", "")

    access_token = os.environ.get("TOKEN", "")

    mode = os.environ.get("MODE", "")

    context = Context(title, user_name, access_token, mode)

    return context
