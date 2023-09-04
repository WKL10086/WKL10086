import random


def get_local_dictionary() -> list[str]:
    with open("./dictionary/word_list.txt", "r") as f:
        return [line.strip() for line in f.readlines()]


def pick_random_word(word_list: list) -> str:
    return random.choice(word_list)
