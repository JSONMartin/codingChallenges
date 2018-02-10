function solution(numbers) {

  // Selection Sort
  for (let i = 0; i < numbers.length; i++) {
    let minIdx = i

    for (let j = i + 1; j < numbers.length; j++) {
      if (numbers[j] < numbers[minIdx]) minIdx = j
    }

    [numbers[i], numbers[minIdx]] = [numbers[minIdx], numbers[i]] // Swap numbers
  }

  return numbers
}

