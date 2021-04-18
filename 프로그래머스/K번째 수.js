function solution(array, commands) {
    var answer = [];

    for (var command of commands){
        // 결과값 바로 answer에 추가
        answer.push(
            // 배열 자르기
            array.slice(command[0]-1, command[1])
            // 오름차순 정렬
            .sort(function (x, y) { return x-y })
            // 인덱스 선택
            [command[2]-1]
        );
    };
    return answer;
}