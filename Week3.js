function solution(number, k) {
    let arr = new Array();
    for (let i = 0; i < number.length; i++) {
        arr.push(number.slice(i, i + 1))
    }

    function getAllCases(arr, selectNumber) {
        const results = [];
        if (selectNumber === 1) return arr.map((value) => [value]);

        arr.forEach((fixed, index, origin) => {
            const rest = origin.slice(index + 1);
            const combinations = getAllCases(rest, selectNumber - 1);
            const attached = combinations.map((combination) => [fixed, ...combination]);
            results.push(...attached);
        });

        return results;
    }

    let allCasesArr = getAllCases(arr, arr.length - k);

    for (let i = 0; i < allCasesArr.length; i++) {
        let strCasesArr = '';
        for (let j = 0; j < allCasesArr[i].length; j++) {
            strCasesArr += allCasesArr[i][j];
        }
        allCasesArr[i] = parseInt(strCasesArr);
    }

    return Math.max(...allCasesArr).toString();
}
