/**
 * Created by jsonmartin on 3/29/16.
 */
'use strict';
function arraySpiralTraversalRecursive(inputArray) {
  var results = [];

  function traverseArray(array) {
    var row;
    if(array.length <= 1) {
      array.forEach(function(row) {
        row.forEach(function(element) {
          results.push(element);
        });
      });
      return true;
    }
    //Shift off top row, add to results
    array.shift().forEach(function(element) {
      results.push(element);
    });

    //Pop off each last element from row going downwards, add each element to results
    for(var i = 0; i < array.length; i++) {
      row = array[i];
      results.push(row.pop());
    }

    //Pop off last row, and reverse, and add to results
    array.pop().reverse().forEach(function(element) {
      results.push(element);
    });

    //Shift off each element from row going upwards, add each element to results
    for(var i = array.length - 1; i >= 0; i--) {
      row = array[i];
      results.push(row.shift());
    }

    traverseArray(array.slice());
  }

  traverseArray(inputArray.slice());

  return results;
}

/******************************************
 * TESTS
 ******************************************/

// var arr1 = [
//   [1,2,3],
//   [4,5,6],
//   [7,8,9]
// ];
//
// var res = arraySpiralTraversalRecursive(arr1);
// console.log(res);

// var arr3= [[1,2,3,4],
//   [5,6,7,8],
//   [9,10,11,12],
//   [13,14,15,16]];
//
// var res = arraySpiralTraversalRecursive(arr3);
// console.log(res);

var arr2 = [
  [1,2,3],
  [4,5,6],
  [7,8,9],
  [10,11,12]
];

var res = arraySpiralTraversalRecursive(arr2);
console.log(res);
