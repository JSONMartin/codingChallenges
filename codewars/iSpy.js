Array.prototype.contains = function(x) {
    return this.indexOf(x) > -1;
};

var spyOn = function(func) {
    let callCounter = 0, calledWithList = [], returnedList = [];

    let fn = function() {
        callCounter++;
        let res = func(...arguments);

        for (let i = 0; i < arguments.length; i++) {
            let arg = arguments[i];
            if (!calledWithList.contains(arg)) { calledWithList.push(arg); }
        }

        if (!returnedList.contains(res)) {
            returnedList.push(res);
        }

        return res;
    };

    fn.callCount = () => callCounter;
    fn.returned = v => returnedList.contains(v);
    fn.wasCalledWith = x => calledWithList.contains(x);

    return fn;
};

// var spyOn = function(func) {
//     return new spyder(func);
// };

// Testing

function returns1 () { return 1; }

var spy = spyOn(returns1);
//var spy = spyder(returns1);
//console.log(spy);
let res = spy.callCount();
console.log(res);
spy('hi');
res = spy.returned(1);
console.log(res);

var spy2 = spyOn(returns1);
spy2('hi', 'asdf', 'blah');
spy2('hi', 'asdf', 'blahf');
spy2('hi', 'asdf', 'blahf');
console.log(spy2.callCount()); // => 3

console.log(spy.callCount()); // => 1

console.log(spy.wasCalledWith('hi'));