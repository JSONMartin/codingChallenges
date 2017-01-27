/**
 * Created by jmartin on 1/20/17.
 */

function longestConsec(strarr, k) {
    if (k <= 0 || k > strarr.length || !strarr) return "";

    try {
        strarr = strarr.map((el, idx) => [el, el.length]);

        let maxIdx = 0, maxes = [];

        for (let i = 0; i < strarr.length + 1 - k; i++) {
            let total = strarr.slice(i, i + k).map(x => parseInt(x[1])).reduce((prev, cur) => prev + cur, 0);
            maxes.push(total);
        }

        maxIdx = maxes.indexOf(Math.max(...maxes));

        return strarr.slice(maxIdx, maxIdx + k).map(x => x[0]).join('');
    } catch(e) {
        return "";
    }
}