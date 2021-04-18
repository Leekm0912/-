function solution(numbers) {
    var answer = [];

    // 마지막칸은 계산할 필요 없음.
    for(var i=0; i<numbers.length-1; i++){
        // i의 한칸앞에서부터 차례대로 돌면서 대입
        for(var j = i+1; j<numbers.length; j++){
            var add = numbers[i]+numbers[j];
            // 배열에 더한값이 들어있지 않다면 -1 리턴
            if(answer.indexOf(add) == -1){
                // 배열에 추가
                answer.push(add);
            }
        }
    }
    // 오름차순 정렬
    answer.sort(function(a, b) { return a - b;});
    return answer;
}