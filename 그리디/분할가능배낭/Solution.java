package greedy;

import java.util.*;

public class Solution {

	public static double solution(List<double[]> cargo, int max_weight) {
		// 람다식 내부에서 쓰기위해 배열로 선언.
		double[] answer = {0.0};
		int[] max_weight_arr = {max_weight};
		
		List<double[]> pack = new ArrayList<>();
		
		cargo.stream().sorted((x, y)->{
			if(x[0] > y[0]) {
				return -1;
			}else if(x[0] == y[0]) {
				return 0;
			}else{
				return 1;
			}
		})
		.forEach(v->{
			pack.add(new double[] {v[0] / v[1], v[0], v[1]});
		});
		
		pack.stream().sorted((x, y)->{
			if(x[0] > y[0]) {
				return -1;
			}else if(x[0] == y[0]) {
				if(x[1] > y[1]) {
					return -1;
				}else if(x[1] == y[1]) {
					return 0;
				}else {
					return 1;
				}
			}else{
				return 1;
			}
		})
		.forEach(v->{
			if((max_weight_arr[0] - v[2]) > 0) {
				answer[0] += v[1];
				max_weight_arr[0] -= v[2];
			}else {
				double fraction = max_weight_arr[0] / v[2];
				answer[0] += v[1] * fraction;
				return;
			}
		});
		
		return answer[0];
	}
	
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		List<double[]> l = new ArrayList<>();
		// {가격, 무게} 배열
		l.add(new double[]{4, 12});
		l.add(new double[]{2, 1});
		l.add(new double[]{10, 4});
		l.add(new double[]{1, 1});
		l.add(new double[]{2, 2});
		
		System.out.println(solution(l, 15));
	}

}
