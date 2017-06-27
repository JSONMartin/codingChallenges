function sumConsecutives(s) {
    let results = s.reduce((prev, cur) => {
        let arr = prev[0]
        let curNum = prev[1]
        let total = prev[2]

        console.log(prev, cur);
        if (prev.length == 0) {
            prev = [cur]
        }
        else {
            if (cur == curNum) {
                total += cur
            }
            else {
                arr = [...arr, total]
                curNum = cur;
                total = cur;
            }
        }
        return [arr, curNum, total]
    }, [[], s[0], 0])

    let consecutives = results[0];
    consecutives.push(results[2])
    return consecutives;
}

console.log(sumConsecutives([1,1,7,7,3]));
console.log(sumConsecutives([-5,-5,7,7,12,0]));