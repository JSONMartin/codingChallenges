function getCount(words) {
  //debugger;
  var count = {
    vowels: 0,
    consonants: 0
  }

  for(var i = 0; i < words.length; i++) {
    if(isVowel(words[i])) { count[vowels]++; }
  }

  var isVowel = function(char) {
    if(char.toUpperCase() === 'A' || char.toUpperCase() === 'E' || char.toUpperCase() === 'I' || char.toUpperCase() === 'O' || char.toUpperCase() === 'U' ) {
      return true;
    }
    return false;
  };

  return count;
}

/******************************************
 * TESTS
 ******************************************/

var test = getCount("abc");
console.log(test);