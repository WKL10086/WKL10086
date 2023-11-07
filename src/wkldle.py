import json
import os
from typing import Literal

import dictionary


def is_today_finish() -> bool:
    # TODO: Impl
    today_count = 0
    with open("./wkldle_stat/log.json", "r") as f:
        today_count = int(f.read())

    return today_count >= 6


def get_env_var() -> tuple[str, str]:
    title = os.environ["TITLE"]
    # TODO: parse title, remove "wkldle-"

    user_name = os.environ["USER"]
    return "PETER", user_name


def format_input(user_input: str) -> str:
    return user_input.upper()


def is_input_valid(user_input: str, dictionary: list[str]) -> tuple[bool, str]:
    if len(user_input) != 5:
        return False, "Input must be 5 characters long"

    if not user_input.encode("utf-8").isalpha():
        return False, "Input must be English letters only"

    if user_input not in dictionary:
        return False, "Input must be a valid word"

    return True, ""


def check_win_con(ans: str, user_input: str) -> bool:
    return ans == user_input


def check_char(ans: str, user_input: str) -> list[tuple[str, str]]:
    # NOTE: key: user_input char, value: "correct" | "misplaced" | "wrong"
    result = []

    for user_letter, correct_letter in zip(user_input, ans):
        if user_letter == correct_letter:
            result.append((user_letter, "correct"))
        elif user_letter in ans:
            result.append((user_letter, "misplaced"))
        else:
            result.append((user_letter, "wrong"))

    return result


def update_total_count(key: Literal["total-guessed", "completed"]) -> None:
    total_count = {}
    with open("./wkldle_stat/total.json", "r") as f:
        total_count = json.load(f)

    total_count[key] += 1

    with open("./wkldle_stat/total.json", "w") as f:
        json.dump(total_count, f)

    return


def main() -> None:
    word_list = dictionary.get_local_dictionary()
    ans = dictionary.pick_random_word(word_list)
    # print(ans)

    if is_today_finish():
        # TODO: save in readme
        print("Today's game is finished")
        return

    (user_input, user_name) = get_env_var()
    user_input = format_input(user_input)

    is_valid, error_msg = is_input_valid(user_input, word_list)
    if not is_valid:
        print(error_msg)
        return

    if check_win_con(ans, user_input):
        print("You win!")
        return

    # (char, correct | misplaced | wrong)[]
    char_dict = check_char(ans, user_input)
    # print(char_dict)
    # TODO: Update game state
    # TODO: Update readme

    return


if __name__ == "__main__":
    main()
