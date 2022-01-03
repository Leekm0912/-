package greedy;

import java.util.*;

import timecheck.TimeCheck;
import timecheck.TimeCheckService;

public class 주식을사고팔기가장좋은지점 {
	@TimeCheck
	public static int solution(int[] data) {
		int answer = 0;

		for (int i = 0; i < data.length - 1; i++) {
			// 값이 오르면 구매
			if(data[i+1] > data[i]) {
				answer += data[i+1] - data[i];
			}
		}
		return answer;
	}

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		int[] data = { 7, 1, 5, 3, 6, 4 };

		new TimeCheckService(new 주식을사고팔기가장좋은지점(), data);
	}

}
