/**
 * @param {string} s
 * @param {string} t
 * @return {boolean}
 */
var isAnagram = function(s, t) {
    let seenS = {};
    let seenT = {};

    let countChar = (string, dict) => {
      for(let i = 0; i < string.length; i++) {
          dict[string[i]] = (dict[string[i]] || 0) + 1;
      }
    };

    countChar(s, seenS);
    countChar(t, seenT);

    if(Object.keys(seenS).length !== Object.keys(seenT).length) return false;

    for(let key in seenS) {
        if(seenS[key] !== seenT[key]) return false;
    }

    return true;
};
