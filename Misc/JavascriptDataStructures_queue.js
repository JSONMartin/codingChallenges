/**
 * Created by jsonmartin on 3/31/16.
 */
function Queue() {
  this._items = [];
}

Queue.prototype.enqueue = function() {
  for(var i = 0; i < arguments.length; i++) {
    this._items.push(arguments[i]);
  }
};

Queue.prototype.dequeue = function() {
  return this._items.shift();
};

Queue.prototype.front = function() {
  return (this._items.length > 0) ? this._items[0] : false;
};

Queue.prototype.isEmpty = function() {
  return (this._items.length === 0);
};

Queue.prototype.size = function() {
  return this._items.length;
};

Queue.prototype.clear = function() {
  this._items = [];
};

Queue.prototype.print = function() {
  console.log(this._items.toString());
};

/******************************************
 * TESTS
 ******************************************/

var Q = new Queue();
Q.print();