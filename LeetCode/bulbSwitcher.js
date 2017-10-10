/**
 * @param {number} n
 * @return {number}
 */

// Math solution: Only perfect squares count!
 var bulbSwitch = function(n) {
    let i = 0
    while (Math.pow(i, 2) <= n) {
        i++
    }
    return i - 1
};

 // Works, but TLE
var bulbSwitch = function(n) {
    try {
        let bulbArray = Array.from({length:n}).fill(false)
        let increment = 1
        
        while (increment <= n) {
            for (let i = increment - 1; i < n; i += increment) {
                bulbArray[i] = !bulbArray[i]
            }
            // console.log(bulbArray)
            increment++
        }
        
        let totals = bulbArray.reduce((prev, cur) => prev + cur, 0)
        // console.log("Totals:", totals)
        return totals
    } catch(e) {
        return 0
    }
};

bulbSwitch(1000000)