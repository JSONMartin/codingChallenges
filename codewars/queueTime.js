// https://www.codewars.com/kata/57b06f90e298a7b53d000a86/solutions/javascript

function queueTime(customers, n) {
    if (customers.length <= 0) return 0;
    if (n > customers.length) return Math.max(...customers);

    let checkStandList = new Array(n);

    let totalTime = 0, customersPosition = 0;

    while (customersPosition < customers.length) {
        // Fill empty checker lines
        for (let checkerIdx = 0; checkerIdx < n; checkerIdx++) {
            if (checkStandList[checkerIdx]) continue;
            checkStandList[checkerIdx] = customers[customersPosition++] || 0;
        }

        // Process checkers
        let minTime = Math.min(...checkStandList);
        checkStandList = checkStandList.map(c => isNaN(c) ? 0 : c - minTime);
        totalTime += minTime;
    }

    return totalTime + Math.max(...checkStandList);
}



//////
// TESTS
//////

// Test.describe("example tests", function() {
//     Test.assertEquals(queueTime([], 1), 0);
//     Test.assertEquals(queueTime([1,2,3,4], 1), 10);
//     Test.assertEquals(queueTime([2,2,3,3,4,4], 2), 9);
//     Test.assertEquals(queueTime([1,2,3,4,5], 100), 5);
//
// //add some more example tests here, if you like
//
// });

/*
 queueTime([5,3,4], 1)
 // should return 12
 // because when n=1, the total time is just the sum of the times

 queueTime([10,2,3,3], 2)
 // should return 10
 // because here n=2 and the 2nd, 3rd, and 4th people in the
 // queue finish before the 1st person has finished.

 queueTime([2,3,10], 2)
 // should return 12
 */

//let res = queueTime([5,3,4], 1);
//let res = queueTime([2,3,10], 2);
let res = queueTime([12,3,19,17,5,15,7,11,4,16,14,15,14,19,8,2,11,14,2,15,8,18,16,12,10,14,1,13,2,11,3,5,15,8,5,9,7,9,16,8,5,8,4,6,18,9,19,5,9,19,3,1,19,5,20,14,3,6,14,14,12,4,7,14,8,20,17,8,9,19,1,8,12,17,11,4,3,10,20,6,14,1,3,11,16,8,5], 20);
console.log(res);
