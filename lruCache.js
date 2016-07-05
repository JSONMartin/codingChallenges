/**
 * Created by jsonmartin on 6/30/16.
 */
/**
 * @constructor
 */
var LRUCache = function(capacity) {
  this.capacity = capacity;
  this.cache = [];
  this.counter = 0;
};

/**
 * @param {number} key
 * @returns {number}
 */
LRUCache.prototype.get = function(key) {
  for(let i = 0; i < this.cache.length; i++) {
    let itemArr = this.cache[i];
    let item = itemArr[0];
    if(item[0] == key) {
      itemArr[1] = this.counter++;
      return item[1];
    }
  }
  return -1;
};

/**
 * @param {number} key
 * @param {number} value
 * @returns {void}
 */
LRUCache.prototype.set = function(key, value) {
  let obj = [key,value];

  // Check if already within cache

  for(let i = 0; i < this.cache.length; i++) {
    let itemArr = this.cache[i];
    let item = itemArr[0];
    if(item[0] == key) {
      item[1] = value;
      itemArr[1] = this.counter++;
      return;
    }
  }

  // If not in cache...

  if(this.cache.length < this.capacity) {
    this.cache.push([obj, this.counter++] );
  }

  else { // Search for oldest item
    let min = this.cache[0][1];
    let minIdx = 0;

    this.cache.forEach((itemArr, idx) => {
      let t = itemArr[1];
      if(t < min) {
        min = t;
        minIdx = idx;
      }
    });

    this.cache[minIdx] = [obj, this.counter++];
  }
};