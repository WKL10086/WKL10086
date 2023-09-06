def get_mit_word_list() -> list[str]:
    # src: https://www.mit.edu/~ecprice/wordlist.10000 for mit_10000.txt
    # src: https://github.com/dwyl/english-words for words_alpha.txt
    with open("words_alpha.txt") as f:
        return [line.strip() for line in f.readlines()]


def gen_filtered_word_list(word_list: list[str]) -> list[str]:
    new_word_list = []
    for word in word_list:
        if len(word) == 5:
            new_word_list.append(word.upper())
    return new_word_list


# NOTE: Delete some uncommon words from word_list.txt
def gen_new_file(word_list: list[str]):
    with open("word_list.txt", "w") as f:
        for word in word_list:
            f.write(word + "\n")


def main():
    mit_word_list = get_mit_word_list()
    word_list = gen_filtered_word_list(mit_word_list)
    gen_new_file(word_list)


if __name__ == "__main__":
    main()
