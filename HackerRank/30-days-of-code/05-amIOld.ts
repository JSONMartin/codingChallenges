/**
 * Created by jsonmartin on 5/2/16.
 */
class Person {
    constructor(public age: number) {
        if(age < 0) {
            console.log("Age is not valid, setting age to 0.");
            age = 0;
        }
    }
    yearPasses() {
        this.age++;
    }
    amIOld() {
        if(this.age < 13) {
            console.log("You are young.");
        }
        else if(this.age >= 13 && this.age < 18) {
            console.log("You are a teenager.");
        }
        else {
            console.log("You are old.");
        }
    }
    agePlusNum(num: number) {
        return this.age + num;
    }
}