function solution(number, k) {
  let str = '';
  let lastIndex = 0;

  while(k > 0) {
    const nums = number.slice(lastIndex, lastIndex + k + 1);
    let max = 0;
    let index = 0;
    for (let i=0; i<nums.length; i++) {
      const n = Number(nums[i]);
      if (max < n) {
        max = n;
        index = i;
        if (max === 9) break;
      }
    }

    lastIndex += index + 1;
    k -= index;

    str += max.toString();

    if (number.length - lastIndex === k) {
      lastIndex = number.length;
      break;
    }
  }

  str += number.slice(lastIndex);
  return str;
}
