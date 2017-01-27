// /**
//  * Created by jsonmartin on 3/28/16.
//  */


function Cat(name, weight) {
  if(!name || !weight) {
    throw new Error("Need to have name & weight");
  }
  this.name = name;
  this.weight = weight;

  Cat.weights.push(weight);
}

Object.defineProperty(Cat, 'weights', {
  value: [],
  writable: true,
  enumerable: true,
  configurable: true
});

// Cat.weights = [];

Cat.averageWeight = function() {
  console.log('averageWeight');
  var length = Cat.weights.length;
  var total = 0;
  for(var i = 0; i < length; i++) {
    total+=Cat.weights[i];
  }
  var avg = total/length;
  console.log("Avg weight:", avg);
  return avg;
};
// Cat.averageWeight(); // 25

/******************************************
 * TESTS
 ******************************************/


var garfield = new Cat('garfield', 25);
Cat.averageWeight(); // 25

var felix = new Cat('felix', 15);
Cat.averageWeight();   // now 20

