function solution(skill, skill_trees) {
    var answer = 0;

    // 스킬트리를 배열로 쪼개줌
    var skill_tree_arr =[];

    for (var i of skill_trees){
        skill_tree_arr.push(i.split(""));
    }

    // index와 스킬트리 순서를 매핑시켜줌
    var map_arr = new Array();

    skill_tree_arr.forEach((s1Value,s1Index)=>{
        // 새로운 Map을 만들고
        map_arr.push(new Map());

        s1Value.forEach((value, Index) => {
            // Map에 Index : 스킬트리 순서로 매핑
            map_arr[s1Index].set(Index,skill.indexOf(value));
        });
    });

    // 스킬트리 순서에 맞는지 확인.
    // map_arr 순회
    map_arr.forEach((map)=>{
        // 현재 찍을수있는 스킬트리 0으로 초기화
        var now_skill = 0;

        // map 순회
        map.forEach((v)=>{
            // -1이면 continue나 break 해주고싶은데
            // js는 forEach에 continue나 break가 없다네; forEach말고 for문으로 바꿔봐야겠음

            // index값이 -1이 아니고, 현재 찍을수 있는 스킬보다 값이 높다면
            if (v != -1 & v > now_skill){
                // -1 대입(나중에 걸러줄꺼임)
                now_skill = -1;
            }
            // index값이 -1이 아니고, 현재 찍을수있는 스킬이라면
            else if(v != -1 & v == now_skill){
                // 스킬트리 +1 해줌
                now_skill+=1;
            }
        });
        // map을 하나 순회한 후 값이 -1이 아니라면 정상적인 스킬트리.
        if(now_skill != -1){
            // 정답 +1 해줌
            answer++;
        }
    });

    return answer;
}
