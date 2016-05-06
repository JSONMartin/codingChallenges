/**
 * Created by jsonmartin on 5/5/16.
 */
function longest_palindromic_substring(inputStr) {
  var longestLength = 0;

  function checkPalindrome(str) {
    if(str === str.split('').reverse().join('')) { // Match found
      longestLength = Math.max(str.length, longestLength);
    }
  }

  for(var i = 0; i < inputStr.length; i++) {
    for(var j = inputStr.length; j >= i; j--) {
      checkPalindrome(inputStr.substring(i, j));
    }
  }

  return longestLength;
}
/****
 * TESTS
 */

var result = longest_palindromic_substring("abba");
console.log(result);