import java.util.ArrayList;
import java.util.Collections;
import java.util.List;
import java.util.Scanner;

public class Main {
	private static void solution(int sizeOfMatrix, int[][] matrix) {
		// 영역의 개수를 저장할 변수
		int count = 0;
		// 영역별 크기를 저장할 리스트
		List<Integer> count_size = new ArrayList<>();
		
		for(int i=0; i<sizeOfMatrix; i++) {
			for(int j=0; j<sizeOfMatrix; j++) {
				if(matrix[i][j] == 1) {
					// 영역별 크기를 리턴받아 add함
					count_size.add(dfs(sizeOfMatrix, matrix, i, j));
					// 영역 개수 증가
					count++;
				}
			}
		}
		// 출력
		System.out.println(count);
		Collections.sort(count_size);
		count_size.stream().forEach(i->{
			System.out.print(i + " ");
		});
	}
	
	private static int dfs(int sizeOfMatrix, int[][] matrix, int i, int j) {
		if(i<0 || i>= sizeOfMatrix ||
				j<0 || j>= sizeOfMatrix ||
				matrix[i][j] != 1) {
			return 0;
		}
		
		matrix[i][j] = -1;
		int count = 1;
		count += dfs(sizeOfMatrix, matrix, i+1, j);
		count += dfs(sizeOfMatrix, matrix, i-1, j);
		count += dfs(sizeOfMatrix, matrix, i, j+1);
		count += dfs(sizeOfMatrix, matrix, i, j-1);
		return count;
	}
	
	private static class InputData{
		int sizeOfMatrix;
		int[][] matrix;
	}
	
	private static InputData processStdin() {
		InputData inputData = new InputData();
		
		try(Scanner scanner = new Scanner(System.in)){
			inputData.sizeOfMatrix = Integer.parseInt(scanner.nextLine().replaceAll("\\s+", ""));
			inputData.matrix = new int[inputData.sizeOfMatrix][inputData.sizeOfMatrix];
			for (int i = 0; i < inputData.sizeOfMatrix; i++) {
				String[] buf = scanner.nextLine().trim().replaceAll("\\s+", " ").split(" ");
				for(int j=0; j<inputData.sizeOfMatrix; j++) {
					inputData.matrix[i][j] = Integer.parseInt(buf[j]);
				}
			}
		}catch(Exception e) {
			throw e;
		}
		return inputData;
	}
	
	public static void main(String[] args) {
		/*
입력 데이터
6
0 1 1 0 0 0
0 1 1 0 1 1
0 0 0 0 1 1
0 0 0 0 1 1
1 1 0 0 1 0
1 1 1 0 0 0

출력
3
4 5 7
		 */
		InputData inputData = processStdin();
		solution(inputData.sizeOfMatrix, inputData.matrix);
	}
}
