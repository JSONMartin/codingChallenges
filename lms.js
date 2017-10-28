console.time("RUN-TIME");

function findLastManStanding(n) {
    // where n = length of array
    var arr = Object.keys(new Int8Array(n+1)).map(Number).slice(1);
    var list = [], c = 0, index = 0;
    do {
        if (index > arr.length) {
            do {
                index -= arr.length;
            } while (index >= arr.length);
        }
        
        list.push(arr.splice(index,1));
        c++;
        index += c;
    } while (arr.length > 0);
    console.log('Last man standing is ', list[list.length-1]);
    console.log('Order of removal: ' + list.join(', '));
}
findLastManStanding(10000);

console.timeEnd("RUN-TIME");