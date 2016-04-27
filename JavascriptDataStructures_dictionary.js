/**
 * Created by jsonmartin on 4/4/16.
 */
function Dictionary() {
  var items = {};

  this.set = function(key,value) {
    items[key] = value;
  }; //This adds a new item to the dictionary.

  this.remove = function(key){
    if(this.has(key)) {
      delete items[key];
      return true;
    }
    return false;
  }; //This removes the value from the dictionary using the key.

  this.has = function(key){
    return items.hasOwnProperty(key);
  }; //This returns true if the key exists in the dictionary and false otherwise.

  this.get = function(key){
    if(this.has(key)) {
      return items[key];
    }
    return undefined;
  }; //This returns a specific value searched by the key.

  this.clear = function(){
    items = {};
  };// This removes all the items from the dictionary.

  this.size = function(){
    return Object.keys(items).length;
  }; //This returns how many elements the dictionary contains. It is similar to the length property of the array.

  this.keys = function(){
    return Object.keys(items);
  }; //This returns an array of all the keys the dictionary contains.

  this.values = function(){
    var vals = [];
    for(var item in items) {
      vals.push(items[item]);
    }
    //console.log(Object.values(items));
    // return Object.values(items);
    return vals;
  }; //This returns an array of all the values of the dictionary.

  this.getItems = function() {
    return items;
  }

}

/*
var d = new Dictionary();
console.log( d.size() ); // 0
console.log( d.set('a', 1) );
console.log( d.size() ); // 1
console.log( d.set('b', 2) );
console.log( d.set('c', 3) );
console.log( d.keys() ); // [a, b, c]
console.log( d.values() ); // [1, 2, 3]
*/


function HashTable() {
  var table = [];

  var loseloseHashCode = function (key) {
    var hash = 0;                           //{1}
    for (var i = 0; i < key.length; i++) {  //{2}
      hash += key.charCodeAt(i);          //{3}
    }
    return hash % 37;                       //{4}
  };

  this.put = function(key, value) {
    var htPosition = loseloseHashCode(key);
    console.log("Putting at position:" + htPosition + ", value:" + value);
    table[htPosition] = value;
  };

  this.remove = function(key) {
    var htPosition = loseloseHashCode(key);
    table[htPosition] = undefined;
  };

  this.get = function(key) {
    var htPosition = loseloseHashCode(key);
    return table[htPosition];
  };
}

var hash = new HashTable();
hash.put('Gandalf', 'gandalf@email.com');
hash.put('John', 'johnsnow@email.com');
hash.put('Tyrion', 'tyrion@email.com');