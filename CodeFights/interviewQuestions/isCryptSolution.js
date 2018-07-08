function isCryptSolution(crypt, solution) {
    try {
        const convertWordToMapping = word => word.split('').map(letter => solutionMap[letter] || letter).join('')

        const solutionMap = {}
        for (let mapping of solution) {
            solutionMap[mapping[0]] = mapping[1]
        }

        const [word1, word2, word3] = [convertWordToMapping(crypt[0]), convertWordToMapping(crypt[1]), convertWordToMapping(crypt[2])]
        return [word1, word2, word3].every(word => word.length === 1 || !word.startsWith(0)) && Number(word1) + Number(word2) === Number(word3)
    } catch(e) {
        return false
    }
}

/* TESTS */
let crypt = ["SEND",
"MORE",
"MONEY"]
let solution = [["O","0"],
["M","1"],
["Y","2"],
["E","5"],
["N","6"],
["D","7"],
["R","8"],
["S","9"]]
// let res = isCryptSolution(crypt, solution) // => True

crypt = ["TEN",
"TWO",
"ONE"]
solution = [["O","1"],
["T","0"],
["W","9"],
["E","5"],
["N","4"]]
let res = isCryptSolution(crypt, solution) // => False
res