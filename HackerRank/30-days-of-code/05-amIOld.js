/**
 * Created by jsonmartin on 5/2/16.
 */
var Person = (function () {
    function Person(age) {
        this.age = age;
        if (age < 0) {
            console.log("Age is not valid, setting age to 0.");
            age = 0;
        }
    }
    Person.prototype.yearPasses = function () {
        this.age++;
    };
    Person.prototype.amIOld = function () {
        if (this.age < 13) {
            console.log("You are young.");
        }
        else if (this.age >= 13 && this.age < 18) {
            console.log("You are a teenager.");
        }
        else {
            console.log("You are old.");
        }
    };
    Person.prototype.agePlusNum = function (num) {
        return this.age + num;
    };
    return Person;
}());
//# sourceMappingURL=05-amIOld.js.map