const double = arr => arr.map(x => x * 2)
const add = arr => arr.reduce((prev, cur) => prev + cur)


$("#btn").on('click', e => {
    this.toggleClass('highlight')
    this.val = this.val === 'Add Highlight' ? 'Remove Highlight' : 'Add Highlight'
})

//////////////// TESTS
let res = double([1, 2, 3])
console.log(res);