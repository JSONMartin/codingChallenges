function toCamelCase(str) {
    let split = str.split(/[^a-zA-Z]/)
    let result = [split[0], ...split.slice(1).map(s => s[0].toUpperCase() + s.slice(1))]
    return result.join('')
}
