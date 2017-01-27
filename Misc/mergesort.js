/**
 * Created by jsonmartin on 3/15/16.
 */
function mergeSort(inputArr) {
  var sortArray = function(array) {

    if(array.length === 1) {
      return [array[0]];
    }

    if(array.length >= 2) {

      var midpoint;
      var lHalf;
      var rHalf;

      if(array.length % 2 === 0) {
        lHalf = array.slice(0, (array.length/2));
        rHalf = array.slice((array.length/2), array.length);
      }
      else {
        midpoint = Math.round((array.length-1)/2); //calculate midpoint
        lHalf = array.slice(0, midpoint+1);
        rHalf = array.slice(midpoint+1, array.length);
      }

      var left = sortArray(lHalf);
      var right = sortArray(rHalf);

      var rtnArr = [];
      while(left.length > 0 || right.length > 0) {

        if(left && right && left[0] <= right[0]) {
          rtnArr.push(left.shift());
        }
        else if(left && right && left[0] > right[0]) {
          rtnArr.push(right.shift());
        }
        else {
          while(left && left.length > 0) {
            rtnArr.push(left.shift());
          }

          while(right && right.length > 0) {
            rtnArr.push(right.shift());
          }
        }
      }
      return rtnArr;
    }
  };

  var results = (sortArray(inputArr));
  return results;
}

/******************************************
 * TESTS
 ******************************************/

var test1 = mergeSort([38,27,43,3,9,82,10]);
//var test1 = mergeSort([38,27,43,3,9,82,10, 11]);
console.log(test1);
