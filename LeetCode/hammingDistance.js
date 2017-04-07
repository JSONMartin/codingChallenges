const hammingDistance = (x, y) => {
  // Calculate Binary Strings
  x = parseInt(x).toString(2), y = parseInt(y).toString(2)

  let maxLength = Math.max(x.length, y.length) + 1

  x = "0".repeat(maxLength - x.length) + x, y = "0".repeat(maxLength - y.length) + y

  // Calculate Difference
  let differenceCount = 0
  for (let i = 0; i < x.length; i++) {
      if (x[i] != y[i]) differenceCount++
  }

  return differenceCount
}

console.log(hammingDistance(1, 4))
