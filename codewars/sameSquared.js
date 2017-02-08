// https://www.codewars.com/kata/550498447451fbbd7600041c/solutions/javascript

function comp(array1, array2){
  try {
    let squaredMap = {}, origMap = {};

    // Create counter objects to store value counts. Complexity: O(n)
    for (let n of array2) { squaredMap[n] = squaredMap[n] + 1 || 1; }
    for (let n of array1) { origMap[n] =  origMap[n] + 1 || 1; }

    // Check if squares of array1 are in array 2. Complexity: O(n)
    for (let n of array1) {
      if (!squaredMap[(n*n)]) { return false; }
      squaredMap[(n*n)] -= 1;
    }

    for (let n of array2) {
      if (!origMap[Math.sqrt(n)]) { return false; }
      origMap[Math.sqrt(n)] -= 1;
    }

    return true;
  } catch(e) {
    return false;
  }
}
