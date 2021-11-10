package 슬라이딩윈도우.최대_슬라이딩_윈도우;

import java.util.*;

public class Solution {
	public int[] solution(int[] nums, int k) {
		List<Integer> result = new ArrayList<Integer>();
		for (int i = 0; i < nums.length - k + 1; i++) {
			int[] split = Arrays.copyOfRange(nums, i, i + k);
			result.add(Arrays.stream(split).max().orElse(0));
		}
		int[] result_int = new int[result.size()];
		for (int i = 0; i < result.size(); i++) {
			result_int[i] = result.get(i).intValue();
		}
		return result_int;
	}

	public int[] solution2(int[] nums, int k) {
		List<Integer> result = new ArrayList<Integer>();
		Queue<Integer> queue = new LinkedList<Integer>();
		for (int i = 0; i < nums.length - k + 1; i++) {
			int[] split = Arrays.copyOfRange(nums, i, i + k);
			result.add(Arrays.stream(split).max().orElse(0));
		}
		int[] result_int = new int[result.size()];
		int size = result.size();
		for (int i = 0; i < size; i++) {
			result_int[i] = result.get(i).intValue();
		}
		return result_int;
	}

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Solution s = new Solution();
		int[] nums = { 1, 3, -1, -3, 5, 3, 6, 7, 1, 1, 1 };
		System.out.println(Arrays.toString(s.solution(nums, 3)));
		System.out.println(Arrays.toString(s.solution2(nums, 3)));
	}
}
