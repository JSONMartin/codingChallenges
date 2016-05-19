/**
 * Created by jsonmartin on 5/18/16.
 */
var position = (x, y, n) => y / x - (x - 1) / 2 + n; // Mathematical solution

function positionOrig(x, y, n) {
  let mid = parseInt(y / x);
  let total;
  let sum;
  do {
    total = [];
    for(let i = 0; i < x; i++) {
      total.push(mid + i);
    }
    sum = total.reduce((prev, cur) => prev + cur);
    if(sum > y) { mid--; } else { mid++; } // Adjusts next try up or down, based on if sum is above or below target
  } while(sum !== y);
  return total[n];
}