/**
 * Created by jmartin on 3/21/17.
 */
function generateCombinationsVariation(cur = [], results = []) {
    results.push(cur)

    if (cur[0] === 1) return results
    else {
        let newCombination = cur.slice();
        newCombination[0]--;
        newCombination.push(1);
        return generateCombinations(newCombination, results)
    }
}

// This will start with all 1s, and then converge both left and right to generate all combinations
// Doesn't come up with enough correct answers...
// function generateCombinations(cur = [], results = {}) {
//     //results.push(cur)
//     let resultsKey = cur.slice().sort().toString()
//
//     //if (resultsKey in results) return results
//
//     results[resultsKey] = results[resultsKey] ? [...results[resultsKey], cur.slice()] : [cur.slice()] //true
//
//     if (cur.length <= 1) return results
//
//     const left = cur[0], right = cur[cur.length - 1]
//     let leftCombo = cur.slice(1), rightCombo = cur.slice(0, cur.length - 1)
//
//     if (leftCombo) {
//         leftCombo[0] += left;
//         generateCombinations(leftCombo, results)
//     }
//     if (rightCombo) {
//         rightCombo[rightCombo.length - 1] += right
//         generateCombinations(rightCombo, results)
//     }
//
//     return results
// }

// function generateCombinations(cur = [], n) {
//     let combo = [];
//     let total = 0;
//
//     while (total < n) {
//         total+= cur.shift();
//     }
//
//     let result = [total, ...cur]
//
//     if (cur.length <= 1) generateCombinations(result, n - 1)
//     else generateCombinations(result, n)
// }

// function generateCombinations(n, arr, i) {
//     if (sumArr(arr) == n) {
//         //console.log(arr);
//         results.push(arr)
//     }
//     if (sumArr(arr) < n) {
//         for (let j = arr[i - 1]; j > 0; j--) {
//             arr[i] = j
//             generateCombinations(n, arr.slice(), i + 1)
//         }
//     }
//
// }
//
// function sum(num) {
//     // let startArray = Array(num).fill(1)
//     // let res = generateCombinations(startArray, num)
//     // console.log(res)
//     //
//     // console.log("Length:", Object.keys(res).length)
//
//     //let set = new Set(res);
//     //console.log("Set:", set);
//
//     let arr = Array(num).fill(0)
//
//     for (let i = num; i > 0; i--) {
//         arr[0] = i
//         generateCombinations(num, arr, 1)
//     }
// }

// function* sumGenerator(n) {
//     if (n == 0) {
//         yield []
//         return
//     }
//
//     let p = sum(n-1);
//     while (!p.done) {
//         yield [...p.value(), 1]
//
//         if (p.length < 2 || p[1] > p[0]) {
//             yield [p.value()[0] + 1, ...p.value().slice(1)]
//         }
//     }
//
//     // for (let p of sum(n-1)) {
//     //     yield [...p, 1]
//     //
//     //     if (p.length < 2 || p[1] > p[0]) {
//     //         yield [p[0] + 1, ...p.slice(1)]
//     //     }
//     // }
// }




// SCRATCH ABOVE
let callCount = 0;

// Works up to about 70, times out in codewars test
// const sumArr = arr => arr.reduce((prev, cur) => prev + cur)
//


// function generateCombinations(n, arr, i, results) {
//     callCount++
//     let total = sumArr(arr)
//     if (total > n) return
//
//     if (total == n) {
//         //console.log(arr)
//         //results.push(arr.slice().filter(x => x))
//         results.push(arr.slice())
//     }
//     if (total < n) {
//         for (let j = arr[i - 1]; j > 0; j--) {
//             arr[i] = j
//             generateCombinations(n, arr.slice(), i + 1, results)
//         }
//     }
//
// }


//
// function sum(num) {
//     if (num <= 0) return 0
//     let arr = Array(num).fill(0), results = []
//
//     for (let i = num; i > 0; i--) {
//         arr[0] = i
//         generateCombinations(num, arr, 1, results)
//     }
//
//     return results.length
// }

// MOST EFFICIENT VERSION below...
// Still times out, but really close.

const sumArr = arr => arr.reduce((prev, cur) => prev + cur)

function generateCombinations(n, arr, i, results, total) {
    //callCount++;
    if (total > n) return

    if (total == n) {
        results.push(arr.slice())
    }
    if (total < n) {
        for (let j = arr[i - 1]; j > 0; j--) {
            arr[i] = j
            let total = sumArr(arr)

            if (total > n) {
                continue;
            }
            else if (total == n) {
                results.push(arr.slice())
            }
            else {
                generateCombinations(n, arr.slice(), i + 1, results, total)
            }
        }
    }

}

function sum(num) {
    if (num <= 0) return 0
    let arr = Array(num).fill(0), results = []

    for (let i = num; i > 0; i--) {
        arr[0] = i
        generateCombinations(num, arr, 1, results, sumArr(arr))
    }

    return results.length
}

let res = sum(40)
// console.log(results);
// console.log(results.length);