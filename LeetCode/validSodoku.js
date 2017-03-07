// https://leetcode.com/submissions/detail/94078927/
/**
 * @param {character[][]} board
 * @return {boolean}
 */
var isValidSudoku = function(board) {
    // Check if each row is unique
    for (let row of board) {
        let seen = {};

        for (let cell of row) {
            if (cell === '.') continue;
            else if (seen[cell]) return false;
            seen[cell] = true;
        }
    }

    // Check if each column is unique
    for (let col = 0; col < 9; col++) {
        let seen = {};

        for (let cell = 0; cell < board.length; cell++) {
            let num = board[cell][col];
            if (num === '.') continue;
            else if (seen[num]) return false;
            seen[num] = true;
        }
    }

    // Check that each 3x3 grid has all unique
    const checkGrid = (startRow, startCol) => {
        let contents = [];

        for (let row = 0; row < 3; row++) {
            for (let col = 0; col < 3; col++) {
                if (board[startRow + row][startCol + col] === ".") continue;
                contents.push(board[startRow + row][startCol + col]);
            }
        }

        return contents.length === [...new Set(contents)].length;
    }

    for (let row = 0; row < board.length; row += 3) {
        for (let col = 0; col < board.length; col += 3) {
            if (!checkGrid(row, col)) return false;
        }
    }

    // No false check has been found, therefore the puzzle can be solved successfully
    return true;
};
