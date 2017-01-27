/**
 * Created by jsonmartin on 3/31/16.
 */
function Set() {
  var items = {};

  this.add = function(value) {
    items[value] = true;
  };

  this.remove = function(value) {
    delete items[value];
  };

  this.has = function(value) {
    return items.hasOwnProperty(value);
  };

  this.clear = function() {
    items = {};
  };

  this.size = function() {
    return Object.keys(items).length;
  };

  this.values = function() {
    var valuesArr = [];
    for(var key in items) {
      valuesArr.push(key);
    }
    return valuesArr;
  };

  this.union = function(otherSet) {
    var newSet = new Set();
    var set1Values = this.values();
    var set2Values = otherSet.values();

    var addValue = function(value) {
      if(!newSet.has(value)) {
        newSet.add(value);
      }
    };

    set1Values.forEach(addValue);
    set2Values.forEach(addValue);
    return newSet;
  }

  this.intersection = function(otherSet) {
    var newSet = new Set();
    var set1Values = this.values();

    var checkValue = function(value) {
      if(otherSet.has(value)) {
        newSet.add(value);
      }
    };

    set1Values.forEach(checkValue);
    return newSet;
  };

  this.difference = function(otherSet) {
    var newSet = new Set();
    var set1Values = this.values();

    var checkValue = function(value) {
      if(!otherSet.has(value)) {
        newSet.add(value);
      }
    };

    set1Values.forEach(checkValue);
    return newSet;
  };

  this.subset = function(otherSet) {
    var set1Values = this.values();
    var isSubset = true;

    var checkValue = function(value) {
      if(!otherSet.has(value)) {
        isSubset = false;
      }
    };

    set1Values.forEach(checkValue);
    return isSubset;
  };
}

/******************************************
 * TESTS
 ******************************************/

var s = new Set();
s.add('a');
s.add('b');
s.add('c');
console.log(s.size());
console.log(s.values());
console.log(s.has('a')); // true
console.log(s.has('d')); // false
s.remove('b');
console.log(s.values());

var s2 = new Set();
s2.add('1');
s2.add('2');
s2.add('3');
s2.add('a');

var s2Copy = new Set();
s2Copy.add('1');
s2Copy.add('2');
s2Copy.add('3');

var unionSet = s.union(s2);
console.log(unionSet.values());

var intersectionSet = s.intersection(s2);
console.log(intersectionSet.values());

var differenceSet = s.difference(s2);
console.log(differenceSet.values());

console.log(s.subset(s2));
console.log(s2Copy.subset(s2));