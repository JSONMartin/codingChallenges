function deepTrim(obj) {
  for(var key in obj) {
    var item = obj[key];
    if(typeof item === 'string' || item instanceof String) { // Check if item is string...
      obj[key] = obj[key].trim(); //Trim item
    } else if (Array.isArray(item)){ // Check if is array
      for(var i = 0; i < item.length; i++) {
        var element = item[i];
        if(typeof element === 'string' || element instanceof String) { // Check if element is string...
          item[i] = item[i].trim();
        }
      }
    } else if (item === Object(item)) { // Check if item is object
      deepTrim(item); // Call deepTrim on the object
    }
  }
}

/******************************************
 * TESTS
 ******************************************/

var testObj = {a: 1, b: false, c: "   Xyz   ", d: {a: 10, b: "   dfg   "}, e: [1, "   ddss   "]};
console.log("Before:", testObj);
deepTrim(testObj);
console.log("After:", testObj);
