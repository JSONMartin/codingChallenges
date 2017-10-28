/**
Last chair standing: 31

Chair removal order: [1,3,6,10,15,21,28,36,45,55,66,78,91,8,26,44,63,83,5,32,57,82,13,43,74,9,47,81,23,64,4,53,97,51,99,59,17,73,37,96,69,39,14,87,68,50,35,27,20,18,19,25,34,49,67,86,12,54,88,38,84,46,100,77,61,48,41,52,65,85,16,71,24,93,80,89,98,40,94,75,76,7,62,58,90,56,72,33,92,2,11,29,70,22,79,95,30,42,60]
*/
const NUM_CHAIRS = 100

// Each chair is a member of a Doubly Linked List, where every chair has a reference to the one before & after itself
class Chair {
    constructor(number) {
        this.number = number
        this.next = null
        this.prev = null
    }
    remove() {
        this.prev.next = this.next
        this.next.prev = this.prev
    }
}

// Automatically build Linked List containing desired number of chairs, with an accessor iterator
const chairs = (n => {
    let lastChair = firstChair = new Chair(1)

    for (let i = 2; i < n + 1; i++) {
        lastChair.next = new Chair(i)
        lastChair.next.prev = lastChair
        lastChair = lastChair.next
    }

    lastChair.next = firstChair
    firstChair.prev = lastChair

    return {
        *[Symbol.iterator]() { // Iterator that continues going around in a circle until it is the last chair (allows [for...of] syntax)
            const isLastChair = chair => chair === chair.next && chair === chair.prev // If the previous and next chair is itself, it is the last chair!
            let currentChair = firstChair

            while(!isLastChair(currentChair)) {
                yield currentChair
                currentChair = currentChair.next
            }

            yield currentChair // Yield the final remaining chair
        },
    }
})(NUM_CHAIRS)

const lastChairStanding = () => {
    let removeCounter = currentCounter = 1
    let chairRemovedOrderList = []

    for (var chair of chairs) {
        if (currentCounter === removeCounter) {
            chairRemovedOrderList.push(chair.number)
            chair.remove()
            currentCounter = 1
            removeCounter++
        } else {
            currentCounter++
        }
    }

    console.log("Last chair standing:", chair.number)
    console.log(`Chair removal order: [${chairRemovedOrderList.toString()}]`)
}

lastChairStanding()
