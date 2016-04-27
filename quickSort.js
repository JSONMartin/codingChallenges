/**
 * Created by jsonmartin on 3/19/16.
 */
"use strict";
function quickSort(inputArray) {

  var quickSortHelper = function(array, first, last) {
    console.log("quickSortHelper ran");
    if(first < last) {
      var splitPoint = partition(array, first, last);
      quickSortHelper(array, first, splitPoint-1);
      quickSortHelper(array, splitPoint+1, last);
    }
  };

  var partition = function(array, first, last) {
    console.log(array);
    var pivotValue = array[first];

    var leftPosition = first + 1;
    var rightPosition = last;

    var done = false;
    var temp;

    while(!done) {
      while(leftPosition <= rightPosition && array[leftPosition] <= pivotValue) {
        leftPosition++;
      }
      while(array[rightPosition] >= pivotValue && rightPosition >= leftPosition) {
        rightPosition--;
      }
      if(rightPosition < leftPosition) {
        done = true;
      }
      else {
        //swap(array, leftPosition, rightPosition);
        temp = array[leftPosition];
        array[leftPosition] = array[rightPosition];
        array[rightPosition] = temp;
      }
    }
    // swap(array, first, rightPosition);
    temp = array[first];
    array[first] = array[rightPosition];
    array[rightPosition] = temp;

    return rightPosition;
  };

  quickSortHelper(inputArray, 0, inputArray.length - 1);

  return inputArray;
}

/******************************************
 * TESTS
 ******************************************/

// function swap(array, a, b) {
//   console.log("swap called for:", a, b);
//   console.log(array);
//   var temp = array[a];
//   array[a] = array[b];
//   array[b] = temp;
//   return array;
// }

console.log(quickSort([54,26,93,17,77,31,44,55,20]));
// console.log(quickSort([8,1,5,14,4,15,12,6,2,11,10,7,9]));