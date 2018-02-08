/*
There are n plants in a garden. Each of these plants has been added with some amount of pesticide. After each day, if any plant has more pesticide than the plant on its left, being weaker than the left one, it dies. You are given the initial values of the pesticide in each plant. Print the number of days after which no plant dies, i.e. the time after which there are no plants with more pesticide content than the plant to their left.

Input:

You are given an array which containsn integers, describing the array p where pi denotes the amount of pesticide in the plant i.

Output:

Output an integer equal to the number of days after which no plants die.

Sample input: Arr = [6 5 8 4 7 10 9]

Sample output: 2

Explanation:
Initially all plants are alive.

Plants = {(6,1), (5,2), (8,3), (4,4), (7,5), (10,6), (9,7)}

Plants[k] = (i,j) => jth plant has pesticide amount = i.

After the 1st day, 4 plants remain as plants 3, 5, and 6 die.

Plants = {(6,1), (5,2), (4,4), (9,7)}

After the 2nd day, 3 plants survive as plant 7 dies.

Plants = {(6,1), (5,2), (4,4)}

After the 3rd day, 3 plants survive and no more plants die.

Plants = {(6,1), (5,2), (4,4)}

After the 2nd day, the plants stop dying.

stacks
Contributed by Coder

*/
function passDay(arr) {
    let newResults = [arr[0]]
    for (let i = 1; i < arr.length; i++) {
        if (arr[i] <= arr[i-1]) newResults = [...newResults, arr[i]]
    }
    return newResults;
}

function solution(arr) {
    let count = 0;

    while(arr.length !== (arr = passDay(arr)).length) {
        count++;
    }

    return count;
}

let testArr =  [6, 5, 8, 4, 7, 10, 9]
let results = solution(testArr)
console.log(`Results:${results}`)