function maxset(a) {
  var subArrs = [];
  var curSubArr = [];

  for(var i = 0; i < a.length; i++) {
    if(a[i] < 0) {
      if(curSubArr.length > 0) {
        subArrs.push(curSubArr.slice());
        curSubArr = [];
      }
    }
    else {
      curSubArr.push(parseInt(a[i]));
    }
  }
  if(curSubArr.length > 0) {
    subArrs.push(curSubArr.slice());
  }

  var maxSubArrIdx = function() {
    var maxIdx = 0;
    var maxVal = 0;
    subArrs.forEach(function(arr, idx) {
      var total = arr.reduce(function(prev, cur) {return prev + cur;});
      //console.log("Total for arr[ "+ arr + " ]:", total);
      if(total > maxVal) {
        maxVal = total;
        maxIdx = idx;
      }
      else if(total === maxVal) {
        if(subArrs[idx].length > subArrs[maxIdx].length) {
          maxIdx = idx;
        }
        else if(subArrs[idx].length === subArrs[maxIdx].length) {
          maxIdx = (subArrs[idx][0] > subArrs[maxIdx][0]) ? idx : maxIdx;
        }
      }
    });
    //console.log("maxIdx:", maxIdx);
    return maxIdx;
  }
  //console.log("SubArrs:", subArrs);
  if(subArrs.length === 0) { return ""; }
  var maxIdx = maxSubArrIdx();

  return subArrs[maxIdx];
}

//var res = maxset([1, 2, 5, -7, 2, 3]);
var res = maxset([-1, -1, -1]);
