import helpers


def record_today_ans(ans: str) -> None:
    with open("./wordle_stat/today_ans.txt", "w") as f:
        f.write(ans)


# TODO: Save last day record
# TODO: Update readme
def main() -> None:
    dictionary = helpers.get_local_dictionary()

    ans = helpers.pick_random_word(dictionary)
    record_today_ans(ans)

    return
