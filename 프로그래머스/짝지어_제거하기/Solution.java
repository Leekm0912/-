package programers.짝지어_제거하기;

import java.util.*;

public class Solution {
	public int solution(String s) {
		char next = '\0';
		char now = '\0';
		boolean end = false;
		String save = null;
		while (!end) {
			if (s.length() == 0) {
				return 1;
			}
			save = s;
			end = true;
			for (int i = 0; i < s.length(); i++) {
				if (i + 1 < s.length()) {
                    now = s.charAt(i);
					next =s.charAt(i+1);
					//System.out.println("now : " + now + " next : " + next);
					if (now == next) {
						save = s.substring(0, i) + s.substring(i + 2);
						//System.out.println("save : " + save);
						end = false;
					}
				}
			}
			s = save;
		}
		return 0;
	}
	
	public int solution2(String s) {
		Stack<Character> stack = new Stack<>();
		for(char c : s.toCharArray()) {
			if(stack.isEmpty()) {
				stack.add(c);
			}else if(stack.peek() == c){
				stack.pop();
			}else {
				stack.add(c);
			}
		}
		return stack.isEmpty() ? 1 : 0;
	}
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Solution s = new Solution();
		System.out.println(s.solution("baabaa")); // 1
		System.out.println(s.solution("cdcd")); // 0
		System.out.println(s.solution("abbcdaadca")); // 1
		System.out.println(s.solution2("baabaa")); // 1
		System.out.println(s.solution2("cdcd")); // 0
		System.out.println(s.solution2("abbcdaadca")); // 1
	}
}
