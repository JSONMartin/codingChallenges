/**
 * Created by jsonmartin on 3/29/16.
 */
/*
 A Node has the following properties:
 var data; // A number or string.
 Node left; // Undefined if there is no left child.
 Node right; // Undefined if there is no right child.
 */

// 1.) Root node, 2.) traverse left subtree, 3.) traverse right subtree.
function preOrder(node) {
  var results = [];
  function checkOrder(node) {
    results.push(node.data);
    if(node.left) {
      checkOrder(node.left);
    }
    if(node.right) {
      checkOrder(node.right);
    }
  }
  checkOrder(node);
  return results;
}

// 1.) Traverse left subtree, 2.) root node, 3.) traverse right subtree.
function inOrder(node) {
  var results = [];

  function checkOrder(node) {
    if(node.left) {
      checkOrder(node.left);
    }
    results.push(node.data);
    if(node.right) {
      checkOrder(node.right);
    }
  }
  checkOrder(node);
  return results;
}

// 1.) Traverse left subtree, 2.) traverse right subtree, 3.) root node.
function postOrder(node) {
  var results = [];

  function checkOrder(node) {
    if(node.left) {
      checkOrder(node.left);
    }
    if(node.right) {
      checkOrder(node.right);
    }
    results.push(node.data);
  }
  checkOrder(node);
  return results;
}

/******************************************
 * TESTS
 ******************************************/

function Node(data) {
  this.data = data; // A number or string.
  this.left = null; this.right = null;
}

var a = new Node(5);
var b = new Node(10);
var c = new Node(2);
a.left = b;
a.right = c;

var results = preOrder(a);
console.log(results);