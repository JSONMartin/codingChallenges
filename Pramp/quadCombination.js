// alex.romero@truecred.com
// jason.carter.martin@gmail.com
// json-ld
// https://www.youtube.com/watch?v=eWtOg3vSzxI

"use strict";

//var arr = [3, 7, 2, 8, 1, 9, 13, 6, 4, 12, 23];
var arr = [3, 1, 2, 8, 6, 9];
var S = 20;

// Are all the numbers unique? YES
// Negative numbers? YES
// Array is not Not sorted

// Input: arr
// Output: [idx] * 4 if result found, or null

// function quadCombination(arr, S) {

//    let subArr = [];

//    // Iterate through array and add values to subarray
//    for(let i = 0; i < arr.length; i++) {
//       if(subArr.length < 4) {
//          subArr.push(arr[i])
//       }
//       if(subArr.length === 4) {
//          // Check total
//          if( subArr.reduce((prev, cur) => prev+cur) === S ) {
//             //4 values are Equal to S
//             //Return indexes
//          }
//       }
//    }

//    let sumPairs = []
//    for(let i = 0; i < arr.length - 1; i+=2) {
//       sumPairs.push(arr[i] + arr[i + 1]);
//    }
// }
function quadCombination(arr, S) {
   const n = arr.length;
   if(!arr || !S || n < 4) return null;

   let pairHash = {};
   for(let i = 0; i <= n-1; i++) {
     for(let j = i + 1; j <= n-1; j++) {
        if(!pairHash[arr[i] + arr[j]]) pairHash[arr[i] + arr[j]] = [];
        pairHash[arr[i] + arr[j]].push([i, j])
     }
   }
   console.log(pairHash);

   for(let pairSum in pairHash) {
      if(pairHash[S-pairSum]) {
         let pairsA = pairHash[pairSum];
         let pairsB = pairHash[S - pairSum];
         let combination = find4Uniques(pairsA, pairsB);
         if(combination !== null) {
            return combination
         }
      }
   }
   return null;
}

function find4Uniques(A, B) {
   let lenA = A.length;
   let lenB = B.length;
   console.log("find4Uniques called");
   console.log("A:", A)
   console.log("B:", B)
   for(let i = 0; i < lenA; i++) {
      for(let j = 0; j < lenB; j++) {
         if(A[i][0] == B[j][0] || A[i][1] == B[j][1]
              ||
            A[i][0] == B[j][1] || A[i][1] == B[j][0]
           ) {
            continue;
         }
         else {
            return [A[i][0], A[i][1], B[j][0], B[j][1]];
         }
      }
   }
   return null;
}

let res = quadCombination([3, 1, 2, 8, 6, 9], 20)
console.log(res)
//arr = [3, 1, 2, 8, 6, 9];
//sumPairs = [4, 10, 15]
//var S = 20;
//
// function findArrayQuadCombination(arr, S):
//    if (arr == null OR S == null):
//       return null
//    n = length(arr)
//    if (n < 4):
//       return null
//    // hashing implementation language dependent:
//    pairHash = new HashTable()
//    for i from 0 to n-1
//       for j from i+1 to n-1
//          if !pairHash.isMapped(arr[i]+arr[j]):
//             pairHash.map(arr[i]+arr[j], [])
//          pairHash.get(arr[i]+arr[j]).push([i, j])
//
//    for pairSum in pairHash.getKeys()
//       if pairHash.isMapped(S - pairSum):
//          pairsA = pairHash.get(pairSum)
//          pairsB = pairHash.get(S - pairsSum)
//          combination = find4Uniques(pairsA, pairsB)
//          if (combination != null):
//             return combination
//    return null
//
// // Helper function.
// // Gets 2 arrays of sub-arrays of 2 numbers
// // Gets 4 unique numbers, from 2 sub-arrays of different arrays
// //The array is not sorted, and may hold any real number (positive, negative, zero, integer or fraction)
// function find4Uniques(A, B):
//    lenA = length(A)
//    lenB = length(B)
//    for i from 0 to lenA-1:
//       for j from 0 to lenB-1:
//          if ( A[i][0] == B[j][0] OR A[i][1] == B[j][1] OR
//               A[i][0] == B[j][1] OR A[i][1] == B[j][0] ):
//             continue
//          else:
//             return [A[i][0], A[i][1], B[j][0], B[j][1]]
//    return null
