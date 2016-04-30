/**
 * Created by jsonmartin on 4/29/16.
 */
function processData(input) {
  input = input.split('\n');
  var cost = parseFloat(input[0]), tip = parseFloat(parseFloat(input[1])/100), tax = parseFloat(parseFloat(input[2])/100);
  var total = Math.round(cost + cost*tip + cost*tax);
  console.log("The total meal cost is " + total + " dollars.")
  return total;
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
