function Node(data) {
  this.data = data;
  this.next = null;
}

function length(head) {
  if(!head) { return 0; }
  var counter = 1;
  while(head.next) {
    counter++;
    head = head.next;
  }
  return counter;
}

function count(head, data) {
  if(!head) { return 0; }
  var counter = 0;
  if(data === head.data) { counter++; }
  while(head.next) {
    head = head.next;
    if(data === head.data) { counter++; }
  }
  return counter;
}