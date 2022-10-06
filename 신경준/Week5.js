function solution(n) {
    let answer = '';
    while (true) {
        if ((n % 3) === 0) {
            n = n - 1;
            let remain = 4;
            answer = remain.toString() + answer;
        }

        else {
            let remain = parseInt(n % 3);
            answer = remain.toString() + answer;
        }
        n = parseInt(n / 3);
        if (n < 3) {
            if (n != 0) {
                answer = n + answer;
            }
            break;
        }
    }

    return answer;
}
