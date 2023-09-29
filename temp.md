<style>
.board {
  width: 300px;
  height: 360px;
}
.item {
    font-family: "nyt-franklin";
    width: 100%;
    display: inline-flex;
    justify-content: center;
    align-items: center;
    font-size: 2rem;
    line-height: 1;
    font-weight: bold;
    vertical-align: middle;
    box-sizing: border-box;
    color: white;
    background-color: #d3d6da;
    border: 2px solid #d3d6da;
    padding: 0.75rem;
}
.row {
    display: grid;
    grid-template-columns: repeat(5, 1fr);
    grid-gap: 5px;
}
.wrong {
    background-color: #787c7e;
}
.correct {
    background-color: #6aaa64;
}
.misplaced {
    background-color: #c9b458;
}
.not-guessed {
    color: black;
    background-color: #d3d6da;
}
</style>

<div class="board ">
    <div class="row">
        <div class="item wrong">W</div>
        <div class="item"></div>
        <div class="item correct">T</div>
        <div class="item misplaced">E</div>
        <div class="item not-guessed">R</div>
    <div>
</div>
