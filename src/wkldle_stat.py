import json


def load_json(filename: str):
    with open(f"../wkldle_stat/{filename}.json", "r") as f:
        return json.load(f)


def load_ans():
    return load_json("ans")


def load_game_state():
    return load_json("game_state")


def load_log():
    return load_json("log")


def load_total_count():
    return load_json("total_count")


def write_json(filename: str, data: dict | list):
    with open(f"../wkldle_stat/{filename}.json", "w") as f:
        json.dump(data, f, indent=2)


def write_ans(data: dict[str, str]):
    write_json("ans", data)


def write_game_state(data: dict[str, str]):
    write_json("game_state", data)


def write_log(data: list[dict]):
    write_json("log", data)


def write_total_count(data: dict[str, int]):
    write_json("total_count", data)
