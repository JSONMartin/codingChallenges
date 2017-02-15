/**
 * @param {number} num
 * @return {boolean}
 */

// Accepted solution
const isUgly = num => {
    for (let divisor of [2, 3, 5]) {
        while (num && num % divisor === 0) {
            num /= divisor;
        }
    }

    return num === 1;
};

// Too slow solution
function getPrimes(n) {
    var listOfNum =range(n),
        i = 2;

    // CHeck only until the square of the prime is less than number
    while (i*i < n && i < n) {
        listOfNum = filterMultiples(listOfNum, i);
        i++;
    }

    return listOfNum;


    function range (num) {
        var res = [];
        for (var i = 2; i <= num; i++) {
            res.push(i);
        }
        return res;
    }

    function filterMultiples (list, x) {
        return list.filter(function (item) {
            // Include numbers smaller than x as they are already prime
            return (item <= x) || (item > x && item % x !== 0);
        });
    }
}

var isUglyTooSlowTLE = function(num) {
    let cache = {};

    var isPrime = function(num) {
        //console.log("Cache from isPrime:", cache);
        if (num in cache) return cache[num];

        if (num <= 2) {
            return cache[num] = true;
        }
        if (num % 2 === 0) {
            return cache[num] = false;
        }

        for (let i = 3; i <= Math.sqrt(num); i+=2) {
            if ( num % i === 0 ) {
                return cache[num] = false;
            }
        }

        return cache[num] = true;
    };

    if (num <= 0) { return false; }
    if (num >= 1 && num <= 6) { return true; }
    if (num === 7) { return false; }

    let primes = getPrimes(num / 2);
    console.log(primes);

    return primes.filter(n => (n !== 2 && n !== 3 && n !== 5) &&  (num/n) === parseInt(num/n) ).length == 0 && !isPrime(num);
};


//////////////
// TESTING
//////////////

//let res = isUgly(22);
//let res = isUgly(905391974);
//let res = isUgly(214797179);
let res = isUgly(1641249143);
//let res = isUgly(28);
console.log(res);