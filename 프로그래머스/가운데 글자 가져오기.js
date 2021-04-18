function solution(s) {
    if(s.length % 2 == 0){
        return s.slice(s.length/2-1,(s.length/2)+1);
    }else{
        console.log()
        return s[parseInt(s.length/2)];
    }
}