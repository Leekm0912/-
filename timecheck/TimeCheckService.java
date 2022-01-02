package timecheck;

import java.lang.reflect.Method;

public class TimeCheckService {
	public static void main(String[] args) {
		// Service 클래스로부터 메소드 정보를 얻음
		Solution solution = new Solution();
		Method[] declaredMethods = solution.getClass().getDeclaredMethods();

		// Method 객체를 하나씩 처리
		for (Method method : declaredMethods) {
			// PrintAnnotation이 적용되었는지 확인
			if (method.isAnnotationPresent(TimeCheck.class)) {
				long beforeTime = System.currentTimeMillis(); // 시작시간 측정
				Object result = null;
				try {
					// 메소드 호출
					result = method.invoke(solution);
				} catch (Exception e) {
				} finally {
					long afterTime = System.currentTimeMillis(); // 코드 실행 후의 시간 측정
					// 메소드 이름 출력
					System.out.println("[" + method.getName() + "] ");
					System.out.println("실행결과 : " + result);
					System.out.println("실행시간(ms) : " + (afterTime - beforeTime));

				}
				System.out.println();

			}
		}
	}
}
