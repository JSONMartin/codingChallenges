class Solution {
    constructor() {
        this._queue = [];
        this._stack = [];
    }
    pushCharacter(ch) {
        this._queue.push(ch);
    }
    enqueueCharacter(ch) {
        this._stack.push(ch);
    }
    popCharacter() {
        return this._queue.pop();
    }
    dequeueCharacter() {
        return this._stack.shift();
    }
}
