/**
 * Created by jsonmartin on 3/18/16.
 */
var moveZeros = function (arr) {
  var zerosArray = [];
  for(var i = 0; i < arr.length; i++) {
    if(arr[i] === 0) {
      arr.splice(i,1);
      zerosArray.push(0);
      i--;
    }
  }
  return arr.concat(zerosArray);
};

/******************************************
 * TESTS
 ******************************************/

console.log(moveZeros([1,2,0,1,0,1,0,3,0,1]));