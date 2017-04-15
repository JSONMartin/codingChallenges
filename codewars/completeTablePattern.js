/*
If rows = 4 and columns = 4 , str = "Hello World!"
The pattern should be a 4x4 table like this:
+---+---+---+---+
| H | e | l | l |   From left to right
+---+---+---+---+
| o |   | W | o |   and from top to bottom
+---+---+---+---+
| r | l | d | ! |   each row separated by "\n"
+---+---+---+---+
|   |   |   |   |
+---+---+---+---+
*/
function pattern(rows,columns,str) {
    const matrix = new Array(rows).fill(null).map(() => Array(columns).fill(' '))
    let i = 0, curCol = 0, curRow = 0

    while (i < str.length) {
        if (curCol >= columns) {
            curCol = 0; curRow += 1
        }
        matrix[curRow][curCol] = str[i]
        curCol++
        i++
    }

    let result = ''
    let border = "+" + "---+".repeat(columns)

    for (let row of matrix) {
        result += border + "\n"
        for (let col of row) {
            result += `| ${col} `
        }
        result += "|\n"
    }
    result += border

    return result
}
// TESTS
let res = pattern(4, 4, "Hello World!")
console.log(res)