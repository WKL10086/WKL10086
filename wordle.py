import random


def get_local_dictionary() -> list[str]:
    with open("./dictionary/word_list.txt", "r") as f:
        return [line.strip() for line in f.readlines()]


get_local_dictionary()


def pick_random_word(word_list: list) -> str:
    return random.choice(word_list)


def is_today_finish() -> bool:
    today_count = 0
    with open("today_count.txt", "r") as f:
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
    # key: user_input char, value: "correct" | "wrong position" | "not in answer"
    char_dict = {}

    for i in range(len(user_input)):
        current_char = ans[i]
        if current_char == user_input[i]:
            char_dict[current_char] = "correct"
        elif current_char in user_input:
            char_dict[current_char] = "wrong position"
        else:
            char_dict[current_char] = "not in answer"

    return char_dict


# TODO: Game Flow
# 1. Get today's word
# 2. Start loop:
# 3. Check if today's game is finished, if yes, exit loop (6 times wrong)
# 4. Get user input
# 5. Check if user input is valid
# 6. Check if user input is correct
# 7. If not correct, print out the result of the user input, increment the count of tries, and go back to step 3
# 8. If correct or out of tries, exit loop
# 9. Display the result of the game (progress, user input, user info)
# 10. Save today's game result


# TODO: Separate the daily logic and the game logic for diff github actions
def main() -> None:
    dictionary = get_local_dictionary()

    ans = pick_random_word(dictionary)
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


# if __name__ == "__main__":
#     main()
