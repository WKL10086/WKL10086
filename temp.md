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

<div class="wrapper">
  <div class="board">
    <div class="row">
      <div class="item wrong">P</div>
      <div class="item misplaced">E</div>
      <div class="item correct">T</div>
      <div class="item misplaced">E</div>
      <div class="item wrong">R</div>
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
      <div class="item misplaced">E</div>
      <div class="item wrong">R</div>
      <div class="item correct">T</div>
      <div class="item not-guessed">Y</div>
      <div class="item not-guessed">U</div>
      <div class="item not-guessed">I</div>
      <div class="item not-guessed">O</div>
      <div class="item wrong">P</div>
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
