function solution(board, moves) {
    var answer = 0;
    var main_stack = [];

    for (var i = 0; i < moves.length; i++) {
        var move = moves[i]-1;
        var peek_main;
        var peek_data = -1; // 초기값을 -1로 줘서 peek데이터 있는지 판단
        
        // main_stack의 마지막항목 가져오기
        if (main_stack.length != 0) {
            peek_main = main_stack[main_stack.length - 1];
        }

        // 선택한 스택의 마지막항목 가져오기 0이면 무시
        for (var j = 0; j < board.length; j++) {
            if (board[j][move] != 0) {
                peek_data = board[j][move];
                board[j][move] = 0;
                break;
            }
        }
        
        // peek_daka가 -1이면 가져온 값이 없다는거니 continue해줌.
        if (peek_data == -1) {
            continue;
        }
        
        // main_stack의 마지막 항목과 넣은 항목이 같다면
        if (peek_main == peek_data) {
            // 마지막 항목 제거 후 터트린개수 +2
            main_stack.pop();
            answer += 2;
        } else {
            // 스택에 추가
            main_stack.push(peek_data);
        }
    }

    return answer;
}