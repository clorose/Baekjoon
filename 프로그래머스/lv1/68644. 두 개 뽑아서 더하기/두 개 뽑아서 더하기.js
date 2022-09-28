function solution(numbers) {
    let temp = [];
    for (let i = 0; i < numbers.length; i++) {
        for(let j = i; j < numbers.length; j++){
            if(i<numbers.length-1 && i!==j){
                temp.push(numbers[i]+numbers[j])
            }
        }
    }
    let answer = [...new Set(temp)];
    return answer.sort((a,b)=>a-b)
}