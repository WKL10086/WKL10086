import wkldle_stat


def init_game_state() -> None:
    inital_game_state = {chr(i): "not-guessed" for i in range(ord("A"), ord("Z") + 1)}

    wkldle_stat.write_game_state(inital_game_state)

    return
