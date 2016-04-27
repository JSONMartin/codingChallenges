/**
 * Created by jsonmartin on 3/16/16.
 */
function isMerge(s, part1, part2) {
  var curPos = 0;
  part1 = part1.split('');
  part2 = part2.split('');
  while(part1.length > 0 && part2.length > 0)
  {
    console.log("Part1:", part1[0]);
    console.log("Part2:", part2[0]);
    console.log("s[curPos]:", s[curPos]);
    console.log(part1);
    console.log(part2);
    if(part1[0] ===  s[curPos]) {
      part1.shift();
      curPos++;
    }
    else if(part2[0] ===  s[curPos]){
      part2.shift();
      curPos++;
    }
    else {
      return false;
    }
  }

  return true;
}

/******************************************
 * TESTS
 ******************************************/

console.log("--------------");
//var res = isMerge('codewars', 'code', 'wars');
//console.log(res);
res = isMerge('codewars', 'cdw', 'oears');
//console.log(res);
res = !isMerge('codewars', 'cod', 'wars');
console.log(res);

