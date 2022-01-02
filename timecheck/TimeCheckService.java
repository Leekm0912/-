package timecheck;

import java.lang.reflect.Method;

public class TimeCheckService {
	public TimeCheckService(Object o, Object... args) {
		// 파라미터로부터 리플렉션을 통해 메소드 정보를 얻음
		Method[] declaredMethods = o.getClass().getDeclaredMethods();

		// Method 객체를 하나씩 처리
		for (Method method : declaredMethods) {
			// TimeCheck 어노테이션이 적용되었는지 확인
			if (method.isAnnotationPresent(TimeCheck.class)) {
				Object result = null;
				long beforeTime = System.currentTimeMillis(); // 시작시간 측정
				try {
					// 메소드 호출
					result = method.invoke(o.getClass().getDeclaredConstructor().newInstance(), args);
				} catch (Exception e) {
				} finally {
					long afterTime = System.currentTimeMillis(); // 코드 실행 후의 시간 측정
					// 메소드 이름 출력
					System.out.println("[" + method.getName() + "] ");
					System.out.println("실행결과 : " + result);
					System.out.println("실행시간(ms) : " + (afterTime - beforeTime));
				}
			}
		}
	}
}
