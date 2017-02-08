// https://www.codewars.com/kata/57ad85bb7cb1f3ae7c000039/solutions/javascript

function numbersWithDigitInside(x, d) {
  let count = 0, sum = 0, product = 1;

  for (let num = 1; num <= x; num++) {
    if (num.toString().includes(d)) {
      count++;
      sum += num;
      product *= num;
    }
  }

  return [count, sum, product === 1 ? 0 : product]
}
