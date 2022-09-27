function solution(n) {
    n = n.toString(3).split('').reverse().join('');
    console.log(n);
    console.log(Number.parseInt(n, 3));
    return Number.parseInt(n, 3);
}