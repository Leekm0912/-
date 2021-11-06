package chap05_project;

import java.util.Random;
import java.util.Scanner;

public class Nomal extends Thread {
	public int threadNum;
	public Share share;

	public Nomal(String threadName, int threadNum, Share share) {
		this.threadNum = threadNum;
		this.setName(threadName);
		this.share = share;
	}

	@Override
	public void run() {
		System.out.println("thread" + threadNum + " start");

		System.out.println(" Enter Critical Section." + "\tThread" + threadNum);
		/*
		 * 임계영역 코드는 여기에 작성
		 */
		System.out.println(" Exit Critical Section." + "\t\tThread" + threadNum);
	}

	public static void main(String[] args) {
		System.out.println("알고리즘 X");
		Scanner sc = new Scanner(System.in);
		System.out.print("프로그램에 참여 할 스레드의 개수 입력 : ");
		int n = sc.nextInt();
		Share share = Share.getInstance(n);

		for (int i = n - 1; i >= 0; --i) {
			Thread th = new Nomal(Integer.toString(i), i, share);
			th.start();
		}
	}

}
