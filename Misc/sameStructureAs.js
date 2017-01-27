/**
 * Created by jsonmartin on 4/24/16.
 */
Array.prototype.sameStructureAs = function (other) {
  if(!Array.isArray(other)) { return false; }
  console.log("Calling with this:", this);
  console.log("Calling with other:", other);
  //Iterate through this array, comparing each element with other
  for(var i = 0; i < this.length; i++) {
    if(Array.isArray(this[i]) !== Array.isArray(other[i])) {
      return false;
    }
    if(Array.isArray(this[i]) && Array.isArray(other[i])) {
      if(this[i].length !== other[i].length) {
        return false; //If invalid match found, return false
      } else {
        return this[i].sameStructureAs(other[i]);
      }
    }
  }
  return true;
};

/******************************************
 * TESTS
 ******************************************/

var a1 = [1, 2, 3];
var a2 = [2, 4, 5];
var a3 = [[1], [2], [3]];

a1.sameStructureAs(a2);

//console.log (("this is foo bar".match(/o/g)||[]).length);

