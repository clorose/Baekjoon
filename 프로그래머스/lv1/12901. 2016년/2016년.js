function solution(a, b) {
    let day= new Date('2016',a-1,b).toDateString().slice(0,3).toUpperCase();
    return day;
}