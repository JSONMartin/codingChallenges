// https://www.codewars.com/kata/anagram-detection/train/javascript
/*
 An anagram is the result of rearranging the letters of a word to produce a new word. (Ref wikipedia).

 Note: anagrams are case insensitive

 Examples

 foefet is an anagram of toffee
 Buckethead is an anagram of DeathCubeK
 The challenge is to write the function isAnagram (or is_anagram in Python) to return true if the word test is an
 anagram of the word original and false otherwise. The function prototype is as given below:

 var isAnagram = function(test, original) {
 };

 */
const _ = require('lodash');

const isAnagram = (test, original) => {
    const originalWordCount = {}, testWordCount = {};

    for (let letter of original.toUpperCase()) {
        originalWordCount[letter] = (originalWordCount[letter] + 1) || 1 ;
    }

    for (let letter of test.toUpperCase()) {
        testWordCount[letter] = (testWordCount[letter] + 1) || 1 ;
    }

    return _.isEqual(testWordCount, originalWordCount);
};


// Tests
let res = isAnagram("foefet", "toffee");
console.log(res);

// Helper Methods
function print() {
    [...arguments].map(function (arg) {
        console.log(arg);
    });
}

function printSeperator() {
    console.log("------------------------------");
}
