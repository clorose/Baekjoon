function solution(n) {
    let answer = [];
    do {
        answer.push(n%10)
        n = parseInt(n / 10)
    } while (n > 0)
    return answer;
}