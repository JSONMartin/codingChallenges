class Event {
  constructor() {
    var _bucket = [];

    this.subscribe = function(){
      for(let i = 0; i < arguments.length; i++) {
        let e = arguments[i];
        if(typeof e === 'function') { _bucket.push(e); }
      }
    };

    this.unsubscribe = function() {
      for(let i = arguments.length - 1; i >= 0; i--) {
        let e = arguments[i];
        for(let j = _bucket.length - 1; j >= 0; j--) {
          if(_bucket[j] === e) {
            _bucket.splice(j, 1);
            break;
          }
        }
      }
    };

    this.emit = function() {
      let _bucketCopy = _bucket;
      for(let i = 0; i < _bucket.length; i++) {
        _bucketCopy[i].apply(this, arguments);
      }
    };
  }
}