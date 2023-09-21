import datetime
import json

import helpers


def record_new_ans(ans: str) -> None:
    content = {
        "ans": ans,
    }
    json_content = json.dumps(content, indent=2)

    with open("./wkldle_stat/today_ans.json", "w") as f:
        f.write(json_content)

    return


def save_last_day_record() -> None:
    today_date = datetime.date.today().strftime("%Y-%m-%d")

    today_ans = {}
    with open("./wkldle_stat/today_ans.json", "r") as f:
        today_ans = json.load(f)

    today_log = []
    with open("./wkldle_stat/log.json", "r") as f:
        today_log = json.load(f)

    today_log.insert(
        0,
        today_ans,
    )
    json_log = json.dumps(today_log, indent=2)

    with open(f"./wkldle_stat/prev_log/log.{today_date}.json", "w") as f:
        f.write(json_log)

    return


# TODO: Impl
def get_wkldle_readme_text() -> str:
    readme_text = f""""""
    return readme_text


# TODO: Update readme
def main() -> None:
    save_last_day_record()

    dictionary = helpers.get_local_dictionary()
    ans = helpers.pick_random_word(dictionary)
    record_new_ans(ans)

    return


if __name__ == "__main__":
    main()
