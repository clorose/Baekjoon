function solution(n) {
    root_n = Math.sqrt(n);
    if (root_n % 1 === 0) {
        return (root_n+1) * (root_n+1);
    }else{
        return -1;
    }
}