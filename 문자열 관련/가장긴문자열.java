package stream;

import java.util.Arrays;

public class 가장긴문자열 {
	public static void main(String[] args) {
		String[] str = { "1", "12345", "12", "문자여얼"};
		System.out.println(longestString(str));
	}

	public static String longestString(String... s) {
		return Arrays.stream(s).sorted((x, y) -> {
			return y.length() - x.length(); // 길이순 내림차순 정렬
		}).toArray(String[]::new)[0];
	}
}
