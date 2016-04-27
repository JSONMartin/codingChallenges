/**
 * Created by jsonmartin on 3/31/16.
 */
function LinkedList() {

  var Node = function(element){ // {1}
    this.element = element;
    this.next = null;
  };

  var _length = 0; // {2}
  var _head = null; // {3}

  this.append = function(element){
    var newNode = new Node(element);

    if(!_head) {
      _head = newNode;
    } else {
      var curNode = _head;
      while(curNode && curNode.next) { //Increment through linked list until reach end node
          curNode = curNode.next;
      }
      curNode.next = newNode;
    }

    _length++;
  };

  this.insert = function(position, element){
    if(position > _length || position < 0) { throw new Error("Position is greater than length of linked list"); }
    if(position === 0) {
      var curHead = _head;
      if(curHead) {
        _head = new Node(element);
        _head.next = curHead;
      }
    } else {
      var curNode = _head;
      for(var i = 0; i < (position - 1); i++) {
        if(!curNode) {
          throw new Error("Position is greater than length of linked list");
        }
        curNode = curNode.next;
      }
      var newNode = new Node(element);
      newNode.next = curNode.next;
      curNode.next = newNode;
      //newNode.next = curNode;
    }
    _length++;
    return true;
  };

  this.removeAt = function(position){
    var deletedNode;
    if(position > _length || position < 0) { throw new Error("Position is greater than length of linked list"); }
    if(position === 0) {
      if(_head.next) {
        _head = _head.next;
      }
    } else {
      var curNode = _head;
      for(var i = 0; i < (position - 1); i++) {
        if(!curNode) {
          throw new Error("Position is `reater than length of linked list");
        }
        curNode = curNode.next;
      }
      deletedNode = curNode.next;
      curNode.next = curNode.next.next;
    }
    _length--;
    return deletedNode.element;
  };

  this.remove = function(element){
    var idx = this.indexOf(element);
    if(idx > -1) {
      return this.removeAt(idx);
    } else {
      console.error("Element does not exist!");
      throw new Error("Element does not exist!");
    }
  };

  this.indexOf = function(element){
    var curNode = _head;
    var index = 0;
    while(curNode) {
      if(curNode.element === element) {
        return index;
      }
      curNode = curNode.next;
      index++;
    }
    return -1;
  };

  this.isEmpty = function() {
    return (_length === 0);
  };

  this.size = function() {
    return _length;
  };

  this.toString = function(){
    var str = "";
    if(!_head) {
      console.error("Empty!");
    } else {
      var curNode = _head;
      while(curNode) {
        str+=curNode.element.toString() +" ";
        curNode = curNode.next;
      }
    }
    return str.trim();
  };

  this.print = function(){
    console.log("---------");
    if(!_head) {
      console.error("Empty!");
    } else {
      var curNode = _head;
      while(curNode) {
        console.log(curNode.element);
        curNode = curNode.next;
      }
    }
    console.log("---------");
  };

  this.getHead = function() {
    return _head;
  }

}

/******************************************
 * TESTS
 ******************************************/

var ll = new LinkedList();
ll.print();
ll.append('a');
ll.print();
ll.append('b');
ll.append('c');
ll.print();
/*
---------
a
b
c
---------
*/
ll.insert(3, 'lol');
ll.print();
/*
 ---------
 a
 lol
 b
 c
 ---------
 */
// ll.insert(0, 'haha');
// ll.print();
// console.log(ll.toString());
//
// console.log(ll.indexOf('lol'));
// console.log(ll.indexOf('b'));
// ll.removeAt(2);
// console.log(ll.toString());
// ll.remove('c');
console.log(ll.toString());
console.log(ll.removeAt(1));
console.log(ll.toString());
console.log("HEAD!:", ll._head);