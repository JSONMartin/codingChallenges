/**
 * Created by jsonmartin on 4/20/16.
 */

function muddle(basil_factor) {
  var t1 = 0;
  var t2 = 1;
  while(t2 < basil_factor) {
    if(Math.floor(Math.random() * (t2 + 1)) == 0) {
      t1 = t2;
    }
    t2++;
  }
  console.log(t1);
  console.log(t2);
  return t1;
}

console.log( muddle(150) );