import datetime
import json

import dictionary
import md_text


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

    return


def init_log() -> None:
    with open("./wkldle_stat/log.json", "w") as f:
        json.dump([], f)

    return


def get_wkldle_readme_text() -> str:
    style_text = md_text.get_style_readme_text()

    readme_text = """\
<div class="wrapper">
  <div class="board">
    <div class="row">
      <div class="item">!</div>
      <div class="item">!</div>
      <div class="item">!</div>
      <div class="item">!</div>
      <div class="item">!</div>
      <div class="item">!</div>
      <div class="item">!</div>
      <div class="item">!</div>
      <div class="item">!</div>
      <div class="item">!</div>
      <div class="item">!</div>
      <div class="item">!</div>
      <div class="item">!</div>
      <div class="item">!</div>
      <div class="item">!</div>
      <div class="item">!</div>
      <div class="item">!</div>
      <div class="item">!</div>
      <div class="item">!</div>
      <div class="item">!</div>
      <div class="item">!</div>
      <div class="item">!</div>
      <div class="item">!</div>
      <div class="item">!</div>
      <div class="item">!</div>
      <div class="item">!</div>
      <div class="item">!</div>
      <div class="item">!</div>
      <div class="item">!</div>
      <div class="item">!</div>
    </div>
  </div>

  <br />

  <div class="keyboard">
    <div class="keyboard-row">
      <div class="item not-guessed">Q</div>
      <div class="item not-guessed">W</div>
      <div class="item not-guessed">E</div>
      <div class="item not-guessed">R</div>
      <div class="item not-guessed">T</div>
      <div class="item not-guessed">Y</div>
      <div class="item not-guessed">U</div>
      <div class="item not-guessed">I</div>
      <div class="item not-guessed">O</div>
      <div class="item not-guessed">P</div>
    </div>
    <br />
    <div class="keyboard-row">
      <div class="item not-guessed">A</div>
      <div class="item not-guessed">S</div>
      <div class="item not-guessed">D</div>
      <div class="item not-guessed">F</div>
      <div class="item not-guessed">G</div>
      <div class="item not-guessed">H</div>
      <div class="item not-guessed">J</div>
      <div class="item not-guessed">K</div>
      <div class="item not-guessed">L</div>
    </div>
    <br />
    <div class="keyboard-row">
      <div class="item not-guessed">Z</div>
      <div class="item not-guessed">X</div>
      <div class="item not-guessed">C</div>
      <div class="item not-guessed">V</div>
      <div class="item not-guessed">B</div>
      <div class="item not-guessed">N</div>
      <div class="item not-guessed">M</div>
    </div>
  </div>
</div>

"""

    return style_text + readme_text


def update_readme(readme_text: str) -> None:
    with open("./README.md", "w") as f:
        f.write(readme_text)

    return


def main() -> None:
    # prev_log
    save_last_day_record()

    # today_ans.json
    word_list = dictionary.get_local_dictionary()
    ans = dictionary.pick_random_word(word_list)
    record_new_ans(ans)

    # README.md
    wkldle_readme_text = get_wkldle_readme_text()
    self_intro = md_text.get_self_intro_readme_text()
    readme_text = wkldle_readme_text + self_intro
    update_readme(readme_text)

    # game_state.json
    init_game_state()

    # log.json
    init_log()

    return


if __name__ == "__main__":
    main()
