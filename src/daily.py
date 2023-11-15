import datetime
import json

import readme


def get_wkldle_readme_text() -> str:
    style_text = readme.get_wkldle_style()

    wdkdle_text = readme.get_init_wkldle_text()

    return style_text + wdkdle_text


def main() -> None:
    # # prev_log
    # save_last_day_record()

    # # today_ans.json
    # word_list = dictionary.get_local_dictionary()
    # ans = dictionary.pick_random_word(word_list)
    # save_new_ans(ans)

    # # README.md
    # wkldle_readme_text = get_wkldle_readme_text()
    # self_intro = md_text.get_self_intro_readme_text()
    # readme_text = wkldle_readme_text + self_intro
    # update_readme(readme_text)

    # # game_state.json
    # init_game_state()

    # # log.json
    # init_log()

    return


if __name__ == "__main__":
    main()
