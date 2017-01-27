/**
 * Created by jmartin on 1/26/17.
 */
/*
 You have an array of numbers.
 Your task is to sort ascending odd numbers but even numbers must be on their places.

 Zero isn't an odd number and you don't need to move it. If you have an empty array, you need to return it.

 Example

 sortArray([5, 3, 2, 8, 1, 4]) == [1, 3, 2, 8, 5, 4]
 */

// Functional Programming solution
function sortArray(array) {
    const isOdd = (x => x % 2 === 1);
    let odds = array.filter(isOdd).sort((a, b) => a > b);
    return array.map(el => isOdd(el) ? odds.shift() : el);
}

// Modified Bubble Sort solution
function sortArrayOriginalSolution(array) {
    let shouldCheckForSwaps = true;
    const isOdd = n => n % 2 === 1;

    while (shouldCheckForSwaps) {
        shouldCheckForSwaps = false;
        let curIdx = 0, nextIdx;

        while (curIdx < array.length - 1) {
            if (!isOdd(array[curIdx])) { curIdx++; }
            else {
                nextIdx = curIdx + 1;

                while (!isOdd(array[nextIdx]) && nextIdx < array.length) {
                    nextIdx++;
                }

                if (isOdd(array[nextIdx]) && array[curIdx] > array[nextIdx]) {
                    [array[curIdx], array[nextIdx]] = [array[nextIdx], array[curIdx]]; // Swap
                    shouldCheckForSwaps = true;
                }

                curIdx++;
            }
        }
    }

    return array;
}

// Tests

let res = sortArray([5, 3, 2, 8, 1, 4]) //== [1, 3, 2, 8, 5, 4]
console.log(res);