function solution(answers) {
    var answer = [];

    function answers_return(len, pattern){
        // 길이만큼 반복
        var count = 0;
        var result = [];
        while(count != len){
            // 나머지 연산을 이용해 패턴을 대입 후 count 증가
            result.push(pattern[count++ % pattern.length]);
        }
        return result;
    }

    function get_p1_pattern(len){
        var result = answers_return(len, [1,2,3,4,5]);
        return result;
    }

    function get_p2_pattern(len){
        var result = answers_return(len, [2,1,2,3,2,4,2,5]);
        return result;
    }

    function get_p3_pattern(len){
        var result = answers_return(len, [3,3,1,1,2,2,4,4,5,5]);
        return result;
    }

    var p1_pattern = get_p1_pattern(answers.length);
    var p2_pattern = get_p2_pattern(answers.length);
    var p3_pattern = get_p3_pattern(answers.length);

    // 수포자 정답 체크
    var right_answers_count = [0,0,0];

    // answers를 돌면서 정답이 맞는지 체크
    for(var i = 0; i< answers.length; i++){
        if(p1_pattern[i] == answers[i]){
            right_answers_count[0]++;
        }
        if(p2_pattern[i] == answers[i]){
            right_answers_count[1]++;
        }
        if(p3_pattern[i] == answers[i]){
            right_answers_count[2]++;
        }
    }

    // 최대점수 구하기
    var max = Math.max.apply(null, right_answers_count);

    // 최대 점수가 몇명인지 구하기 (최대점수가 아닌항목 삭제. 이후 length로 비교)
    var filtered = right_answers_count.filter(
        function (element, index, array) {return element == max;});

    // 필터링한 배열의 길이가 1이면 바로 최대값의 index구해서 push
    if(filtered.length == 1){
        answer.push(right_answers_count.indexOf(max)+1);
    }else{ //길이가 1이 아니라면 동점자 존재
        // right_answers_count돌면서 최대점수와 일치하는 인덱스 push
        for(var i=0; i<right_answers_count.length; i++){
            if(right_answers_count[i] == max){
                answer.push(i+1);
            }
        }
    }

    return answer;
}