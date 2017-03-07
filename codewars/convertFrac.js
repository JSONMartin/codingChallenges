/**
 * Created by jmartin on 2/16/17.
 */
// https://www.codewars.com/kata/54d7660d2daf68c619000d95/train/javascript (5 Kyu)

// Euclid's algorithm:
//  1. a % b -> c
//  2. b % c -> d
//  3. c % d -> e
//  ...
// If any results in 0, divisor is GCD
function leastCommonMultiple(x, y) {
    let gcd = x, tmp = y;

    while (tmp !== 0) {
        [gcd, tmp] = [tmp, gcd % tmp];
    }

    return x * (y / gcd);
}


function convertFrac(lst){
    console.log("lst:", lst);

    let min = Math.min(...lst.map(tuple => tuple[1])),
        max = Math.max(...lst.map(tuple => tuple[1])),
        denominator = lst.reduce((prev, cur) => prev * cur[1], 1),
        leastCommonDenominator = denominator;

    // Calculate leastCommonDenominator
    for (let i = max; i < denominator; i++) {
        let allPass = true;

        for (let tuple of lst) {
            if (i % tuple[1] !== 0) { allPass = false; }
        }

        if (allPass) {
            leastCommonDenominator = i;
            break;
        }
    }

    let resultStr = "";

    lst.forEach(tuple => {
        tuple[0] = (leastCommonDenominator / tuple[1]) * tuple[0];
        tuple[1] = leastCommonDenominator;

        resultStr += `(${tuple[0]},${tuple[1]})`;
    });

    return resultStr;
}


/****************************************
 *               Testing
 ****************************************/
const Test = require('./TESTING.js');


var lst = [ [1, 2], [1, 3], [1, 4] ];
//var lst = [ [ 6, 13 ], [ 187, 1310 ], [ 31, 41 ] ];
Test.assertEquals(convertFrac(lst), "(6,12)(4,12)(3,12)");