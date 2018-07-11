function areFollowingPatterns(strings, patterns) {
    const patternMatches = {}
    const stringMatches = {}

    for (let i = 0; i < patterns.length; i++) {
        const pattern = patterns[i]
        const string = strings[i]

        if (stringMatches[string] && stringMatches[string] !== pattern) return false
        stringMatches[string] = pattern
        patternMatches[pattern] = pattern in patternMatches ? patternMatches[pattern].add(string) : new Set([string])
    }

    for (let pattern in patternMatches) {
        if (patternMatches[pattern].size > 1) return false
    }

    return true
}

/** TESTS */
let strings = ["cat",
 "dog",
 "dog"]

let patterns = ["a",
 "b",
 "b"]

let res = areFollowingPatterns(strings, patterns) //=> True
console.log(res);