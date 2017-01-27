/**
 * Created by jmartin on 1/6/17.
 */
const orderWeight = (s) => {
    try {
        return s.split(" ")
            .map(w => [w, parseInt(w.split("").reduce((prev, cur) => parseInt(cur) + parseInt(prev)))])
            .sort((a, b) => {
                if (a[1] > b[1]) { return 1; }
                else if (b[1] > a[1]) { return -1; }
                else if (a[1] === b[1]) {
                    if (a[0] > b[0]) { return 1; }
                    else if (b[0] > a[0]) { return -1; }
                    else { return 0; }
                }
            })
            .reduce((prev, cur) => prev + cur[0] + ' ', '')
            .trim();
    }
    catch(e) {
        return '';
    }
};