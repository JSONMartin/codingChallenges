var Vector = function (components) {
  this.components = components;
};

Vector.prototype.equals = function(vector) {
  var arr1 = this.components;
  var arr2 = vector.components;
  if(arr1.length !== arr2.length)
    return false;
  for(var i = arr1.length; i--;) {
    if(arr1[i] !== arr2[i])
      return false;
  }
  return true;
};

Vector.prototype.add = function(vector) {
  var summedArray = [];
  if(this.components.length !== vector.components.length) {
    throw new Error("Vectors need to be same size!");
  }

  for(var i = 0; i < this.components.length; i++) {
    summedArray.push(this.components[i] + vector.components[i]);
  }

  return new Vector(summedArray);
};

Vector.prototype.subtract = function(vector) {
  var summedArray = [];
  if(this.components.length !== vector.components.length) {
    throw new Error("Vectors need to be same size!");
  }

  for(var i = 0; i < this.components.length; i++) {
    summedArray.push(this.components[i] - vector.components[i]);
  }

  return new Vector(summedArray);
};

Vector.prototype.dot = function(vector) {
  var summedArray = [];
  if(this.components.length !== vector.components.length) {
    throw new Error("Vectors need to be same size!");
  }
  var total = 0;

  for(var i = 0; i < this.components.length; i++) {
    total+=(this.components[i] * vector.components[i]);
  }

  return total;
};

Vector.prototype.norm = function() {
  var total = 0;

  for(var i = 0; i < this.components.length; i++) {
    total+=Math.pow(this.components[i], 2);
  }

  return Math.sqrt(total);
};

Vector.prototype.toString = function() {
  var str = "(";
  for(var i = 0; i < this.components.length; i++) {
    str = str + this.components[i] + ",";
  }
  return str.slice(0,-1) + ")";
};