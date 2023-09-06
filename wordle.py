import helpers


def is_today_finish() -> bool:
    # TODO: can count the number of lines in today_progress.txt
    today_count = 0
    with open("./wordle_stat/today_count.txt", "r") as f:
        today_count = int(f.read())

    return today_count >= 6


def get_user_input() -> str:
    return input("Enter your guess: ")


def format_input(user_input: str) -> str:
    return user_input.lower()


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


def check_char(ans: str, user_input: str) -> dict[str, str]:
    # NOTE: key: user_input char, value: "correct" | "misplaced" | "wrong"
    char_dict = {}

    for i in range(len(user_input)):
        current_char = ans[i]
        if current_char == user_input[i]:
            char_dict[current_char] = "correct"
        elif current_char in user_input:
            char_dict[current_char] = "misplaced"
        else:
            char_dict[current_char] = "wrong"

    return char_dict


def main() -> None:
    dictionary = helpers.get_local_dictionary()

    ans = helpers.pick_random_word(dictionary)
    print(ans)

    while True:
        if is_today_finish():
            print("Today's game is finished")
            break

        user_input = get_user_input()
        user_input = format_input(user_input)

        is_valid, error_msg = is_input_valid(user_input, dictionary)
        if not is_valid:
            print(error_msg)
            continue

        if check_win_con(ans, user_input):
            print("You win!")
            break

        char_dict = check_char(ans, user_input)
        print(char_dict)
        # TODO: Update readme


# if __name__ == "__main__":
#     main()
