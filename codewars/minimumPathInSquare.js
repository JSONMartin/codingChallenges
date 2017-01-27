// https://www.codewars.com/kata/minimum-path-in-squares/train/javascript
// Dynamic programming

/*
You're given a square consisting of random numbers, like so:

var square = [
  [1,2,3],
  [4,8,2],
  [1,5,3]];
Your job is to calculate the minimum total cost when moving from the upper left corner to the coordinate given. You're only allowed to move right or down.

In the above example the minimum path would be:

var square = [
  [1,2,3],
  [_,_,2],
  [_,_,3]];
Giving a total of 11. Start and end position are included.

Note: Coordinates are marked as x horizontally and y vertically.
*/
let callCount = 0;

Array.prototype.deepCopy = function() {
    return JSON.parse(JSON.stringify(this));
};

function minPath(grid, col, row) {
    const result = [...Array(grid.length).keys()].map(i => Array(grid.length).fill(0));

    // Set starting position
    result[0][0] = grid[0][0];

    // Fill Top Column out, going straight across right
    for (let x = 1; x <= col; x++) {
        console.log(result);
        result[0][x] = grid[0][x] + result[0][x - 1];
    }
    // Fill Left Column out, going straight down
    for (let y = 1; y <= row; y++) {
        console.log(result);
        result[y][0] = grid[y][0] + result[y - 1][0];
    }

    // Traverse through matrix from left to right, then top to bottom,
    // Checking if the minimum so far yet is from left or top, then add
    // The result and set as new minimum
    for (let y = 1; y <= row; y++) {
        for (let x = 1; x <= col; x++) {
            console.log(`Row:${y}, Col:${x}`);
            console.log(result);
            result[y][x] = grid[y][x] + Math.min(result[y - 1][x], result[y][x - 1]);
        }
    }

    return result[row][col];
}

// Array cache implementation (my best solution before revealing answer). Correct, just too slow
function minPathWithArray(grid, col, row) {
    const length = grid.length;
    let cache = grid.deepCopy().map((i) => i.map((x) => Infinity)), minTotalFound = Infinity;

    function traversePath(curCol, curRow, counter = 0) {
        console.log(cache);
        callCount++;
        if (!grid[curRow][curCol] || curRow > row || curCol > col) {
            return false;
        }

        cache[curRow][curCol] = Math.min(cache[curRow][curCol], counter + grid[curRow][curCol]);

        if (curRow === row && curCol === col) {
            return minTotalFound = counter;
        }
        else {
            if (curCol + 1 <= col && counter + grid[curRow][curCol] < cache[curRow][curCol + 1]) traversePath(curCol + 1, curRow, counter + grid[curRow][curCol]); // Go Right
            if (curRow + 1 <= row && counter + grid[curRow][curCol] < cache[curRow + 1][curCol]) traversePath(curCol, curRow + 1, counter + grid[curRow][curCol]); // Go Down
        }
    }

    traversePath(0, 0);
    return cache[row][col];
}

// Object cache implementation
function minPathWithObjCache(grid, col, row) {
    const length = grid.length;

    let cache = {}, minTotalFound = Infinity;

    function traversePath(curCol, curRow, counter = 0) {
        console.log(cache);
        callCount++;
        if (!grid[curRow][curCol] || curRow > row || curCol > col) {
            return false;
        }

        let key = curRow + "," + curCol;
        cache[key] = Math.min((cache[key] || Infinity), counter + grid[curRow][curCol]);

        if (curRow === row && curCol === col) {
            return minTotalFound = counter + grid[curRow][curCol];
        }
        else {
            key = curRow + "," + (curCol + 1);
            if (curCol + 1 <= col
                &&
                (!cache[key] || counter + grid[curRow][curCol] < cache[key])) traversePath(curCol + 1, curRow, counter + grid[curRow][curCol]); // Go Right
            key = (curRow + 1) + "," + curCol;
            if (curRow + 1 <= row
                &&
                (!cache[key] || counter + grid[curRow][curCol] < cache[key])) traversePath(curCol, curRow + 1, counter + grid[curRow][curCol]); // Go Down
        }
    }

    traversePath(0, 0);
    let key = row + "," + col;
    return cache[key];
}


// TESTS
var square = [
    [1, 2, 3, 6, 2, 8, 1],
    [4, 8, 2, 4, 3, 1, 9],
    [1, 5, 3, 7, 9, 3, 1],
    [4, 9, 2, 1, 6, 9, 5],
    [7, 6, 8, 4, 7, 2, 6],
    [2, 1, 6, 2, 4, 8, 7],
    [8, 4, 3, 9, 2, 5, 8]];

console.log("---------------------------");
//minPath(square, 0, 0); // => 1
let res = minPath(square, 6, 6); // => 11
console.log(res);
console.log("Call Count:", callCount);
