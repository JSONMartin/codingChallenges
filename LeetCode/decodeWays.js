/**
 * @param {string} s
 * @return {number}
 */
var numDecodings = function(s) {
    if (s.length === 0 || s.length === 1 && s !== '0') return s.length

    let dict = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

    let memo = {}
    let ways = []
    
    let recurse = (cur, remaining) => {
        console.log(memo)
        // Memoization
        const KEY = cur + '-' + remaining

        if (memo[KEY]) {
            console.log("Cache hit!")
            return memo[KEY]
        }
        // Base case
        if (remaining.length === 0) {
            memo[KEY] = cur
            ways.push(cur)
            return
        }

        let curNumSingleDigit = remaining[0]
        if (curNumSingleDigit !== '0') {
            let curNumSingleLetter = dict[curNumSingleDigit - 1]
            recurse(cur + curNumSingleLetter, remaining.slice(1))
            
            if (remaining.length >= 2) {
                let curNumDoubleDigit = remaining[0] + remaining[1]
                if (parseInt(curNumDoubleDigit) <= 26) {
                    let curNumDoubleLetter = dict[curNumDoubleDigit - 1]
            
                    recurse(cur + curNumDoubleLetter, remaining.slice(2))
                }
            }
        }
    }

    recurse('', s)

    console.log(ways)
    return ways.length
};




let test = "1791"
//let test = "4757562545844617494555774581341211511296816786586787755257741178599337186486723247528324612117156948"
//let test = "12"

let res = numDecodings(test)
console.log(res);