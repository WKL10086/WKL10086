import datetime

import wkldle_stat


def init_log() -> None:
    wkldle_stat.write_log([])

    return


def save_last_day_record() -> None:
    today_ans = wkldle_stat.load_ans()
    today_log = wkldle_stat.load_log()

    today_log.insert(
        0,
        today_ans,
    )
    current_time = datetime.datetime.now().isoformat(timespec="seconds")

    wkldle_stat.write_prev_log(today_log, current_time)

    return
