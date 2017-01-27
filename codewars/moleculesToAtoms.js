/**
 * Created by jmartin on 1/10/17.
 */
// https://www.codewars.com/kata/molecule-to-atoms/train/javascript // 3 kyu!
/*
 For a given chemical formula represented by a string, count the number of atoms of each element contained in the molecule and return an object.

 For example:

 var water = 'H2O';
 parseMolecule(water); // return {H: 2, O: 1}

 var magnesiumHydroxide = 'Mg(OH)2';
 parseMolecule(magnesiumHydroxide); // return {Mg: 1, O: 2, H: 2}

 var fremySalt = 'K4[ON(SO3)2]2';
 parseMolecule(fremySalt); // return {K: 4, O: 14, N: 2, S: 4}
 As you can see, some formulas have brackets in them. The index outside the brackets tells you that you have to multiply count of each atom inside the bracket on this index. For example, in Fe(NO3)2 you have one iron atom, two nitrogen atoms and six oxygen atoms.

 Note that brackets may be round, square or curly and can also be nested. Index after the braces is optional.
 */

function parseMolecule(formula, multiplier = 1) {
    const matchDict = {
        ')': '(',
        '}': '{',
        ']': '['
    };

    let moleculeDict = {}, parts = [],
        currentElement = "", currentNum = "";

    const saveNum = () => {
        currentNum = currentNum || 1;
        moleculeDict[currentElement] = moleculeDict[currentElement] ? moleculeDict[currentElement] + parseInt(currentNum) : parseInt(currentNum);
        currentElement = "";
        currentNum = "";
    };

    formula = formula.split('');

    while (formula.length > 0) {
        let ch = formula.pop();

        if (/[0-9]/.test(ch)) { // Number found (multiplier)
            currentNum = ch + currentNum;
            while (/[0-9]/.test(formula[formula.length - 1])) {
                ch = formula.pop();
                currentNum = ch + currentNum;
            }
        }
        else if (/[)\]}]/.test(ch)) {
            let idx = formula.length - 1;
            while (formula[idx] !== matchDict[ch]) {
                idx--;
            }

            parts = [...formula.slice(idx), ch];
            let partsSlice = parts.slice(1, parts.length - 1);
            let segmentResults = parseMolecule(partsSlice.join(''), parseInt(currentNum) || 1);

            for (let r in segmentResults) {
                moleculeDict[r] = moleculeDict[r] ? moleculeDict[r] + segmentResults[r] : segmentResults[r];
            }

            formula = formula.slice(0, idx);
            currentNum = "";
        }
        else if (/[a-z]/.test(ch)) { // Lowercase Letter found
            currentElement = formula.pop() + ch;
            saveNum();
        }
        else if (/[A-Z]/.test(ch)) {
            currentElement = ch;
            saveNum();
        }
        else {
            formula.pop();
        }
    }

    for (let l in moleculeDict) {
        moleculeDict[l] = parseInt(parseInt(moleculeDict[l]) * multiplier);
    }

    return moleculeDict;
}

// Tests

//var water = 'H2O';
//parseMolecule(water);

//var magnesiumHydroxide = 'Mg(OH)2'; //var magnesiumHydroxide = '(OH)';
//let res = parseMolecule(magnesiumHydroxide); // return {Mg: 1, O: 2, H: 2}


//var fremySalt = 'K4[ON(SO3)2]2';
//let res = parseMolecule(fremySalt); // return {K: 4, O: 14, N: 2, S: 4}

let res = parseMolecule("(C5H5)Fe(CO)2CH3");

console.log(res);
