import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
	public static void main(String[] args) throws IOException {
		// 에라토스테네스의 채

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

		int start = Integer.parseInt(st.nextToken());
		int end = Integer.parseInt(st.nextToken());
//		System.out.println("" + start + end);
		br.close();

		boolean[] list = new boolean[end+1];
		list[0] = true;
		list[1] = true;
		
//		System.out.println(Arrays.toString(list));
		
		for (int i = 2; i < end; i++) {
			if(list[i] == false) {
				for(int j=2; j<end; j++) {
					// 오버플로우때문에 long으로.
					long check_num = i*j;
					if(check_num > end) {
						break;
					}
					if(list[(int) check_num] == false) {
						list[(int) check_num] =true;
					}
				}
			}
		}
		
		for(int i=start; i<end+1; i++) {
			if(list[i] == false)
				System.out.println(i);
		}
	}

}
