/**
 * Created by jmartin on 1/12/17.
 */
// https://www.codewars.com/kata/546e2562b03326a88e000020/train/javascript

function squareDigits(num){
    let result = "";

    for (let n of (""+num)) {
        result += ""+Math.pow(parseInt(n), 2);
    }

    return parseInt(result);
}

/*
TESTING
 */

let res = squareDigits(9119); // => 811181
console.log(res);