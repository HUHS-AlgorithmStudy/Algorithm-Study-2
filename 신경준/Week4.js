function solution(n, left, right) {
    let answer = new Array();

    for (let i = left; i <= right; i++) {
        let share = parseInt(i / n) + 1; //몫
        let remain = i % n + 1; //나머지

        if (share < remain) {
            answer.push(remain)
        }
        else {
            answer.push(share);
        }
    }

    return answer;
}