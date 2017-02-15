// https://www.codewars.com/kata/58595b6f5a8a0713e6000eed/solutions/javascript

function maxConsecutiveSequenceLength(array) {
  if (!array || array.length === 0) return 0;

  let max = 0;

  for (let i = array.length; i >= 0; i--) {
    let count = 1, cur = array[i];

    for (let j = i - 1; j >= 0; j--) {
        let next = array[j];

        if (next === cur || next === cur - 1) {
          count++;
          cur = next;
        }
    }

    max = Math.max(max, count);
  }

  return max;
}
