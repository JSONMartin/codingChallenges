function rotateImage(a) {
    let [row, col] = [a.length - 1, a.length - 1];
    let mid = Math.floor(a.length / 2);
    let bounds = 0;

    while (bounds < mid) {
        let counter = 0;

        while (counter <= (a.length - (2 * bounds) - 2)) { // Ensure the increased boundaries are respected on both sides to terminate
            let curNum = a[row - bounds][col - counter - bounds];

            // Swap to bottom left
            [curNum, a[row - bounds - counter][bounds]] = [a[row - bounds - counter][bounds], curNum];

            // Swap to upper left
            [curNum, a[bounds][counter + bounds]] = [a[bounds][counter + bounds], curNum];

            // Swap to upper right
            [curNum, a[counter + bounds][col - bounds]] = [a[counter + bounds][col - bounds], curNum];

            // Swap to lower right
            [curNum, a[row - bounds][col - counter - bounds]] = [a[row - bounds][col - counter - bounds], curNum];

            counter++;
        }

        bounds += 1;
    }

    return a;
}

// Tests //
// let res = rotateImage([[1,2,3],
//     [4,5,6],
//     [7,8,9]]);

let res = rotateImage([[10,9,6,3,7],
    [6,10,2,9,7],
    [7,6,3,8,2],
    [8,9,7,9,9],
    [6,8,6,8,2]]);

// let res = rotateImage([[40,12,15,37,33,11,45,13,25,3],
//     [37,35,15,43,23,12,22,29,46,43],
//     [44,19,15,12,30,2,45,7,47,6],
//     [48,4,40,10,16,22,18,36,27,48],
//     [45,17,36,28,47,46,8,4,17,3],
//     [14,9,33,1,6,31,7,38,25,17],
//     [31,9,17,11,29,42,38,10,48,6],
//     [12,13,42,3,47,24,28,22,3,47],
//     [38,23,26,3,23,27,14,40,15,22],
//     [8,46,20,21,35,4,36,18,32,3]])
console.log(res);