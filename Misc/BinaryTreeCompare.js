/**
 * Created by jsonmartin on 3/18/16.
 */
function compare(a, b) {
  var isSame = false;
  function checkIfSame(a, b){
    // console.log("running for a:", a);
    // console.log("running for b:", b);
    if(!a && !b) { isSame = true; return isSame;}
    if(!a || !b) { isSame = false; return isSame;}
    if(a.val !== b.val) { isSame = false; return isSame;}
    if(a.val === b.val) {
      isSame = true;
      if(a.left) {
        if(b.left) {
          checkIfSame(a.left, b.left)
        }
        else {
          isSame = false;
        }
      }

      if(a.right) {
        if(b.right) {
          checkIfSame(a.right, b.right);
        }
        else {
          isSame = false;
        }
      }
    }
    return isSame;
  }
  checkIfSame(a,b);
  return isSame;
}

//or...

function compare2(a, b) {
  if (a === null || b === null) {
    return a === b;
  }
  return a.val === b.val && compare(a.left, b.left) && compare(a.right, b.right);
}


/******************************************
 * TESTS
 ******************************************/


var aNode =  { val: 0,
  left:
  { val: 1,
    left: { val: 2, left: null, right: null },
    right: null },
  right: null };
var bNode = { val: 0,
  left:
  { val: 1,
    left: { val: 2, left: null, right: null },
    right: null },
  right: null };

var results1 = compare(aNode, bNode);

console.log(results1);