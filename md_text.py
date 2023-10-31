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


def get_style_readme_text() -> str:
    readme_text = """\
<style>
    .wrapper {
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    height: 100vh;
    }
    .board {
    width: 300px;
    height: 400px;
    }
    .keyboard {
    width: 600px;
    height: 360px;
    }
    .item {
    font-family: "nyt-franklin";
    width: 56px;
    display: inline-flex;
    justify-content: center;
    align-items: center;
    font-size: 32px;
    line-height: 1;
    font-weight: bold;
    vertical-align: middle;
    box-sizing: border-box;
    color: #d3d6da;
    background-color: #d3d6da;
    border: 2px solid #d3d6da;
    border-radius: 4px;
    padding: 12px;
    }
    .row {
    display: grid;
    grid-template-columns: repeat(5, 1fr);
    grid-gap: 5px;
    }
    .keyboard-row {
    display: flex;
    gap: 5px;
    justify-content: center;
    }
    .wrong {
    color: white;
    background-color: red;
    }
    .correct {
    color: white;
    background-color: #6aaa64;
    }
    .misplaced {
    color: white;
    background-color: #c9b458;
    }
    .not-guessed {
    color: black;
    background-color: #d3d6da;
    }
</style>

"""

    return readme_text


def get_init_readme_text() -> str:
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

    return readme_text
