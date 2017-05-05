function* someSyncGenerator() {
    yield 1;
    yield 2;
    yield 3;
}

function mainSync() {
    let generator = someSyncGenerator();
    
    // Method 1
    let next = generator.next();

    while (!next.done) {
        console.log(next);
        next = generator.next();
    }

    // Method 2
    generator = someSyncGenerator();

    for (let value of generator) {
        console.log(value);
    }
}

//mainSync();


// Async improved version - Needs to be ran through transpiler
Symbol.asyncIterator = Symbol.asyncIterator || Symbol("asyncIterator") // Polyfill for proper use

const delay = (ms) => new Promise(resolve => {
    setTimeout(resolve, ms)
})

async function* someGenerator() {
    await delay(1000)
    yield 1

    await delay(1000)
    yield 2

    await delay(1000)
    yield 3
}

async function mainAsyncForAwait() {
    for await (const value of someGenerator()) {
        console.log(value)
    }
}
// Is equivelant to...
async function mainAsync() {
    const generator = someGenerator();

    while (true) {
        const { value, done } = await generator.next();
        if (done) {
            break;
        }
        console.log(value);
    }
}

mainAsync()