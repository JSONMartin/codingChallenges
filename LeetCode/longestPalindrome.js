/**
 * Created by jmartin on 2/17/17.
 */

// https://leetcode.com/problems/longest-palindrome/

/*
 Given a string which consists of lowercase or uppercase letters, find the length of the longest palindromes that can be built with those letters.

 This is case sensitive, for example "Aa" is not considered a palindrome here.

 Note:
 Assume the length of given string will not exceed 1,010.

 Example:

 Input:
 "abccccdd"

 Output:
 7

 Explanation:
 One longest palindrome that can be built is "dccaccd", whose length is 7.
 */

/*
    Strategy:
    Count the amount of letters in the input.
    Loop through the counter object, and add each letter pair
    to the object.

    At the end, loop through the dictionary object again and
    if there is a character remaining, add one to the total.

    Time complexity: 3 linear passes, O(n)
 */

/**
 * @param {string} s
 * @return {number}
 */
var longestPalindrome = function(s) {
    let dict = {}, total = 0;

    for (let letter of s) { // Time Complexity: O(n)
        dict[letter] = dict[letter] + 1 || 1;
    }

    for (let letter in dict) { // Time Complexity: O(n)
        let letterCount = dict[letter];
        if (letterCount <= 1) continue;

        let amountToAdd = (letterCount % 2 === 0) ? letterCount : letterCount - 1;

        total += amountToAdd;
        dict[letter] -= amountToAdd;
    }

    for (let letter in dict) { // Time Complexity: O(n)
        let letterCount = dict[letter];

        if (letterCount === 1) {
            total++;
            break;
        }
    }

    return total;
};


// testing
longestPalindrome("abccccdd");