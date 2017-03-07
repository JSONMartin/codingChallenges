function incrementString (strng) {
  try {
    let word = (strng.match(/[a-zA-Z]/gi) || []).join(''),
        nums = (strng.match(/[0-9]/gi) || [0]),
        newNum = parseFloat(nums ? nums.join('') : 0) + 1,
        differenceInLengths = nums.length - (""+newNum).length;

    word = word.length >= 1 ? word : [];
    nums =   nums.length >= 1 ?   nums : [];

    return word + '0'.repeat(differenceInLengths > 0 ? differenceInLengths : 0) + newNum;
  } catch(e) {
    if (isNaN(parseFloat(strng))) {
      return strng + '1';
    }
    else {
      return "" + (parseFloat(strng) + 1);
    }
  }
}
