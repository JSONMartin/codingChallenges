// https://leetcode.com/problems/pascals-triangle/#/description

/**
 * @param {number} numRows
 * @return {number[][]}
 */
const generate = (numRows) => {
    let triangle = [[1], [1, 1]]

    if (numRows <= 0) {
        return []
    }
    if (numRows - 1 <= 1) {
        return triangle.slice(0, numRows)
    }

    let i = 1
    while (i < numRows - 1) {
        let row = [], prevRow = triangle[i]

        for(let j = 0; j < prevRow.length - 1; j++) {
            row = [...row, prevRow[j] + prevRow[j + 1]]
        }

        triangle = [...triangle, [1, ...row, 1]]
        i++
    }

    return triangle
}


let res = generate(5)
console.log(res)