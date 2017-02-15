/**
 * Created by jmartin on 2/14/17.
 */
// https://www.codewars.com/kata/sum-without-highest-and-lowest-number/train/javascript

const sumArray = array => {
    try {
        return array.sort((a, b) => a - b).slice(1, - 1).reduce((prev, cur) => prev + cur);
    }
    catch(e) {
        return 0;
    }
};