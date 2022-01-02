package timecheck;

public class Solution {
	@TimeCheck
	public static int solution(int num) {
		for(int i=0; i<2; i++) {
			try {
				Thread.sleep(1000);
				System.out.println("test " + num);
			} catch (InterruptedException e) {
				// TODO Auto-generated catch block
				e.printStackTrace();
			}
		}
		return num;
	}
	
	public static void main(String[] args) {
		new TimeCheckService(new Solution(), 10);
	}
}
