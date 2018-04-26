function isValidCoordinates(coordinates){
    debugger;

    try {
        let matches = coordinates.match(/(^.*), (.*$)/).slice(1);
        let [latitude, longitude] = matches.map(n => isNaN(n) || /[a-zA-Z]/g.test(n) ? Infinity : parseFloat(n));
        console.log(latitude, longitude);
        return matches.length === 2 && (-90 <= latitude && latitude <= 90) && (-180 <= longitude && longitude <= 180)
    } catch(e) {
        return false;
    }
}


// var ValidCoordinates = [
//     "-23, 25",
//     "4, -3",
//     "24.53525235, 23.45235",
//     "04, -23.234235",
//     "43.91343345, 143"
//   ];

// console.log(isValidCoordinates(ValidCoordinates[0]));

// for( i in ValidCoordinates ) {
//   console.log(isValidCoordinates(ValidCoordinates[i]), ValidCoordinates[i]);
// }

var InvalidCoordinates = [
    // "23.234, - 23.4234",
    // "2342.43536, 34.324236",
    // "N23.43345, E32.6457",
    // "99.234, 12.324",
    // "6.325624, 43.34345.345",
    // "0, 1,2",
    // "0.342q0832, 1.2324",
    "23.245, 1e1"
  ];
// for( i in InvalidCoordinates ) {
//     console.log(isValidCoordinates(ValidCoordinates[i]), ValidCoordinates[i]);
// }
console.log(isValidCoordinates(InvalidCoordinates[0]));