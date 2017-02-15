/**
 * Created by jmartin on 2/10/17.
 */
/*
 Given s1, s2, s3, find whether s3 is formed by
 the interleaving of s1 and s2.

 For example,
 Given:
 s1 = "aabcc",
 s2 = "dbbca",

 When s3 = "aadbbcbcac", return true.
 When s3 = "aadbbbaccc", return false.
 */

/**
 * @param {string} s1
 * @param {string} s2
 * @param {string} s3
 * @return {boolean}
 */

const isInterleave = (s1, s2, s3) => {
    if (s1 === s2 && s2 === s3) return true;

    const interleave = (function interleaveMemoized() {
        let cache = {};

        return (s1, s2, current = "", remaining = s3) => {
            let found = false,
                nextLetterToLookFor = remaining[0];

            const cacheKey = JSON.stringify([s1, s2, current, remaining]);

            if (cacheKey in cache) { return cache[cacheKey]; }

            if (found || (remaining.length === 0 && s1.length === 0 && s2.length === 0)) {
                return true;
            }
            else if (!nextLetterToLookFor) { return false ;}

            if (s1.length > 0 && s1[0] === nextLetterToLookFor) {
                found = found || interleave(s1.slice(1), s2, current + s1[0], remaining.slice(1))
            }

            if (s2.length > 0 && s2[0] === nextLetterToLookFor) {
                found = found || interleave(s1, s2.slice(1), current + s2[0], remaining.slice(1))
            }

            return cache[cacheKey] = found;
        };
    })();

    return interleave(s1, s2);
};
/*
    Alternative Solutions below
 */

// var _ = require('lodash');

// const isInterleaveUsingLodash = (s1, s2, s3) => {
//     console.log(`s1:${s1}\ns2:${s2}\ns3:${s3}`);
//     let found = false,
//         functionRunCount = 0;
//
//     function interleaveS(s1, s2, current = "", remaining = s3) {
//         let cache = {};
//
//         const interleave = (s1, s2, current = "", remaining = s3) => {
//             functionRunCount++;
//             let nextLetterToLookFor = remaining[0];
//
//             if (found || (remaining.length === 0 && s1.length === 0 && s2.length === 0)) {
//                 return true;
//             }
//             else if (!nextLetterToLookFor) { return false ;}
//
//             if (s1.length > 0 && s1[0] === nextLetterToLookFor) {
//                 found = found || interleaveS(s1.slice(1), s2, current + s1[0], remaining.slice(1))
//             }
//
//             if (s2.length > 0 && s2[0] === nextLetterToLookFor) {
//                 found = found || interleaveS(s1, s2.slice(1), current + s2[0], remaining.slice(1))
//             }
//
//             return found;
//         };
//
//         let cacheStr = [...arguments].toString();
//         if (!(cacheStr in cache)) {
//             cache[cacheStr] = interleave(...arguments);
//         }
//
//         return cache[cacheStr];
//     }
//
//     // const interleave = (s1, s2, current = "", remaining = s3) => {
//     //     functionRunCount++;
//     //     let nextLetterToLookFor = remaining[0];
//     //
//     //     if (found || (remaining.length === 0 && s1.length === 0 && s2.length === 0)) {
//     //         return true;
//     //     }
//     //     else if (!nextLetterToLookFor) { return false ;}
//     //
//     //     if (s1.length > 0 && s1[0] === nextLetterToLookFor) {
//     //         found = found || interleave(s1.slice(1), s2, current + s1[0], remaining.slice(1))
//     //     }
//     //
//     //     if (s2.length > 0 && s2[0] === nextLetterToLookFor) {
//     //         found = found || interleave(s1, s2.slice(1), current + s2[0], remaining.slice(1))
//     //     }
//     //
//     //     return found;
//     // };
//
//     interleaveS(s1, s2);
//
//     console.log("function ran times:", functionRunCount);
//     return found;
// };

// const memoize = fn => {
//     let cache = {};
//
//
// };

const isInterleaveBeforeCleanup = (s1, s2, s3) => { // 99 out of 101 test cases passed
    //console.log(`s1:${s1}\ns2:${s2}\ns3:${s3}`);

    if (s1 === s2 && s2 === s3) return true;

    let found = false,
        functionRunCount = 0;

    const interleaveMemoized = () => {
        let cache = {};

        let interleave = (s1, s2, current = "", remaining = s3) => {
            console.log("cache:", cache);
            functionRunCount++;
            let nextLetterToLookFor = remaining[0];
            const cacheKey = JSON.stringify([s1, s2, current, remaining]);

            if (cacheKey in cache) { return cache[cacheKey]; }

            if (found || (remaining.length === 0 && s1.length === 0 && s2.length === 0)) {
                return true;
            }
            else if (!nextLetterToLookFor) { return false ;}

            if (s1.length > 0 && s1[0] === nextLetterToLookFor) {
                found = found || interleave(s1.slice(1), s2, current + s1[0], remaining.slice(1))
            }

            if (s2.length > 0 && s2[0] === nextLetterToLookFor) {
                found = found || interleave(s1, s2.slice(1), current + s2[0], remaining.slice(1))
            }

            return cache[cacheKey] = found;
        };

        return interleave;
    };

    let interleave = interleaveMemoized();

    //console.log(interleave);

    interleave(s1, s2);

    //console.log("function ran times:", functionRunCount);
    return found;
};

// const isInterleaveLodashMemoize = (s1, s2, s3) => { // 99 out of 101 test cases passed
//     console.log(`s1:${s1}\ns2:${s2}\ns3:${s3}`);
//     let found = false,
//         functionRunCount = 0;
//
//     let interleave = (s1, s2, current = "", remaining = s3) => {
//         functionRunCount++;
//         let nextLetterToLookFor = remaining[0];
//
//         if (found || (remaining.length === 0 && s1.length === 0 && s2.length === 0)) {
//             found = true;
//             return true;
//         }
//         else {
//             if (!nextLetterToLookFor) { return false ;}
//         }
//
//         if (s1.length > 0 && s1[0] === nextLetterToLookFor) {
//             found = found || interleave(s1.slice(1), s2, current + s1[0], remaining.slice(1))
//         }
//
//         if (s2.length > 0 && s2[0] === nextLetterToLookFor) {
//             found = found || interleave(s1, s2.slice(1), current + s2[0], remaining.slice(1))
//         }
//
//         return found;
//     };
//
//     interleave = _.memoize(interleave, function(...input) {
//         console.log("input:", input);
//         return JSON.stringify(input);
//     });
//
//     interleave(s1, s2);
//
//     console.log("function ran times:", functionRunCount);
//     return found;
// };

/*
    Testing
 */

// let s1 = "aabcc", s2 = "dbbca";
// let s3 = "aadbbcbcac" //=>, return true.
// let s3 = "aadbbbaccc" //=> , return false.

// let s1 = "a", s2 = "b";
// let s3 = "ab" //=> , return false.
//

let s1 = "bbbbbabbbbabaababaaaabbababbaaabbabbaaabaaaaababbbababbbbbabbbbababbabaabababbbaabababababbbaaababaa", s2 = "babaaaabbababbbabbbbaabaabbaabbbbaabaaabaababaaaabaaabbaaabaaaabaabaabbbbbbbbbbbabaaabbababbabbabaab";
let s3 = "babbbabbbaaabbababbbbababaabbabaabaaabbbbabbbaaabbbaaaaabbbbaabbaaabababbaaaaaabababbababaababbababbbababbbbaaaabaabbabbaaaaabbabbaaaabbbaabaaabaababaababbaaabbbbbabbbbaabbabaabbbbabaaabbababbabbabbab" //=> , return false.

console.log(s1.length, s2.length, s3.length)
let res = isInterleave(s1, s2, s3);
console.log(res);