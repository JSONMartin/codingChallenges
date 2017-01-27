/**
 * Created by jsonmartin on 3/20/16.
 */
"use strict";

function quickSort(array, start, end) {
  start = start || 0;
  var pivotValue = array[start];
  var leftMarker = start + 1;
  end = end || array.length - 1;

  if(start > array.length) {
    return;
  }
  if(end <= 1) {
    return;
  }

  if(end-start <= 0) {
    return;
  }

  var done = false;
  var lastSwapped;
  while(!done) {
    if(leftMarker >= end) { done = true; }

    while(leftMarker <= end) {
      if(array[leftMarker] > pivotValue ) {
        break;
      }
      else {
        leftMarker++;
      }
    }
    var rightMarker = leftMarker +1;
    if(rightMarker >= end) { done = true; }

    while(rightMarker <= end) {
      if(array[rightMarker] < pivotValue ) {
        break;
      }
      else {
        rightMarker++;
      }
    }
    
    if(rightMarker >= end || leftMarker >= end) { done = true; }

    if(array[leftMarker] > array[rightMarker]) {
      swap(array, leftMarker, rightMarker);
      lastSwapped = leftMarker;
    }
    leftMarker++;
  }

  if(!lastSwapped) {
    lastSwapped = end;
  }

  if(array[start] > array[lastSwapped]) {
    swap(array, start, lastSwapped);
  }

  quickSort(array, start, lastSwapped - 1);

  quickSort(array, (lastSwapped + 1));
  return array;

}

function swap(array, aIndex, bIndex) {
  var temp = array[aIndex];
  array[aIndex] = array[bIndex];
  array[bIndex] = temp;
}

/******************************************
 * TESTS
 ******************************************/

var res1 = quickSort([3,1,4,1,5,9,2,6,5,3]);
// console.log(res);
// console.log(results);

var res2 = quickSort([2,19,3,5,1,-3,2,500,63,193, -1005, 1058, -1, 234834, -20]);
// console.log(res);

var res3 = quickSort([15,14,13,12,11,10,9,8,7,6,5,4,3,2,1]);
console.log(res1, res2, res3);
