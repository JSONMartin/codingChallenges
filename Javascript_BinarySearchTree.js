function BinarySearchTree() {

  var Node = function(key){ //{1}
    this.key = key;
    this.left = null;
    this.right = null;
  };

  var root = null; //{2}

  this.insert = function(key) {
    var newNode = new Node(key);
    if(!root) {
      root = newNode;
    } else {
      traverse(root);
    }

    function traverse(curNode) {
      if(key < curNode.key) {
        if(!curNode.left) {
          curNode.left = newNode;
          return true;
        } else {
          traverse(curNode.left);
        }
      } else {
        if(!curNode.right) {
          curNode.right = newNode;
          return true;
        } else {
          traverse(curNode.right);
        }
      }
    }
  };

  this.min = function() {
    var checkLeft = function(node) {
      if(!node.left) {
        return node.key;
      } else {
        return checkLeft(node.left);
      }
    };
    return checkLeft(root);
  };

  this.max = function() {
    var checkRight = function(node) {
      if(!node.right) {
        return node.key;
      } else {
        return checkRight(node.right);
      }
    };
    return checkRight(root);
  };

  this.inOrderTraverse = function(cb) {
    var inOrderTraverseNode = function(node, cb) {
      if(node) {
        inOrderTraverseNode(node.left, cb);
        cb(node);
        inOrderTraverseNode(node.right, cb);
      }
    };
    inOrderTraverseNode(root, cb);
  };

  this.preOrderTraverse = function(cb) {
    var inOrderTraverseNode = function(node, cb) {
      if(node) {
        cb(node);
        inOrderTraverseNode(node.left, cb);
        inOrderTraverseNode(node.right, cb);
      }
    };
    inOrderTraverseNode(root, cb);
  };

  this.postOrderTraverse = function(cb) {
    var inOrderTraverseNode = function(node, cb) {
      if(node) {
        inOrderTraverseNode(node.left, cb);
        inOrderTraverseNode(node.right, cb);
        cb(node);
      }
    };
    inOrderTraverseNode(root, cb);
  };

  this.search = function(key){
    return searchNode(root, key);
  };

  var searchNode = function(node, key) {
    if(node.key === key) { return true; }

    if(key < node.key) {
      if(node.left) {
        return searchNode(node.left, key);
      }
    } else {
      if(node.right) {
        return searchNode(node.right, key);
      }
    }
    return false;
  };

  this.print = function() {
    console.dir(root);
  };
}

function printNode(node) {
  console.log(node.key);
}


/******************************************
 * TESTS
 ******************************************/

var bst = new BinarySearchTree();
bst.insert(11);
//bst.print();
bst.insert(7);
bst.insert(15);
//bst.print();
bst.insert(5);

bst.insert(9);
bst.insert(13);
bst.insert(20);

bst.insert(4);
bst.insert(6);
//bst.print();
bst.inOrderTraverse(printNode);

console.log("MIN:" + bst.min());
console.log("Max:" + bst.max());
console.log("Search 11:", bst.search(11));
console.log("Search 12:", bst.search(12));
console.log("Search 6:", bst.search(6));
console.log("Search 13:", bst.search(13));
console.log("Search 1:", bst.search(1));