package greedy;

import java.util.*;

import timecheck.TimeCheck;
import timecheck.TimeCheckService;

public class Solution {

	@TimeCheck
	public static double solution(List<double[]> cargo, int max_weight) {
		// 람다식 내부에서 쓰기위해 배열로 선언.
		double[] answer = {0.0};
		int[] max_weight_arr = {max_weight};

		// {단가, 가격, 무게} 순으로 새로 만들어 주기 위한 리스트.
		List<double[]> pack = new ArrayList<>();
		// {단가(가격/무게}, 가격, 무게} 형식으로 저장.
		cargo.stream()
		.forEach(v->{
			pack.add(new double[] {v[0] / v[1], v[0], v[1]});
		});

		// 단가 순으로 내림차순 정렬 후 그리디 계산.
		// 단가가 같다면 가격 순으로 내림차순 정렬.
		pack.stream()
		.sorted((x, y)->{
			if(x[0] > y[0]) {
				return -1;
			}else if(x[0] == y[0]) {
				// 단가가 같다면 가격을 기준으로 내림차순으로 정렬.
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
			// 가방에 모두 담을수 있다면 담음.
			if((max_weight_arr[0] - v[2]) > 0) {
				answer[0] += v[1];
				max_weight_arr[0] -= v[2];
			}
			// 가방에 담을수 없다면 쪼개서 담음.
			else {
				// 남은 무게 / 무게 로 비율을 구함.
				double fraction = max_weight_arr[0] / v[2];
				// 구한 비율만큼 결과에 추가.
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

		new TimeCheckService(new Solution(), l, 15);
	}
}
