//let checkBracketCallCount = 0;

function checkBracket(str) {
    //checkBracketCallCount++;
    if (str.length < 2) return 0;
    console.log("Check bracket called with:", str);
    let bracketCount = 0;
    for (let x of str) {
        if (bracketCount < 0) return 0;
        else if (x === '(') {
            bracketCount++;
        }
        else if (x === ')') {
            bracketCount--;
        }
    }
    return bracketCount === 0 ? str.length : 0;
}

function findLongest(str) {
    let longest = 0, cache = {}, matches = [];

    // Find all '()' matches:
    for (let i = 0; i < str.length - 1; i++) {
        if (str[i] === '(' && str[i + 1] === ')') matches.push(i);
    }

    console.log(matches);

    for (let match of matches) {
        let l = (match - 1 < 0) ? 0 : match - 1;
        let r = (match + 2 >= str.length) ? str.length : match + ((l === 0) ? 3 : 2);
        while (l >= 0 && r <= str.length - 1) {
            console.log(match, l, r);
            let res = checkBracket(str.substring(l, r + 1));
            longest = Math.max(longest, res);
            console.log("Result for:", match, res);
            l++; r++;
        }

    }


    //console.log(startingPos);

    // for (let i = 0; i < str.length; i++) {
    //     let substr = str.substring(0, i);
    //
    //     let res = (substr in cache) ? cache[substr] : (cache[substr] = checkBracket(substr));
    //
    //     //console.log("checkBracket res:", res);
    //     if (checkBracket(substr)) {
    //         //return substr.length;
    //         longest = Math.max(longest, res);
    //     }
    // }
    return longest > 0 ? longest : ((matches.length >= 1) ? 2 : 0);
}

function findLongestOld(str) {
    let longest = 0, cache = {};
    let startingPos = str.indexOf('(');

    for (let i = startingPos; i < str.length; i++) {
        for (let j = str.length; j >= i; j--) {
            let substr = str.substring(i, j);
            //let res = checkBracket(substr);

            // if (substr in cache) {
            //     //console.log("cache HIT!");
            // }
            let res = (substr in cache) ? cache[substr] : (cache[substr] = checkBracket(substr));

            //console.log("checkBracket res:", res);
            if (checkBracket(substr)) {
                //return substr.length;
                longest = Math.max(longest, res);
            }
        }

    }
    return longest;
}




// function findLongest(str){
//     let longest = 0, cur = 0, bracketCount = 0, longestBracketCount = 0, idx = 0;
//
//     for (let x of str) {
//         if (x === '(') {
//             bracketCount++;
//         }
//         else if (x === ')' && bracketCount > 0) {
//             bracketCount--;
//             cur+=2;
//         }
//         else {
//             console.log("resetting at:", idx, "Brakcet Count:", bracketCount);
//             longestBracketCount = Math.max(longestBracketCount, bracketCount);
//             bracketCount = 0;
//             longest = Math.max(longest, cur);
//             cur = 0;
//         }
//
//         console.log(x, longest, cur, bracketCount);
//
//         idx++;
//     }
//
//     longestBracketCount = Math.max(longestBracketCount, bracketCount);
//
//     console.log("Ending bracket count", bracketCount);
//     console.log("longestBracket bracket count", longestBracketCount);
//
//     //if (bracketCount === 0)
//     longest = Math.max(longest, cur);
//
//
//     return longest - longestBracketCount;
// }


//let res = findLongest("())(()))");
let res = findLongest("()");
//console.log("checkBracketCallCount:", checkBracketCallCount);
//let res = findLongest("(()()())");

console.log(res);