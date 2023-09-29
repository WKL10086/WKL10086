import random
from typing import Literal


def get_local_dictionary() -> list[str]:
    with open("./dictionary/word_list.txt", "r") as f:
        return [line.strip() for line in f.readlines()]


def pick_random_word(word_list: list) -> str:
    return random.choice(word_list)


def get_core_readme_text() -> str:
    readme_text = """\
### Hi there 👋, my name is Peter Wong

#### I am a full stack developer

![I am a full stack developer ](https://cutshort.io/blog/wp-content/uploads/2018/04/bd1e5c2457278a37313c55ce8c887aa3.jpg)

Skills: React / TS / CSS / Python / Golang / C / C++ / SQL / Java / Rust

- 🔭 I’m currently working on e-commerce platform
- 🌱 I’m currently learning Rust

[![Top Langs](https://github-readme-stats.vercel.app/api/top-langs/?username=WKL10086)](https://github.com/anuraghazra/github-readme-stats)

![GitHub stats](https://github-readme-stats.vercel.app/api?username=WKL10086&show_icons=true&count_private=true)

![ayaya](https://count.ayaya.beauty/get/@WKL10086?theme=rule34)

"""

    return readme_text
