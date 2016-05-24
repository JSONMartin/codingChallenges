/**
 * Created by jsonmartin on 5/23/16.
 */
function main() {
  var arr = [];
  for(let arr_i = 0; arr_i < 6; arr_i++){
    arr[arr_i] = readLine().split(' ');
    arr[arr_i] = arr[arr_i].map(Number);
  }

  let calculateHourglassSum = (row, col) => { // Input X,Y is the center coordinate
    return arr[row - 1][col - 1] + arr[row - 1][col] + arr[row - 1][col + 1] + // Top Row
      arr[row][col] + // Top Row
      arr[row + 1][col - 1] + arr[row + 1][col] + arr[row + 1][col + 1]; // Bot row
  };

  let maxSum = calculateHourglassSum(1, 1);

  for(let row = 1; row <= arr.length - 2; row++) {
    for(let col = 1; col <= arr[row].length - 2; col++) {
      maxSum = Math.max(calculateHourglassSum(row, col), maxSum);
    }
  }

  console.log(maxSum);
  return maxSum;
}