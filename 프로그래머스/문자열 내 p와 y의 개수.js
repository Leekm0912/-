function solution(s) {
    // 개수를 세줄 변수
    var count_y = 0;
    var count_p = 0;

    // 문자 하나씩 검사
    for(var element of s){
        if(element == "p" | element == "P"){
            count_p++;
        }else if(element == "y" | element == "Y"){
            count_y++;
        }
    };

    // 개수가 같으면 true 아니면 false 리턴
    return count_p == count_y ? true : false;
}