function processData(input) {
  let inputArr = input.split("\n");
  let d2 = inputArr[0].split(' ');
  let d1 = inputArr[1].split(' ');
  let fine = 0;
  if(d2[2] - d1[2] > 0) { fine = 10000; }
  else if(d2[1] - d1[1] > 0) { fine = (d2[1] - d1[1]) * 500; }
  else if(d2[0] - d1[0] > 0) { fine = (d2[0] - d1[0]) * 15; }
  console.log(fine);
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
