/**
 * Created by jsonmartin on 3/30/16.
 */
function Stack() {
  this._items = [];
}

Stack.prototype.push = function() {
  for(var i = 0; i < arguments.length; i++) {
    this._items.push(arguments[i]);
  }
};

Stack.prototype.pop = function() {
  return this._items.pop();
};

Stack.prototype.peek = function() {
  return this._items[(this._items.length - 1)];
};

Stack.prototype.isEmpty = function() {
  return this._items.length === 0;
};

Stack.prototype.clear = function() {
  this._items = [];
};

Stack.prototype.size = function() {
  return this._items.length;
};

Stack.prototype.print = function() {
  console.log(this._items.toString());
};

function divideBy2(num) { //Converts number into binary
  var s = new Stack();

  function divideUntilZeroRemainder(num) {
    console.log(num);
    if(num === 0) { return 0; }
    s.push(num % 2);
    divideUntilZeroRemainder(Math.floor(num / 2) );
  }

  divideUntilZeroRemainder(num);

  var binaryString = "";
  while(!s.isEmpty()) {
    binaryString+=s.pop().toString();
  }

  s.print();
  console.log("Binary String:", binaryString);
  return binaryString;
}

// console.log(divideBy2(233));
// console.log(divideBy2(10));
// console.log(divideBy2(1000));


function baseConverter(num, base) { //Converts number into binary
  var s = new Stack();
  var digits = '0123456789ABCDEF';

  function divideUntilZeroRemainder(num) {
    console.log(num);
    if(num === 0) { return 0; }
    s.push(Math.floor(num % base));
    divideUntilZeroRemainder(Math.floor(num / base) );
  }

  divideUntilZeroRemainder(num);

  var binaryString = "";
  while(!s.isEmpty()) {
    binaryString+=digits[s.pop()];
  }

  s.print();
  console.log("Binary String:", binaryString);
  return binaryString;
}

console.log(baseConverter(100345, 2));
console.log(baseConverter(100345, 8));
console.log(baseConverter(100345, 16));