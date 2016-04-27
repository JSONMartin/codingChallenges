/**
 * Created by jsonmartin on 4/24/16.
 */
// Create the NSA object
var NSA = {
  addLog: function(caller, callee, action, phone) {
    this.checkForCaller(caller);
    var str = caller + " " + action + " " + callee + " from " + phone.owner.name + "'s phone(" + phone.number + ")";
    NSA[caller].push(str);
  },
  log: function(person) {
    if(!this[person.name] || this[person.name] === []) { return "No Entries"; }
    var log = this[person.name].join("\n");
    delete this[person.name];
    return log;
  },
  checkForCaller : function(caller) {
    if(!NSA[caller]) {
      NSA[caller] = [];
    }
  }
};

var Person = function(name) {
  this.name = name;
  this.call = function(cellphone, callee) {
    NSA.addLog(this.name, callee.name, "called", cellphone);
  };
  this.text = function(cellphone) {
    for(var i = 1; i < arguments.length; i++) {
      var callee = arguments[i];
      NSA.addLog(this.name, callee.name, "texted", cellphone);
    }
  };
};

/******************************************
 * TESTS
 ******************************************/


// Create two people
var dan = new Person("Dan");
var mark = new Person("Mark");

// Create a phone object
var phone = {owner: dan, number: '202-555-0199'};

// Make a phone call
dan.call(phone, mark);

// Ensure our logs are accurate
console.log( NSA.log(dan) ); // -> 'Dan called Mark from Dan\'s phone(202-555-0199)');

