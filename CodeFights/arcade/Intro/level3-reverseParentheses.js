/*
For string s = "a(bc)de", the output should be
reverseParentheses(s) = "acbde".
*/

const reverseParentheses = inputStr => {
    let regex = /\(([^()]+\))/g;
    let resultStr = inputStr;
    let match;

    // Check for the inner most parenthesis, reverse the content inside, then move out to the next set of parenthesis
    while(match = resultStr.match(regex)) {
        let matchStr = match[0]
        resultStr = resultStr.replace(matchStr, matchStr.slice(1, -1).split('').reverse().join(''))
    }

    return resultStr;
}

//// TESTS
// let testStr = "a(bc)de"
let testStr = "a(bcdefghijkl(mno)p)q"
let res = reverseParentheses(testStr)
console.log(res);