function solution(lottos, win_nums) {
    var answer = [];
    let winning = win_nums.filter(it=>lottos.includes(it)).length;
    let zero = lottos.filter(lotto =>lotto === 0).length;
    let min = 7-winning >=6 ? 6: 7-winning;
    let max = min-zero < 1 ? 1 : min-zero;
    answer = [max,min]
    return answer;
}