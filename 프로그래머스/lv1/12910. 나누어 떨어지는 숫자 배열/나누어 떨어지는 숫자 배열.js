function solution(arr, divisor) {
    arr.sort(function compare(a, b) {
        return a - b;
    });
    var answer = [];
    for (var i = 0; i < arr.length; i++) {
        if(arr[i]%divisor === 0){
            answer.push(arr[i])
        }
    }if (answer == ""){
        answer.push(-1)
    }
    return answer;
}