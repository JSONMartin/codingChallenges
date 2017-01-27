/**
 * Created by jsonmartin on 4/10/16.
 */
function Node(value) {
  this.value = value;
  this.next = null;
}

function loop_size(node){
  var visited = [];
  var done = false;

  while(!done) {
    if(visited.indexOf(node) > -1) { // If node has already been visited
      done = true;
    } else {
      visited.push(node);
    }
    node = node.next;
  }

  var refNode = node;
  node = node.next;
  var count = 1;

  while(node !== refNode) {
    count++;
    node = node.next;
  }

  return count;
}