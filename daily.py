import helpers


def record_today_ans(ans: str) -> None:
    with open("./wkldle_stat/today_ans.txt", "w") as f:
        f.write(ans)


# TODO: Impl
def save_last_day_record() -> None:
    return


# TODO: Impl
def get_wkldle_readme_text() -> str:
    readme_text = f""""""
    return readme_text


# TODO: Save last day record
# TODO: Update readme
def main() -> None:
    dictionary = helpers.get_local_dictionary()

    ans = helpers.pick_random_word(dictionary)
    record_today_ans(ans)

    return
