const sumUpNumbers = inputStr =>
{
    try {
        return inputStr.match(/\d+/g).map(num => parseInt(num)).reduce((prev, cur) => prev + cur)

    } catch(e) {
        return 0
    }
}