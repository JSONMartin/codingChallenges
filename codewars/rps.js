// https://www.codewars.com/kata/5672a98bdbdd995fad00000f/train/javascript
const rps = (p1, p2) => {
    const p1Won = 'Player 1 won!';
    const p2Won = 'Player 2 won!';

    if (p1 === p2) return 'Draw!';
    switch (p1) {
        case 'scissors':
            switch (p2) {
                case 'paper':
                    return p1Won;
                case 'rock':
                    return p2Won;
            }
        case 'rock':
            switch (p2) {
                case 'scissors':
                    return p1Won;
                case 'paper':
                    return p2Won;
            }
        case 'paper':
            switch (p2) {
                case 'rock':
                    return p1Won;
                case 'scissors':
                    return p2Won;
            }
    }
};
