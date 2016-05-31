/**
 * Created by jsonmartin on 5/30/16.
 */
"use strict";
let generateMatrix = function(n){
  let matrix = new Array(n).fill(undefined).map(() => new Array(n).fill(null));
  let bounds = 0;
  let counter = 1;

  let traverse = function() {
    let tBound = bounds;
    let rBound = n - bounds - 1;
    let bBound = n - bounds - 1;
    let lBound = bounds;
    //console.log("---------");
    //console.log("tBound:", tBound);
    //console.log("rBound:", rBound);
    //console.log("bBound:", bBound);
    //console.log("lBound:", lBound);
    if(tBound === rBound && rBound === bBound && bBound === lBound) {
      //console.log("THEY EQUAL!");
      matrix[bounds][bounds] = counter++;
      return;
    }
    //Top left -> Top Right
    for(let x = tBound; x < rBound; x++) {
      matrix[tBound][x] = counter++;
    }

    //Top Right -> Bottom Right
    for(let y = tBound; y <= bBound; y++) {
      matrix[y][rBound] = counter++;
    }

    rBound--;

    //Bottom right -> Bottom Left
    for(let x = rBound; x >= lBound; x--) {
      matrix[bBound][x] = counter++;
    }

    bBound--;

    //Bottom Left -> Top Left
    for(let y = bBound; y > tBound; y--) {
      matrix[y][lBound] = counter++;
    }
  };

  while(bounds <= Math.floor((n - 1)/2)) {
    traverse();
    //console.log("Matrix for bounds:" + bounds);
    //console.log(matrix);
    bounds++;
  }
  //console.log(matrix);
  return matrix;
};

generateMatrix(80);