// Longest repeated number in string
// 111 -> 3
// 111122 -> 4
// 22111112 -> 5
'use strict';

function longestRepeatedNumCountImproved(str) {
  let count = 1, max = 1;
  let last = str[0];
  for(var i = 1; i < str.length; i++) {
    let cur = str[i];

    if(cur === last) {
      count++;
    } else {
      count = 1;
    }

    if(count > max) {
      max = count;
    }

    last = str[i];
  }

  return max;
}
function longestRepeatedNumCountOrig(str) {
    let count = 1, max = 1;
    let last = str[0];
    for(var i = 1; i < str.length; i++) {
      let cur = str[i];

      if(cur === last) {
        count++;
      } else {
        if(count > max) {
          max = count;
        }
        count = 1;
      }

      if (i === str.length - 1) {
        if(count > max) {
          max = count;
        }
      }

      last = str[i];
    }

  return max;
}

function streak(arr) {
  var i,
    temp,
    streak,
    length = arr.length,
    highestStreak = 0;

  for(i = 0; i < length; i++) {
    // check the value of the current entry against the last
    if(temp != '' && temp == arr[i]) {
      // it's a match
      streak++;
    } else {
      // it's not a match, start streak from 1
      streak = 1;
    }

    // set current letter for next time
    temp = arr[i];

    // set the master streak var
    if(streak > highestStreak) {
      highestStreak = streak;
    }
  }

  return highestStreak;
}


let res1 = longestRepeatedNumCountImproved('22111112');
console.log(res1);

let res2 = streak('22111112'.split(''));
console.log(res2);