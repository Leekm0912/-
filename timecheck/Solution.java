package timecheck;

public class Solution {
	@TimeCheck
	public int solution() {
		for(int i=0; i<2; i++) {
			try {
				Thread.sleep(1000);
				System.out.println("sleep");
			} catch (InterruptedException e) {
				// TODO Auto-generated catch block
				e.printStackTrace();
			}
		}
		return 1;
	}
}
