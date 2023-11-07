import json
from typing import Literal, overload


@overload
def load_json(filename: Literal["ans", "game_state", "total_count"]) -> dict:
    ...


@overload
def load_json(filename: Literal["log"]) -> list[dict]:
    ...


def load_json(filename: str) -> dict | list[dict]:
    with open(f"../wkldle_stat/{filename}.json", "r") as f:
        return json.load(f)


def load_ans() -> dict[str, str]:
    return load_json("ans")


def load_game_state() -> dict[str, str]:
    return load_json("game_state")


def load_log() -> list[dict]:
    return load_json("log")


def load_total_count() -> dict[str, int]:
    return load_json("total_count")


def write_json(
    filename: Literal["ans", "game_state", "log", "total_count"],
    data: dict | list[dict],
) -> None:
    with open(f"../wkldle_stat/{filename}.json", "w") as f:
        json.dump(data, f, indent=2)


def write_ans(data: dict[str, str]) -> None:
    write_json("ans", data)


def write_game_state(data: dict[str, str]) -> None:
    write_json("game_state", data)


def write_log(data: list[dict]) -> None:
    write_json("log", data)


def write_total_count(data: dict[str, int]) -> None:
    write_json("total_count", data)
