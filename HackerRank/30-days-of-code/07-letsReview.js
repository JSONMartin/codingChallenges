/**
 * Created by jsonmartin on 5/4/16.
 */
function processData(input) {
  input = input.split("\n");

  for(var i = 1; i <= parseInt(input[0]); i++) {
    var str = input[i];

    var strEven = "", strOdd = "";
    for(var j = 0; j < str.length; j+=2) {
      strEven+=str[j];
    }
    for(j = 1; j < str.length; j+=2) {
      strOdd+=str[j];
    }
    console.log(strEven + " " + strOdd);
  }

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
