import wkldle_stat


def save_new_ans(ans: str) -> None:
    wkldle_stat.write_ans({"ans": ans})

    return


def get_ans() -> str:
    return wkldle_stat.load_ans()["ans"]
