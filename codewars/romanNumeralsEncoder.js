/**
 * Created by jmartin on 1/11/17.
 */
// https://www.codewars.com/kata/51b62bf6a9c58071c600001b/train/javascript

/*
 Create a function taking a positive integer as its parameter and
 returning a string containing the Roman Numeral representation
 of that integer.

 Modern Roman numerals are written by expressing each digit separately
 starting with the left most digit and skipping any digit with a
 value of zero.
 In Roman numerals 1990 is rendered:
 1000=M, 900=CM, 90=XC; resulting in MCMXC.
 2008 is written as 2000=MM, 8=VIII; or MMVIII.
 1666 uses each Roman symbol in descending order: MDCLXVI.

 Example:

 solution(1000); // should return 'M'
 Help:

 Symbol    Value
 I          1
 V          5
 X          10
 L          50
 C          100
 D          500
 M          1,000
 */
const solution = number =>{
    const dict = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }, romanNumeralOrder = ['M', 'D', 'C', 'L', 'X', 'V', 'I'];

    let solution = '';

    const calc = (key, val) => {
        while(number > 0 && number >= val - Math.ceil(val / 10)) {
            if (number < val) {
                let prevNumeral = "";
                for (let k in dict) {
                    if (dict[k] === (Math.ceil(val / 10))) {
                        prevNumeral = k;
                    }
                }
                solution += prevNumeral + key;
                number -= (val - (Math.ceil(val / 10)));
            }
            else {
                solution += key;
                number -= val;
            }
        }
    };

    for (let key of romanNumeralOrder) {
        try {
            calc(key, dict[key])
        }
        catch(e) {
            calc(key, dict[key])
        }

    }

    return solution;
};


// TESTING
let res = solution(1666);
console.log(res);