function processData(input) {
  let primeDict = {};
  input = input.split("\n");
  let resultStr = "";

  for(let x = 1; x < input.length; x++) {
    let val = parseInt(input[x]);
    if(val === 2) { resultStr+="Prime\n"; }
    else if(val <= 1 || val % 2 === 0) { resultStr+="Not prime\n"; }
    else if(val in primeDict) { resultStr += !primeDict[val] ? 'Prime\n' : 'Not prime\n'; }
    else {
      let isPrime = false;
      for(let i = 3; i < val / Math.sqrt(val); i+=2) {
        if(val % i === 0) {
          isPrime = true;
          break;
        } else {

        }
      }
      primeDict[val] = isPrime;
      resultStr += !isPrime ? 'Prime\n' : 'Not prime\n';
    }
  }

  console.log(resultStr.trim());
}

process.stdin.resume();
process.stdin.setEncoding("ascii");
_input = "";
process.stdin.on("data", function (input) {
  _input += input;
});

process.stdin.on("end", function () {
  processData(_input);
});
