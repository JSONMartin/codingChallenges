/**
 * Created by jsonmartin on 6/2/16.
 */
"use strict";

function parseStringLeetCode(matrix) {
  let parsedStringInput = [];
    console.log("Matrix Before trans:", matrix);

    matrix.forEach((row) => {
      if(!Array.isArray(row)) {
        let newRow = row.split("").map((num) => parseInt(num));
        parsedStringInput.push(newRow);
        console.log("parsedStringInput:", parsedStringInput)
      } else {
        console.log("Row:", row);
        let newRow = row.map((num) => parseInt(num));
        parsedStringInput.push(newRow);
      }
    });

    console.log("Matrix after trans:", parsedStringInput);
    return parsedStringInput;
}

function islandCount(matrix) {
  matrix = parseStringLeetCode(matrix); // This helper method transforms input from LeetCode

  let islandCount = 0;

  let checkSingleArrayRow = (col) => { // Added for LeetCode single row test case
    if(col < 0 || col >= matrix.length) { return; } //Base Case
    if(matrix[col] === 1) {
      matrix[col] = 2;
      checkSingleArrayRow(col - 1); // Check Left
      checkSingleArrayRow(col + 1); // Check Right
    }
  };

  let checkEdges = (row, col) => {
    // Check bounds
    if(row < 0 || row >= matrix.length) { return; } //Base Case
    if(col < 0 || col >= matrix[0].length) { return; } //Base Case

    // Traverse Each Cardinal direction in matrix, checking for 1s
    if(matrix[row][col] === 1) {
      matrix[row][col] = 2;
      checkEdges(row, col - 1); // Check Left
      checkEdges(row, col + 1); // Check Right
      checkEdges(row + 1, col); // Check Up
      checkEdges(row - 1, col); // Check Down
    }
  };

  if(!Array.isArray(matrix[0])) { // If only single row matrix (array), LeetCode addition
    for(let col = 0; col < matrix.length; col++) {
      //console.log(matrix);
      if(matrix[col] === 1) {
        islandCount++;
        checkSingleArrayRow(col);
      }
    }
  } else { // Multi row/column matrix
    for(let row = 0; row < matrix.length; row++) {
      for(let col = 0; col < matrix[0].length; col++) {
        if(matrix[row][col] === 1) {
          islandCount++;
          checkEdges(row, col);
        }
      }
    }
  }

  return islandCount;
}

// let testMatrix = [
//   [0, 1, 0, 1, 0],
//   [0, 0, 1, 1, 1],
//   [1, 0, 0, 1, 0],
//   [0, 1, 1, 0, 0],
//   [1, 0, 1, 0, 1]
// ];

let testMatrix;

testMatrix = [
  [1, 1, 1, 1, 0],
  [1, 1, 0, 1, 0],
  [1, 1, 0, 0, 0],
  [0, 0, 0, 0, 0]
]; // => 1 island

// testMatrix = [
//   [1, 1, 0, 0, 0],
//   [1, 1, 0, 0, 0],
//   [0, 0, 1, 0, 0],
//   [0, 0, 0, 1, 1]
// ]; // => 3 island

/*
LeetCode input tests
 */
//testMatrix = ["0", "0", "0"]; // => 1 island
//testMatrix = ["1011011"]; // => 3 island

//testMatrix = ["1","0", "1"];

let res = islandCount(testMatrix);
console.log("Result:", res);

