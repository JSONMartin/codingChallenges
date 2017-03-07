class Test {
    static assertEquals(a, b) {
        let res = (a === b);
        console.log(`Result for actual: ${a} | expected: ${b}: ${res}`);
        return res;
    }
}

module.exports = Test;