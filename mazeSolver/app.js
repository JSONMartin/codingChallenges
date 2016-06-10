"use strict";

let app = angular.module("mazeSolver", []);

app.controller("mazeCtrl", ($scope) => {
  $scope.test = "test";

  let maze2 = `
  S#####
  .....#
  #.##.#
  #.##.#
  ...#.G
  ##...#
  `;

  let m = new Maze(maze2);
  $scope.curMaze = m.curMaze;
  let solutions = m.solveMazeDFS();


});