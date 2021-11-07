package programers.스코빌지수;

import java.util.*;

public class Solution {
	public int solution(int[] scoville, int K) {
        int answer = 0;
        // heap 생성
        PriorityQueue<Integer> minHeap = new PriorityQueue<Integer>();
        // heap에 추가.
        for(int i : scoville) {
        	minHeap.add(i);
        }
        // heap의 사이즈가 1보다 작아지면 다 섞어도 K보다 작은거. 종료.
        // 그리고 가장 작은 값이 K보다 커지면 종료.
        while(minHeap.size() > 1 && minHeap.peek() < K) {
        	int first_low = minHeap.remove();
        	int second_low = minHeap.remove();
        	minHeap.add(first_low + (second_low * 2));
        	answer++;
        }
        System.out.println(minHeap);
        return minHeap.size() > 1 || minHeap.peek() > K ? answer : -1;
    }
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Solution s = new Solution();
		System.out.println(s.solution(new int[]{1, 2, 3, 9, 10, 12}, 7)); // 2
	}

}
