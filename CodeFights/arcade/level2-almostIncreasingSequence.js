// function almostIncreasingSequence(sequence, remaining = 1, maximum) {
//     if (remaining < 0) return false
//     else if (sequence.length === 1) return true

//     if (sequence[0] > sequence[1]) return almostIncreasingSequence(sequence.slice(1), remaining - 1, maximum)

//     maximum = sequence[0]
//     return sequence[1] > maximum && almostIncreasingSequence(sequence.slice(1), remaining, maximum)
// }

// // almostIncreasingSequence([1, 3, 2])
// let res = almostIncreasingSequence([1, 2, 1, 2])
// console.log(res);

const almostIncreasingSequence = (sequence) => {
    let skips = 1;

    for (let i = 0; i < sequence.length - 1; i++) {
        if (skips < 0) return false
        if (sequence[i] > sequence[i + 1]) {
            skips -= 1
        }
    }

    return true;
}