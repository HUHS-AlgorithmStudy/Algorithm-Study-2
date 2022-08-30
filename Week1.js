function fact(n) {
    let result = 1;
    for (let i = 2; i <= n; i++) {
        result *= i;
    }
    return result;
}

function week1(n) {
    let max_two = parseInt(n/2); //2의 최대개수
    let check = 0; //답 구하기전 변수

    for (let i = 0; i < max_two+1; i++) {
        let num_two = i; // 2의 개수
        let num_one = n - 2 * num_two;// 1의 개수

        let bunmo = fact(num_one+num_two); // 중복조합공식 에서 분모 즉, n!
        let bunja = fact(num_one)*fact(num_two);// 중복조합공식에서 분자 즉, (n-r)!*r!

        check += (bunmo/bunja);
    }

    let answer = check%1000000007;

    return answer;
}
