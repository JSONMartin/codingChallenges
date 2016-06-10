function removeSmallest(numbers) {
  if(numbers.length === 0) return [];

  let lowestIndex = 0;
  for(let i = 1; i < numbers.length; i++) {
    if(numbers[i] < numbers[lowestIndex]) lowestIndex = i
  }

  numbers.splice(lowestIndex, 1);

  return numbers;
}
