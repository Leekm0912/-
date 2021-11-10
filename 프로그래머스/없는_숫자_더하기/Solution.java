package programers.없는_숫자_더하기;

import java.util.Arrays;

public class Solution {
	public int solution(int[] numbers) {
        return 45-Arrays.stream(numbers).sum();
    }
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Solution s = new Solution();
		System.out.println(s.solution(new int[] {1,2,3,4,6,7,8,0})); // 14
		System.out.println(s.solution(new int[] {5,8,4,0,6,7,9})); // 6
	}

}
