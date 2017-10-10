<?php
//This program is to be run using command line php. In order to make the program as flexible as possible, I wrote it such that it takes the number of chairs as it's first and only argument.
//While this problem can easily be done using a brute-force solution, it takes O(log2(n)) time to solve using that method.
//Noticing a mathematical relationship in the first few simple cases (1 - 8 chairs),
//I realized that this problem can be solved in constant time O(1) by utilizing a mathematical closed form solution.
function seatedSurvivor($numChairs) {
  //If the number of chairs is a power of two, the person in the highest numbered chair will be the survivor.
  if(floor(log($numChairs, 2)) == log($numChairs, 2)) {
    return $numChairs;
  //Otherwise the survivor is seated in the chair whose number is two times the difference between the highest numbered chair and the highest "power of two" numbered chair.
  //For example if there are 100 chairs, the highest numbered chair is 100, and the highest "power of two" numbered chair is 64 (since 2^9=128 is greater than 100, 2^8=64 is the highest power of two). So 2*(100-64) = 72. Thus the survivor is seated in chair #72.
  } else {
    return 2*($numChairs - pow(2, floor(log($numChairs, 2))));
  }
}
if(!isset($argv[1])) {
  die("Please provide the number of chairs as the first command-line argument.\n");
}
echo "The survivor is seated in chair #".seatedSurvivor($argv[1])."\n";
?>
