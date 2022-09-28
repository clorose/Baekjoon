function solution(arr) {
    var answer = [];
    for(let i=0;i<arr.length;i++){
        if(arr[i] !== arr[i+1] && i<arr.length){
            answer.push(arr[i])
        }
    }
    return answer;
}