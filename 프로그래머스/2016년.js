function solution(a, b) {
    var day = ["SUN","MON","TUE","WED","THU","FRI","SAT"];
    // 자바스크립트는 월에서 -1 해줘야함(0월부터 시작)
    return day[new Date(2016,(a-1),b).getDay()];
}