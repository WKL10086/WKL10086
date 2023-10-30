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


def init_game_state() -> None:
    with open("./wkldle_stat/game_state.json", "w") as f:
        game_state = {chr(i): "not-guessed" for i in range(ord("A"), ord("Z") + 1)}
        json.dump(game_state, f)


def init_log() -> None:
    with open("./wkldle_stat/log.json", "w") as f:
        json.dump([], f)


# TODO: Impl
def get_wkldle_readme_text() -> str:
    readme_text = f""""""
    return readme_text


def update_readme(readme_text: str) -> None:
    with open("./README.md", "w") as f:
        f.write(readme_text)

    return


def main() -> None:
    # prev_log
    save_last_day_record()

    # today_ans.json
    dictionary = helpers.get_local_dictionary()
    ans = helpers.pick_random_word(dictionary)
    record_new_ans(ans)

    # README.md
    wkldle_readme_text = get_wkldle_readme_text()
    core_readme_text = helpers.get_core_readme_text()
    readme_text = wkldle_readme_text + core_readme_text
    update_readme(readme_text)

    # game_state.json
    init_game_state()

    # log.json
    init_log()

    return


if __name__ == "__main__":
    main()
