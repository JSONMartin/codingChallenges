/**
 * Created by jsonmartin on 3/28/16.
 */
function createSpiral(N) {
  var x = 0, y = 0; //Starting position
  var topBound = 0, rightBound = N, bottomBound = N, leftBound = 0;

  if(N < 1) { return []; }
  if(N === 1 ) { return [[N]]; }
  if(N % 1 !== 0 || typeof(N) !== "number") {
    return [];
  }

  var counter = 1;
  var results = new Array(N);
  for(var i = 0; i < N; i++) {
    results[i] = new Array(N);
  }

  while(topBound < bottomBound && leftBound < rightBound) {
    for(x = leftBound; x < rightBound; x++) { //Left to right
      results[y][x] = counter;
      counter++;
    }
    topBound++;
    x--;y++;

    for(y = topBound; y < bottomBound; y++) { //Top to bottom
      results[y][x] = counter;
      counter++;
    }
    rightBound--;
    y--;
    x--;

    for(x; x >= leftBound; x--) { //Right to left
      results[y][x] = counter;
      counter++;
    }

    bottomBound--;
    y--;x++;

    for(y; y >= topBound; y--) { //Bottom to top
      results[y][x] = counter;
      counter++;
    }
    leftBound++;
    y++;
  }

  return results;
}

let str = "";
createSpiral(5).forEach((row) => {
  row.forEach((num) => {
      str+=num + " ";
  });
  str+="\n";
});

//createSpiral(5).map((row))
