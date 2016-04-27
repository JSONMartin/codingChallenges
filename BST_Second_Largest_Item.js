function BinaryTreeNode(value) {
  this.value = value;
  this.left  = null;
  this.right = null;
}

BinaryTreeNode.prototype.insertLeft = function(value) {
  this.left = new BinaryTreeNode(value);
  return this.left;
};

BinaryTreeNode.prototype.insertRight = function(value) {
  this.right = new BinaryTreeNode(value);
  return this.right;
};

BinaryTreeNode.prototype.secondLargest = function() {
  var stack = [];

  var curNode = this;
  stack.push(curNode);

  while(curNode.right) { //Traverse down the right side until last element.
    curNode = curNode.right;
    stack.push(curNode);
  }

  if(curNode.left) { //If last element has a left side...
    curNode = curNode.left;
    if(!curNode.right) { //If there is no right side, return value
      return curNode.value;
    } else {
      while(curNode.right) {
        curNode = curNode.right;
        return curNode.value;
      }
    }
  } else { //Otherwise, return the previous element
    stack.pop();
    return stack.pop().value;
  }
};


/*
Interview Cake solution
 */

function findLargest(rootNode) {
  var current = rootNode;
  while (current) {
    if (!current.right) return current.value;
    current = current.right;
  }
}

/******************************************
 * TESTS
 ******************************************/

function findSecondLargest(rootNode) {
  if (!rootNode.left && !rootNode.right) {
    throw new Error('Tree must have at least 2 nodes');
  }

  var current = rootNode;

  while (current) {
    // case: current is largest and has a left subtree
    // 2nd largest is the largest in that subtree
    if (current.left && !current.right) {
      return findLargest(current.left);
    }

    // case: current is parent of largest, and
    // largest has no children, so
    // current is 2nd largest
    if (current.right &&
      !current.right.left &&
      !current.right.right) {
      return current.value;
    }

    current = current.right;
  }
}

/****
 * TRY ONE — second largest (13) — CORRECT!
 */

var bst = new BinaryTreeNode(8);
var three = bst.insertLeft(3);
three.insertLeft(1);
var six = three.insertRight(6);
six.insertLeft(4);
six.insertRight(7);

var ten = bst.insertRight(10);
ten.insertRight(14).insertLeft(13);

console.dir(bst);

var secondLargest = bst.secondLargest();
console.log("Second Largest:", secondLargest);


/****
 * TRY TWO — second largest (21) — CORRECT!
 */

// var bst = new BinaryTreeNode(5);
// var two = bst.insertLeft(2);
// two.insertLeft(-4);
// two.insertRight(3);
//
// var twentyOne = bst.insertRight(21);
// twentyOne.insertLeft(19);
// twentyOne.insertRight(25);
//
// console.dir(bst);
//
// var secondLargest = bst.secondLargest();
// console.log("Second Largest:", secondLargest);


/****
 * TRY THREE : Value (11) - correct!
 */

// var bst = new BinaryTreeNode(5);
// var three = bst.insertLeft(3);
// three.insertLeft(1);
// three.insertRight(4);
//
// var eight = bst.insertRight(8);
// eight.insertLeft(7);
// var twelve = eight.insertRight(12);
//
// var ten = twelve.insertLeft(10);
// ten.insertLeft(9);
// ten.insertRight(11);
//
//
// console.dir(bst);
//
// var secondLargest = bst.secondLargest();
// console.log("Second Largest:", secondLargest);