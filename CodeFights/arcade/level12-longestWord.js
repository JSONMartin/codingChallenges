const longestWord = text => text.match(/[a-zA-Z]*/g).sort((a, b) => b.length - a.length)[0]

// TESTS //

// let res = longestWord("Ready, steady, go!")
let res = longestWord("You are the best!!!!!!!!!!!! CodeFighter ever!")
console.log(res);