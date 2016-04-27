// /*
//  Implement a key-value store with history (through timestamps)  |
//  Write a map implementation with a get function that lets you retrieve the value of a key at a particular time
//  */


var HashTableTimestamp = function() {
  this.values = {};
};

HashTableTimestamp.prototype.setValue = function(key, value) {
  //Check if key currently exists & has any data
  if(!this.values[key]) {
    this.values[key] = [];
  }

  //Set value & record with timestamp
  this.values[key].push({timestamp: Date.now().toString(), value: value});
};

HashTableTimestamp.prototype.get = function(key, timestamp) {
  if(!timestamp) {
    return this.values[key][this.values[key].length - 1];
  }
  else {
    for(var i = 0; i < this.values[key].length; i++) {
      if(this.values[key][i].timestamp === timestamp) {
        return this.values[key][i];
      }
    }
  }
};

/******************************************
 * TESTS
 ******************************************/

var ht = new HashTableTimestamp();

ht.setValue('asdf', '1');
var res = ht.getValue('asdf');
console.log(res);

ht.setValue('asdf', '2');
res = ht.getValue('asdf');
console.log(res);

res = ht.getValue('asdf');
console.log(res);
