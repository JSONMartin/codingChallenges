const almostIncreasingSequence = (sequence, remaining = 1) => {
    if (remaining < 0) return false

    for (let i = 0; i < sequence.length - 1; i++) {
        if (sequence[i] >= sequence[i + 1]) {
            let removeFirstNumber = almostIncreasingSequence([...sequence.slice(0, i), ...sequence.slice(i + 1)], remaining - 1)
            let removeSecondNumber = almostIncreasingSequence([...sequence.slice(0, i + 1), ...sequence.slice(i + 2)], remaining - 1)
            return removeFirstNumber || removeSecondNumber
        }
    }

    return true
}

// TESTS

let res = almostIncreasingSequence([1, 2, 3, 4, 3, 6])
// let res = almostIncreasingSequence([1, 3, 2])
// let res = almostIncreasingSequence([1, 3, 2, 1])
// let res = almostIncreasingSequence([1, 2, 1, 2])
console.log(res);
