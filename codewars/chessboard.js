/**
 * Created by jsonmartin on 5/20/16.
 */
"use strict";
//Refactored Solution
function chessBoard(rows, columns) {
  return Array.from({length: rows}, (_,i) => Array.from({length: columns}, (_,j) => ("OX"[(i+j)%2])));
}

//My Original solution
function chessBoardOirg(rows, columns) {
  let board = [];
  let isO = true;
  for(let r = 0; r < rows; r++) {
    let newRow = [];
    for(let c = 0; c < columns; c++) {
      newRow.push(isO ? "O" : "X");
      isO = !isO;
    }
    board.push(newRow);
    isO = columns % 2 === 0 ? !isO : isO;
  }
  return board;
}

let res = chessBoard(6,4);
console.log(res);
res = chessBoard(3,7);
console.log(res);