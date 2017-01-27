/**
 * Created by jmartin on 1/10/17.
 */

const findUniq = arr => {
    let last = null;

    for (let s of arr) {
        let uniques = [...new Set(s.toUpperCase())].join(''),
            charCodeTotal = uniques.split('').reduce((prev, cur) => prev + cur.charCodeAt(0), 0);

        if (last !== null && charCodeTotal !== last) {
            return s;
        }

        last = charCodeTotal;
    }
};

// First solution, too slow:

// function findUniq(arr) {
//     let seen = {};
//
//     arr.map(s => [...new Set(s.toUpperCase())].join(''))
//         .forEach((s, idx) => {
//             let str = s.toLowerCase();
//             str.split('').forEach(ch => {
//                seen[ch] = !!seen[ch] ? [...seen[ch], idx] : [idx];
//             });
//         });
//
//     for (let ch in seen) {
//         if (seen[ch].length === 1) {
//             return arr[seen[ch][0]];
//         }
//     }
// }

//////////////
// Tests
//////////////

let res = findUniq([ 'Aa', 'aaa', 'aaaaa', 'BbBb', 'Aaaa', 'AaAaAa', 'a' ]);
res = findUniq([ 'abc', 'acb', 'bac', 'foo', 'bca', 'cab', 'cba' ]);
res = findUniq([ '', '', '', 'a', '', '' ]);
console.log(res);

/*
 Test.assertEquals(findUniq([ 'Aa', 'aaa', 'aaaaa', 'BbBb', 'Aaaa', 'AaAaAa', 'a' ]), 'BbBb');
 Test.assertEquals(findUniq([ 'abc', 'acb', 'bac', 'foo', 'bca', 'cab', 'cba' ]), 'foo');
 Test.assertEquals(findUniq([ 'silvia', 'vasili', 'victor' ]), 'victor');
 Test.assertEquals(findUniq([ 'Tom Marvolo Riddle', 'I am Lord Voldemort', 'Harry Potter' ]), 'Harry Potter');
 */