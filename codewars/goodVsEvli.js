/**
 * Created by jmartin on 1/12/17.
 */
// https://www.codewars.com/kata/good-vs-evil/train/javascript

/*
 Description

 Middle Earth is about to go to war. The forces of good will have many battles with the forces of evil. Different races will certainly be involved. Each race has a certain 'worth' when battling against others. On the side of good we have the following races, with their associated worth:

 Hobbits - 1
 Men - 2
 Elves - 3
 Dwarves - 3
 Eagles - 4
 Wizards - 10
 On the side of evil we have:

 Orcs - 1
 Men - 2
 Wargs - 2
 Goblins - 2
 Uruk Hai - 3
 Trolls - 5
 Wizards - 10
 Although weather, location, supplies and valor play a part in any battle, if you add up the worth of the side of good and compare it with the worth of the side of evil, the side with the larger worth will tend to win.

 Thus, given the count of each of the races on the side of good, followed by the count of each of the races on the side of evil, determine which side wins.

 Input:

 The function will be given two parameters. Each parameter will be a string separated by a single space. Each string will contain the count of each race on the side of good and evil.

 The first parameter will contain the count of each race on the side of good in the following order:

 Hobbits, Men, Elves, Dwarves, Eagles, Wizards.
 The second parameter will contain the count of each race on the side of evil in the following order:

 Orcs, Men, Wargs, Goblins, Uruk Hai, Trolls, Wizards.
 All values are non-negative integers. The resulting sum of the worth for each side will not exceed the limit of a 32-bit integer.

 Output:

 Return ""Battle Result: Good triumphs over Evil" if good wins, "Battle Result: Evil eradicates all trace of Good" if evil wins, or "Battle Result: No victor on this battle field" if it ends in a tie.
 */

// Order:
// Hobbits, Men, Elves, Dwarves, Eagles, Wizards.
// Orcs, Men, Wargs, Goblins, Uruk Hai, Trolls, Wizards.

function goodVsEvil(good, evil){
    let goodData = [
        // [Name, Worth, Num]
        ['Hobbits', 1],
        ['Men', 2],
        ['Elves', 3],
        ['Dwarves', 3],
        ['Eagles', 4],
        ['Wizards', 10]
    ],
    evilData = [
        ['Orcs', 1],
        ['Men', 2],
        ['Wargs', 2],
        ['Goblins', 2],
        ['Uruk Hai', 3],
        ['Trolls', 5],
        ['Wizards', 10]
    ];

    // Parse Data
    good.split(' ').forEach((n, idx) => {
        goodData[idx].push(parseInt(n));
    });

    evil.split(' ').forEach((n, idx) => {
        evilData[idx].push(parseInt(n));
    });

    // Compare results
    let goodScore = goodData.reduce((prev, cur) => prev + cur[2] * cur[1], 0),
        evilScore = evilData.reduce((prev, cur) => prev + cur[2] * cur[1], 0);

    return goodScore > evilScore ? "Battle Result: Good triumphs over Evil" :
           evilScore > goodScore ? "Battle Result: Evil eradicates all trace of Good" :
           "Battle Result: No victor on this battle field";
}


/*
TESTING
 */
goodVsEvil('1 1 1 1 1 1', '1 1 1 1 1 1 1')


/*
Test.expect( goodVsEvil('1 1 1 1 1 1', '1 1 1 1 1 1 1') === 'Battle Result: Evil eradicates all trace of Good', 'Evil should win' );
Test.expect( goodVsEvil('0 0 0 0 0 10', '0 1 1 1 1 0 0') === 'Battle Result: Good triumphs over Evil', 'Good should win' );
Test.expect( goodVsEvil('1 0 0 0 0 0', '1 0 0 0 0 0 0') === 'Battle Result: No victor on this battle field', 'Should be a tie' );
*/