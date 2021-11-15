package kakao.숫자문자열과영단어;

import java.util.*;

public class Solution {
	public int solution(String s) {
        Map<String, String> m = new HashMap<>();
        m.put("one", "1");
        m.put("two", "2");
        m.put("three", "3");
        m.put("four", "4");
        m.put("five", "5");
        m.put("six", "6");
        m.put("seven", "7");
        m.put("eight", "8");
        m.put("nine", "9");
        m.put("zero", "0");
        String result = "";
        String temp = "";
        for(int i=0; i<s.length(); i++) {
        	if(Character.isDigit(s.substring(i, i+1).charAt(0))) {
        		result += s.substring(i, i+1);
        	}else {
        		temp += s.substring(i, i+1);
        		if(m.containsKey(temp)) {
        			result += m.get(temp);
        			temp = "";
        		}
        	}
        }
//        System.out.println(result);
        return Integer.parseInt(result);
    }

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Solution s = new Solution();
		System.out.println(s.solution("one4seveneight"));
		System.out.println(s.solution("23four5six7"));
		System.out.println(s.solution("2three45sixseven"));
		System.out.println(s.solution("123"));
	}

}
