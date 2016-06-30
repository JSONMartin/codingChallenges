/**
 * @param {number} num
 * @return {number}
 */
var addDigits = function(num) {
    let numStr = "" + num;
    let total = 0;

    if(numStr.length <= 1) {
        return num;
    }

    if(numStr.length > 1) {
        for(let i = 0; i < numStr.length; i++) {
            total+=parseInt(numStr[i]);
        }
        //console.log("Total:", total);
    }

    return addDigits(total);
};
