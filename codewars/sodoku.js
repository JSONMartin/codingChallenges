/*
Sodoku solution validator

https://www.codewars.com/kata/529bf0e9bdf7657179000008/solutions/javascript
*/

function validSolution(boardInput){
  const length = boardInput.length;

  const validateBoard = board => {
    let seenRows, seenCols, curNum;

    for (let row = 0; row < length; row++) {
      seenRows = {}, seenCols = {};

      for (let i = 0; i < length; i++) {
        // Check Rows
        curNum = board[row][i];
        if (curNum in seenRows) return false;
        seenRows[curNum] = true;

        // Check Cols
        curNum = board[i][row];
        if (curNum in seenCols) return false;
        seenCols[curNum] = true;
      }
    }
    return true;
  };

  const checkGrid = (r, c) => {
    let seen = {};
    r *= 3; c *= 3;

    for (let row = r; row <= r + 2; row++) {
      let curRow = boardInput[row].slice(c, c + 3);

      for (let num of curRow) {
        if (num in seen) return false;
        seen[num] = true;
      }
    }

    return true;
  };

  for (let i = 0; i <= 2; i++) {
    for (let j = 0; j <= 2; j++) {
      if (!checkGrid(i, j)) return false;
    }
  }

  return validateBoard(boardInput);
}
