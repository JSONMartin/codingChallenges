/**
 * Created by jsonmartin on 5/18/16.
 */
/**
 * Created by jsonmartin on 5/18/16.
 */
var Event = (function () {
    function Event() {
        this['_bucket'] = [];
    }
    Event.prototype.subscribe = function () {
        for (var i = 0; i < arguments.length; i++) {
            var e = arguments[i];
            this._bucket.push(e);
        }
    };
    Event.prototype.unsubscribe = function () {
        for (var i = arguments.length - 1; i >= 0; i--) {
            var e = arguments[i];
            for (var j = this._bucket.length - 1; j >= 0; j--) {
                if (this._bucket[j] === e) {
                    this._bucket.splice(j, 1);
                    break;
                }
            }
        }
    };
    Event.prototype.emit = function (arr) {
        for (var i = 0; i < this._bucket.length; i++) {
            this._bucket[i](arr);
        }
        // arr = this._bucket;
        // return arr;
        return arr;
    };
    return Event;
}());
//# sourceMappingURL=events.js.map