/**
 * Created by jmartin on 1/12/17.
 */
// https://www.codewars.com/kata/removing-elements/train/javascript

function removeEveryOther(arr) {
    let result = [];

    for (let i = 0; i < arr.length; i+=2) {
        result.push(arr[i]);
    }

    return result;
}