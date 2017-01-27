function isBalanced(inputStr, stack = []) {
  const dict = {
    "(": ")",
    "{": "}",
    "[": "]"
  };

  // Base Cases
  if (inputStr.length === 0 && stack.length === 0) { return true; }
  if (inputStr.length === 0 && stack.length > 0) { return false; }

  let curChar = inputStr[0];

  if (curChar in dict) {
    stack.push(dict[curChar]);
  }

  else if (')}]'.includes(curChar)) {
    if (curChar !== stack.pop()) { return false; }
  }

  if (!isBalanced(inputStr.substr(1), stack)) { return false; }
  else { return true; }
}

/**********
 * Tests
 **********/
const assertEquals = (test, expected, actual) => {
  if (expected !== actual) {
    console.error(`Failed test: ${test}. >>>>> Actual value: ${actual} | Expected value: ${expected}`);
    return false;
  } else {
    console.error(`Passed test: ${test}. >>>>> Actual value: ${actual} | Expected value: ${expected}`);
    return true;
  }
};

const tests = [
  ['{}', true],
  ['{[]}', true],
  ['{5}', true],
  ['{[}', false],
  ['[A]{}d()', true],
  ['a', true],
  ['a}', false],
];

tests.map((test) => assertEquals(test[0], isBalanced(test[0]), test[1]));