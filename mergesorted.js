function mergesorted(a, b) {
  var result = [];

  while(a.length > 0 || b.length > 0) {
    if(a.length <= 0) { //Check if a is empty
      while(b.length > 0) {
        result.push(b.shift()); //If so, add rest of B to result array
      }
    }

    else if(b.length <= 0) { //Check if b is empty
      while(a.length > 0) {
        result.push(a.shift()); //If so, add rest of A to result array
      }
    }

    else if(a[0] <= b[0]) {
      result.push(a.shift());
    }
    else if(b[0] <= a[0]) {
      result.push(b.shift());
    }
  }

  return result;
}

/******************************************
 * TESTS
 ******************************************/

console.log(mergesorted([1,2],[3,4])); //should: [1,2,3,4]

console.log(mergesorted([1,2],[3])); //should: [1,2,3]

console.log(mergesorted([1],[2, 3])); //should: [1,2,3]