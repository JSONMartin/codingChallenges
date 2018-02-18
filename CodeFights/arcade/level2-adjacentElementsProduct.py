def adjacentElementsProduct(inputArray):
    length = len(inputArray)
    products = [inputArray[i] * inputArray[i + 1] for i in range(length - 1)]
    return max(products)
