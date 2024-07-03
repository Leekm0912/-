package lkm.baseball;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class Baseball {
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

		System.out.println("숫자야구 자리수 입력\n");
		String read = br.readLine();
		int length = Integer.parseInt(read);

		read = "";
		while (!("0".equals(read) || "1".equals(read))) {
			System.out.println("중복 허용 여부 입력 (0: 비허용, 1: 허용)\n");
			read = br.readLine();
		}
		boolean dupAllowed = "1".equals(read);

		read = "";
		while (!("0".equals(read) || "1".equals(read))) {
			System.out.println("0 허용 여부 입력 (0: 비허용, 1: 허용)\n");
			read = br.readLine();
		}
		boolean zeroAllowed = "1".equals(read);

		int[] answer = new int[length];
		List<char[]> inputList = new ArrayList<>();
		Map<Integer, Integer> numberMap = init(zeroAllowed);
		Map<Integer, char[]> resultMap = new HashMap<>();
		boolean isEnd = false;
		while(!isEnd) {
			System.out.println("검증할 숫자 입력\n");
			char[] nowInput = br.readLine().toCharArray();
			inputList.add(nowInput);

			System.out.println("결과 입력 ex) 1S2B : 12, out : 0\n");
			nowInput = br.readLine().toCharArray();

		}

	}

	private static Map<Integer, Integer> init(boolean zeroAllowed) {
		Map<Integer, Integer> numMap = new HashMap<>();
		for (int i = zeroAllowed ? 0 : 1; i <= 9; i++) {
			numMap.put(i, 0);
		}
		return numMap;
	}
}
