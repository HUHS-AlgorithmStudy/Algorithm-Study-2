function solution(priorities, location) {
    let copyArr = new Array(priorities.length);
    copyArr.fill(0);
    copyArr[location] = 1;
    let count = 0;

    while (true) {
        let now = priorities.shift();
        let copyNow = copyArr.shift();
        if (now < Math.max(...priorities)) {
            priorities.push(now);
            copyArr.push(copyNow);
        }
        else {
            count += 1;
            if (copyNow === 1) {
                return count;
            }
        }
    }
}
