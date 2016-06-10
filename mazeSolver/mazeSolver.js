"use strict";

function sleep(delay) {
  var start = new Date().getTime();
  while (new Date().getTime() < start + delay);
}

class Maze {
  constructor(mazeStr, delay) {
    delay = delay || 0;
    if(mazeStr) this.setMaze(mazeStr);
    this.setDelay(delay);
  }

  setDelay(delay) {
    this._delay = delay;
  }

  setMaze(mazeStr) {
    this._mazeArr = mazeStr.split("\n").filter((row) => (row.trim() !== '')).map((row) => row.trim().split(''));

    this._width = this._mazeArr[0].length;
    this._height = this._mazeArr.length;

    //Find starting point
    let findStartingPoint = () => {
      for(let r = 0; r < this._height; r++) {
        for(let c = 0; c < this._width; c++) {
          if(this._mazeArr[r][c] === 'S') {
            return [r, c];
          }
        }
      }
      return false;
    };

    this._startingPoint = findStartingPoint();
  }

  get curMaze() {
    return this._curMaze;
  }

  solveMazeDFS() {
    var possibleSolutions = [];
    //Check for Goal in current position
    let legalMove = (r, c, matrix) => {
      if(r < 0 || r >= this._height || c < 0 || c >= this._width) { // Check bounds
        return false;
      }
      if(matrix[r][c] === '.' || matrix[r][c] === 'G') {
        return true;
      }
    };

    let traverse = (r, c, maze, numsteps) => {
      //sleep(this._delay);
      this._curMaze = maze.slice();

      maze = maze.slice();

      numsteps = numsteps || 1;
      console.log("nunsteps:", numsteps);
      console.log("----------------------");
      console.log(maze);
      console.log("----------------------");

      //console.log(matrix[r][c]);
      if(maze[r][c] === 'G' || maze[r][c] === '!') { // Checks if is goal
        let winBoard = maze.slice();

        winBoard[r][c] = "!";
        console.log("NUMSTEPS TO SOLUTION:", numsteps);
        console.log("SOLUTION BOARD:");
        console.log("----------------------");
        console.log(winBoard);


        let newArr = winBoard.map(row => row.slice());
        console.log("NewArr:", newArr);
        console.log("----------------------");
        possibleSolutions.push({solution: newArr.slice(0), numsteps: numsteps});


        //possibleSolutions.push(winBoard.slice());
        //possibleSolutions.push(winStr);
        winBoard[r][c] = "G";
        //return matrix; // Goal found

      }
      else {
        maze[r][c] = '@';
        let foundGoal = false;

          if(legalMove(r+1, c, maze.slice())) {
            foundGoal = traverse(r+1, c, maze.slice(), numsteps+1);
            if(foundGoal) return true;
            //matrix[r+1][c] = '.';
          }
          //Check right
          if(legalMove(r, c+1, maze.slice())) {
            foundGoal = traverse(r, c+1, maze.slice(), numsteps+1);
            if(foundGoal) return true;
            //if(foundGoal) return true;
            //matrix[r][c+1] = '.';
          }
          //Check left
          if(legalMove(r, c-1, maze.slice())) {
            foundGoal = traverse(r, c-1, maze.slice(), numsteps+1);
            if(foundGoal) return true;
            //if(foundGoal) return true;
            //matrix[r][c-1] = '.';
          }
          //Check up
          if(legalMove(r-1, c, maze.slice())) {
            foundGoal = traverse(r-1, c, maze.slice(), numsteps+1);
            if(foundGoal) return true;
            //if(foundGoal) return true;
            //matrix[r-1][c] = '.';
          }
          maze[r][c] = ".";
        //return false;
        // return true;
      }
      return false;
    };

    let traverseAsync = (r, c, maze, numsteps) => {
      //sleep(this._delay);
      //this._curMaze = maze.;
      this._curMaze = maze

      //maze = maze.slice();
      maze = maze.map((r) => r.slice());

      numsteps = numsteps || 1;
      console.log("nunsteps:", numsteps);
      console.log("----------------------");
      console.log(maze);
      console.log("----------------------");

      //console.log(matrix[r][c]);
      if(maze[r][c] === 'G' || maze[r][c] === '!') { // Checks if is goal
        let winBoard = maze.slice();

        winBoard[r][c] = "!";
        console.log("NUMSTEPS TO SOLUTION:", numsteps);
        console.log("SOLUTION BOARD:");
        console.log("----------------------");
        console.log(winBoard);


        let newArr = winBoard.map(row => row.slice());
        console.log("NewArr:", newArr);
        console.log("----------------------");
        possibleSolutions.push({solution: newArr.slice(0), numsteps: numsteps});


        //possibleSolutions.push(winBoard.slice());
        //possibleSolutions.push(winStr);
        winBoard[r][c] = "G";
        return true;
        //return matrix; // Goal found

      }
      else {
        maze[r][c] = '@';
        let foundGoal = false;
            var p = new Promise((resolve, reject) => {
              // setTimeout(() => {
              //   console.log("This.maze:", maze.map((r) => r.slice()));
              //   foundGoal = traverseAsync(r+1, c, maze.map((r) => r.slice()), numsteps+1);
              //   resolve();
              // }, this._delay);'
              setTimeout(() => {
                if(legalMove(r+1, c, maze.slice())) {
                  //resolve(traverseAsync(r + 1, c, maze.map((r) => r.slice()), numsteps + 1)); // Down
                  resolve(traverseAsync(r + 1, c, maze, numsteps + 1)); // Down
                } else {
                  resolve(false);
                }
              }, this._delay);

            })
            .then((result) => {
              if (!result) {
                console.log("result from then going down:", result);
                //Check right
                new Promise((resolve, reject) => {
                  setTimeout(() => {
                    if (legalMove(r, c + 1, maze.slice())) {
                      //resolve(traverseAsync(r, c + 1, maze.map((r) => r.slice()), numsteps + 1));
                      resolve(traverseAsync(r, c + 1, maze, numsteps + 1));
                    }
                    else {
                      resolve(false);
                    }
                  }, this._delay);
                })
              }
            })
            .then((result) => {
              if (!result) {
                console.log("result from going right:", result);
                //Check right
                new Promise((resolve, reject) => {
                  setTimeout(() => {
                    if (legalMove(r, c - 1, maze.slice())) {
                      //resolve(traverseAsync(r, c - 1, maze.map((r) => r.slice()), numsteps + 1));
                      resolve(traverseAsync(r, c - 1, maze, numsteps + 1));
                    }
                    else {
                      resolve(false);
                    }
                  }, this._delay);
                })
              }
            })
            .then((result) => {
              if (!result) {
                console.log("result from going left:", result);
                //Check right
                new Promise((resolve, reject) => {
                  setTimeout(() => {
                    if (legalMove(r + 1, c, maze.slice())) {
                      resolve(traverseAsync(r + 1, c, maze, numsteps + 1));
                      //resolve(traverseAsync(r + 1, c, maze.map((r) => r.slice()), numsteps + 1));
                    }
                    else {
                      resolve(false);
                    }
                  }, this._delay);

                })
              }
            })
            .then((resultUp) => {
              if (!resultUp) {
                maze[r + 1][c] = '.'
              }
            });
          //maze[r][c] = ".";
        //return false;
        // return true;
      }
      //return new Promi
      return p;
    };

    //TODO: Complete async version
    //let res = traverseAsync(this._startingPoint[0], this._startingPoint[1], this._mazeArr.slice());
    let res = traverse(this._startingPoint[0], this._startingPoint[1], this._mazeArr.slice());
    // console.log(res);
    console.log("POSSIBLESOLUTIONS:");
    console.log(possibleSolutions);
    return possibleSolutions;
  }

  printMaze(maze) {
    let retStr = "";

    for(let i = 0; i < maze.length; i++) {
      console.log(maze[i])
      //retStr+=maze[i].join('');
    }

    return retStr;
  }
}

function printSolution(solution) {
  console.log("Total solutions:");

  for(let row in solution) {
    console.log(solution[row]);
  }
}

function solveMaze() {
  let maze1 = `
  S#####
  .....#
  #.####
  #.####
  ...#.G
  ##...#
  `;

  let maze2 = `
  S#####
  .....#
  #.##.#
  #.##.#
  ...#.G
  ##...#
  `;

  let m = new Maze(maze2, 1000);
  //let solutions = m.solveMazeDFS();
  let solutions = m.solveMazeDFS();
  //printSolution(solutions);
}

solveMaze();
