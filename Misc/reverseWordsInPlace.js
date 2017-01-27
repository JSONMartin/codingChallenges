function reverseWords(message) {
  var messageArr = message.split(' '); //Split message string into array by spaces
  var len = messageArr.length - 1;
  var midPoint = Math.floor( len / 2);
  for(var i = 0; i <= midPoint; i++) { //Starting with the first word, swap with last. Increment until halfway mark
    var temp = messageArr[i];
    messageArr[i] = messageArr[len - i];
    messageArr[len - i] = temp;
  }
  return messageArr.join(' '); //Rejoin split string, and return
}

/******************************************
 * TESTS
 ******************************************/

var message = 'find you will pain only go you recordings security the into if';

console.log(reverseWords(message));