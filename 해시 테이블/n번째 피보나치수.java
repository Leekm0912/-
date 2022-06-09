package algo.q2747;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.HashMap;
import java.util.Map;
import java.util.StringTokenizer;

public class Main {
	public static void main(String[] args) throws IOException {
		// 피보나치 수

		// 여러 개의 데이터 입력받기
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in)); // 선언
//		String s2[] = br.readLine().split(" "); // split을 이용해 다량의 데이터 입력 받기

		StringTokenizer st = new StringTokenizer(br.readLine(), " ");
//		int arr[] = new int[st.countTokens()];
//		int count = 0;
//		while (st.hasMoreTokens()) {
//			arr[count] = Integer.parseInt(st.nextToken());
//			System.out.println(arr[count++]);
//			// countTokens() : 총 토큰의 개수를 리턴
//			// hasMoreTokens() : 토큰이 남아있다면 true, 없으면 false 리턴
//
//		}

		int num = Integer.parseInt(st.nextToken());
		br.close();

		boolean[] data = new boolean[num+1];
		data[0] = true;
		data[1] = true;

		Map<Integer, Integer> map = new HashMap<>();
		map.put(0, 0);
		map.put(1, 1);

		System.out.println(fibo(map, num));
	}

	public static int fibo(Map<Integer, Integer> map, int num) {
    // 계산해놓은 피보나치 수가 없으면 계산하고, 있으면 바로 리턴
		if (!map.containsKey(num)) {
			map.put(num, fibo(map, num - 1) + fibo(map, num - 2));
		}
		return map.get(num);
	}
}
