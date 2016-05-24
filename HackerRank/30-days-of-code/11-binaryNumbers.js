/**
 * Created by jsonmartin on 5/23/16.
 */
function main() {
  var n = parseInt(readLine());

  let binary = n.toString(2);
  let maxOnes = 0;
  let curOnes = 0;

  for(let i = 0; i < binary.length; i++) {
    if(binary[i] === "1") {
      curOnes++;
    } else {
      maxOnes = Math.max(maxOnes, curOnes);
      curOnes = 0;
    }
  }

  let result = Math.max(maxOnes, curOnes);
  console.log(result);
}