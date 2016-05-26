this.removeDuplicates=function(head){
  let seen = {};
  seen[head.data] = true;
  let curNode = head.next;
  let prevNode = head;

  while(curNode) {
      if(curNode.data in seen) {
          let next = curNode.next;
          prevNode.next = next;
          curNode = next;
      } else {
          seen[curNode.data] = true;
          curNode = curNode.next;
          prevNode = prevNode.next;
      }
  }
  return head;
}
