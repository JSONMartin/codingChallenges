const allLongestStrings = inputArray => {
    return inputArray.slice(1).reduce((prev, cur) => {
        if (cur.length > prev[0].length) return [cur]
        else if (cur.length === prev[0].length)  return [...prev, cur]
        return prev
    }, [inputArray[0]])
}

/// TESTS

// let inputArray = ["aba", "aa", "ad", "vcd", "aba"]
let inputArray = ["abc", "eeee", "abcd", "dcd"]
let res = allLongestStrings(inputArray)
console.log(res);