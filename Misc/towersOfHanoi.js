/**
 * Created by jsonmartin on 4/22/16.
 */
function hanoi(n) {
  var stacks = {
    A: [],
    B: [],
    C: []
  };

  var stackTrace = [];

  for(var i = n; i >= 0; i--) { // Initialize Stack with disks in reverse order
    stacks['A'].push(i);
  }

  var numTurns = 0;
  var numSolveCalls = 0;

  function solve(numDisks, source, destination, spare) {
    stackTrace.push("Solve called with:" + JSON.stringify(arguments));
    numSolveCalls++;
    if(numDisks >= 0) {
      solve(numDisks - 1, source, spare, destination);
      moveDisk(source, destination);
      solve(numDisks - 1, spare, destination, source);
    }
  }

  function moveDisk(from, to) {
    numTurns++;
    console.log("Turn [" + numTurns + "], Moving disk from " + from + " to " + to);
    stackTrace.push("Moving disk from " + from + " to " + to);
    stacks[to].push(stacks[from].pop());
    console.log("CURRENT Stack:", stacks);
  }

  console.log("Starting Stack:", stacks);

  solve(n, 'A', 'C', 'B'); //OR if desired ending peg is B...: solve(n, 'A', 'B', 'C');
  console.log("Total turns:" + numTurns);
  console.log("Ending Stack:", stacks);
  console.log("Total Calls to Solve:", numSolveCalls);
  console.log("-----");
  console.log("Ending Stack trace", stackTrace);
}

/******************************************
 * TESTS
 ******************************************/

hanoi(2);