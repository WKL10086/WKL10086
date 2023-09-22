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
    border: 2px solid #d3d6da;
}
.row {
    display: grid;
    grid-template-columns: repeat(5, 1fr);
    grid-gap: 5px;
}
</style>

<div class="board">
<div class="row">
<div class="item">
    Q
</div>
<div class="item">
    W
</div>
<div class="item">
    E
</div>
<div class="item">
    R
</div>
<div class="item">
    T
</div>
<div>
</div>
