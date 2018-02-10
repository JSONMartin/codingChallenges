//  https://www.codela.io/challenges/5a6f027a840eaee691e1ec64/program-to-delete-vowels-from-a-string
const solution = str => str.split('').filter(letter => !'AEIOU'.includes(letter.toUpperCase())).join('');
