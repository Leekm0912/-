function solution(n, lost, reserve) {
    // 여분 - 도난 차집합
    var new_reserve = reserve.filter(x => !lost.includes(x));
    // 도난 - 여분 차집합
    var new_lost = lost.filter(x => !reserve.includes(x));

    for(var i of new_lost){
        // 뒷번호
        var b = i-1;
        // 앞번호
        var f = i+1;

        // 도난당한 번호의 앞 or 뒤 번호가 있는지 확인
        // 있으면 여분리스트에서 삭제
        if(new_reserve.includes(f)){
            // f에 해당하는 인덱스를 찾아서 삭제한다.
            new_reserve.splice(new_reserve.indexOf(f),1);
        }else if(new_reserve.includes(b)) {
            // b에 해당하는 인덱스를 찾아서 삭제한다.
            new_reserve.splice(new_reserve.indexOf(b),1);
        }else{ // 없으면 총원에서 -1
            n--;
        }
    }
    return n;
}