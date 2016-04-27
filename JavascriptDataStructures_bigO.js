/*
• The Fibonacci of 1 or 2 is 1
• The Fibonacci of n (for n>2) is the Fibonacci of (n-1) + the Fibonacci of (n-2)
  */

var fib = function(n) {
  if(n === 1 || n === 2) { return 1; }
  return ( fib(n-1) + fib(n-2) );
};

var fibNonRecrusive = function(n) {
  if(n === 1 || n === 2) { return 1; }
  var fib = [1, 1];

  var counter = 0;
  while(counter < n) {
    fib[counter] = fib[counter-1] + fib[counter-2];
    counter++;
  }

  return fib[n];
};


//console.log( "Recursive Fib:", fib(10) );
//console.log( "NON-Recursive Fib:", fib(10) );

/*

  Book Version:

 function fib(num){
   var n1 = 1,
   n2 = 1,
   n = 1;
   for (var i = 3; i<=num; i++){
     n = n1 + n2;
     n1 = n2;
     n2 = n;
   }
  return n;
 }

 Why use recursion? Is it faster? Recursion is not faster than the normal version;
 it is slower. But note that recursion is clear to understand and it requires less code as well.
 In ECMAScript 6, because of tail call optimization, recursion will not be slower. But in other languages, recursion code is usually slower.
 So, we usually use recursion because it is easier to solve problems using it.
 */


/*
 This is the version I constructed on my own, and is a "greedy algorithm".
 Did this without even knowing it!

 Greedy algorithms:
 A greedy algorithm follows the problem-solving heuristic of making the locally optimal choice
 (the best solution at the time) at each stage with the hope of ending a global optimum (global best solution).
 It does not evaluate the bigger picture like a dynamic programming algorithm does.
 Let's use the same problem we covered in the dynamic programming topic so we can see the difference.

 */
function MinCoinChange(amount){
  var coins = [1, 5, 10, 25];
  var total = 0;
  var result = [];

  while(total < amount) {
    total = !result.length ? 0 : result.reduce(function (prev, cur) {
      return prev + cur;
    });
    console.log("Total:", total);
    console.log("result:", result);
    console.log("coins:", coins);
    if( (total + coins[coins.length - 1]) <= amount ) {
      result.push(coins[coins.length - 1]);
      //total+=coins[coins.length - 1];
    } else {
      coins.pop();
    }
  }

  return result;
}

console.log("Coin change for 36:" + MinCoinChange(36) );

function MinCoinChangeDynamicProgramming(coins){
  var coins = coins; //{1}
  var cache = {};    //{2}
  this.makeChange = function(amount) {
    var me = this;
    if (!amount) { //{3}
      return [];
    }
    if (cache[amount]) { //{4}
      return cache[amount];
    }
    var min = [], newMin, newAmount;
    for (var i=0; i<coins.length; i++){ //{5}
      var coin = coins[i];
      newAmount = amount - coin;  //{6}
      if (newAmount >= 0){
        newMin = me.makeChange(newAmount); //{7}
      }
      if (
        newAmount >= 0 && //{8}
        (newMin.length < min.length-1 || !min.length)//{9}
        && (newMin.length || !newAmount) //{10}
      ){
        min = [coin].concat(newMin); //{11}
        console.log('new Min ' + min + ' for ' + amount);
      } }
    return (cache[amount] = min); //{12}
  };
}

var minCoinChange = new MinCoinChangeDynamicProgramming([1, 5, 10, 25]);
console.log(minCoinChange.makeChange(36));

/*
Greedy algorithm finds an acceptable solution via heuristics,
Dynamic Programming calculates all possible solutions, stores them, and finds the most optimal solution (at the expense of speed)

Greedy algorithms are simpler and also faster than dynamic programming algorithms.
However, as we can see, it is not going to give the optimal answer all the time.
But on average, it outputs an acceptable solution for the time it takes to execute.
 */