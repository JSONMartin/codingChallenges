// O(n) time complexity. This satisfies O(1) space complexity, because there can only be a maximum of 26 letters.
function firstNotRepeatingCharacter(s) {
    // Count characters
    const counter = {};
    for (const ch of s) {
        counter[ch] = (counter[ch] || 0) + 1;
    }

    // Iterate through string, looking for first non-repeating character
    for (const ch of s) {
        if (counter[ch] === 1) return ch;
    }

    return "_";
}

let res = firstNotRepeatingCharacter("abacabad")
res;