/**
 * Created by jsonmartin on 3/26/16.
 */
function permutations(string) {
  var stringArr = string.split(''); //Convert to array
  var results = [];

  function permutator(strArr) {
    var strArrStringified = strArr.slice().join(''); //Stringifies to push into results array
    if(results.indexOf(strArrStringified) === -1) { //If current permutation does not exist In results..
      results.push(strArr.slice().join('')); //Push first string that comes in
    }
    var char = strArr.shift(); //Remove the first character from the String Array
    for(var i = 1; i <= strArr.length; i++) {
      var newArr = strArr.slice(); //Creates a new copy of the array
      newArr.splice(i, 0, char); //Inserts the char into every diff position in the string

      var newArrStr = newArr.slice().join(''); //Converts back into a string
      if(results.indexOf(newArrStr) === -1) { //If the new permutation is not present in results...
        results.push(newArrStr); //Adds to result array
        permutator(newArr); //Calls permutator again with the new Version
      }
    }
  }

  permutator(stringArr);

  return results;
}

/******************************************
 * TESTS
 ******************************************/

var result = permutate('aabb');
console.log(result);