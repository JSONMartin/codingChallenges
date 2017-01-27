function spiralArrayTraversal(arr) {
  var x = 0, y = 0; //Starting position
  var topBound = 0, rightBound = arr[0].length, bottomBound = arr.length, leftBound = 0;

  while(topBound < bottomBound && leftBound < rightBound) {
    for(x = leftBound; x < rightBound; x++) { //Left to right
      console.log(arr[y][x]);
    }
    topBound++;
    x--;y++;

    for(y = topBound; y < bottomBound; y++) { //Top to bottom
      console.log(arr[y][x]);
    }
    rightBound--;
    y--;
    x--;

    for(x; x >= leftBound; x--) { //Right to left
      console.log(arr[y][x]);
    }

    bottomBound--;
    y--;x++;

    for(y; y >= topBound; y--) { //Bottom to top
      console.log(arr[y][x]);
    }
    leftBound++;
    y++;
  }
}

/******************************************
 * TESTS
 ******************************************/

var arr1 = [
  [1,2,3],
  [4,5,6],
  [7,8,9]
];

//spiralArrayTraversal(arr1);
//
var arr2 = [
  [1,2,3],
  [4,5,6],
  [7,8,9],
  [10,11,12]
];

spiralArrayTraversal(arr2);

// var arr3= [[1,2,3,4],
//   [5,6,7,8],
//   [9,10,11,12],
//   [13,14,15,16]];
// spiralArrayTraversal(arr3);
