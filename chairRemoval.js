const NUM_CHAIRS = 100

// Each chair is a member item of a doubly linked list, where each chair is linked to the one before and after itself
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

// Build Linked List containinig number of chairs, with an iterator.
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
        // Iterator that continues going around the chain until it is the last chair (allows [for...of])
        *[Symbol.iterator]() {
            const isLastChair = chair => chair === chair.next && chair === chair.prev // If the previous and next chair is itself, it is the last chair
            let current = firstChair

            while(!isLastChair(current)) {
                yield current;
                current = current.next
            }

            yield current
        },
    };
})(NUM_CHAIRS);

const lastChairStanding = () => {
    let remove = counter = 1
    let chairRemovedOrder = []

    for (var chair of chairs) {
        console.log(`CHAIR #: ${chair.number} | Remove:${remove} | COunteR:${counter} | Length:${chairRemovedOrder.length}`)
        
        if (counter === remove) {
            console.log("Chair removed:", chair.number);
            chairRemovedOrder.push(chair.number);
            // chairs.removeChair(chair);
            chair.remove();
            counter = 1;
            remove++;
            console.log(chairRemovedOrder);
            console.log("-----------------------------------------------------------------------");
        } else {
            counter++;
        }
    }

    let res = chairRemovedOrder.toString()
    console.log(res);
    console.log("Remaining chair:", chair);
}

lastChairStanding();
// let remove = 1;
// let counter = 1;

// const chairRemovedOrder = [];

// let chair = chairs.head;

// for (chair of chairs) {
//     console.log(`CHAIR #: ${chair.number} | Remove:${remove} | COunteR:${counter} | Length:${chairRemovedOrder.length}`)
//     if (counter === remove) {
//         console.log("Chair removed:", chair.number);
//         chairRemovedOrder.push(chair.number);
//         chairs.removeChair(chair);
//         counter = 1;
//         remove++;
//         console.log(chairRemovedOrder);
//         console.log("-----------------------------------------------------------------------");
//     } else {
//         counter++;
//     }
// }