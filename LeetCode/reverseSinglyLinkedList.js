var reverseList = function(head) {
    if(!head || head.next === null) { return head; }
    let q = [];
    let cur = head;
    
    while(cur) {
        q.push(cur);
        cur = cur.next;
    }
    
    if(q.length > 0) {
        head = q.pop();
        cur = head;
        cur.next = null;
        while(q.length > 0) {
            console.log("Cur val:" + cur.val)
            cur.next = q.pop();
            cur = cur.next;
        }
        cur.next = null;
    }
    
    return head;
};
