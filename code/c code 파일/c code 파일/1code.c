#include <stdio.h>
#include <stdlib.h>  // atoi, atof 함수 사용하기위한 라이브러리 stdlib.h

int main() {
	//1
	//printf("hello");
	//return 0;
	// 2
	//printf("hello, world\n");
	//printf("숫자 출력: %d\n", 10);
	// 3
	//int a = 20;
	//float b = 3.14;
	//char c = 'A';
	//printf("%d\n",a);
	//printf("%f\n",b);
	//printf("%c\n",c);
	// 4
	//int a;
	//	printf("나이를 입력하시요");
	//	scanf_s("%d", &a);
	//	printf("%d",a);
	// 5
	//int a;
	//printf("나이:");
	//scanf_s("%d", &a);*/
	//if (a == 3) {
	//	printf("진짜 짜증나네");
	//}
	//else {
	//	printf("에반데");
	//}
	// 6
	//int score;
		//printf("점수를 입력하세요: ");
		//scanf_s("%d", &score);
		//if (score >= 90) {
		//	printf("A 등급\n");
		//}
		//else if (score >= 80) {
		//	printf("B 등급\n");
		//}
		//else if (score >= 70) {
		//	printf("C 등급\n");
		//}
		//else {
		//	printf("재시험 대상입니다.\n");
		//return 0 ;
		//}
	//1번 문제
	//100점이 최대임
	//int a; 
	//	printf("당신의 점수는?");
	//	scanf_s("%d", &a);
	//	if (a >= 75) {
	//		if (a == 100) {
	//			printf("와 100점 이라니 정말 대단하십니다");
	//		}
	//		else {
	//			printf("축하합니다 당신은 통과 하셨습니다");
	//		}
	//	}
	//	else {
	//		printf("아쉽지만 다음 기회에");
	//	}
	//2번문제
	//int a;
	//	printf("이번 년도의 날짜는 어떻게 되시는가요--->");
	//	scanf_s("%d", &a);
	//	if (a % 4 == 0) {
	//		if (a % 100 ==0){
	//			printf("평년임");
	//		}
	//		else if(a%400==0){
	//			printf("윤년임");
	//		}
	//		else {
	//			printf("윤년임");
	//		}
	//	}
	//	else{
	//		printf("평년임");
	//	}
	//7
	//int myNum = 15;        // 선언 + 초기화
	//int myNum;             // 선언만
	//myNum = 15;            // 나중에 값 대입
	//8
	//int a = 15;
	//float b = 30.4;
	//char c ='k';
	//char d[10] = "k.k.k.";
	//printf("%d\n", a);
	//printf("%f\n", b);
	//printf("%c\n", c);
	//printf("%s\n", d);
	// 9
	//float x = 3.5;
	//int y = (int)x;  // x를 정수로 강제 변환 → y = 3
	//printf("%d\n", y);
	//10
	//char strInt[] = "123";
	//char strFloat[] = "3.14";
	//int num = atoi(strInt);        // 문자열 → 정수
	//float fnum = atof(strFloat);   // 문자열 → 실수
	//printf("정수 변환: %d\n", num);
	//printf("실수 변환: %f\n", fnum);
	// 11
	//char a[10]; 
	//char b[10];
	//int s;
	//	scanf_s("%s", a, (unsigned)_countof(a));//a=10
	//	scanf_s("%s", b, (unsigned)_countof(b));//b=20
	//	int num = atoi(a);        // 문자열 → 정수
	//	int nam = atoi(b);
	//	printf("정수 변환: %d\n", num);
	//	printf("정수 변환: %d\n", nam);
	//	s = num + nam;
	//	printf("%d\n",s);//30
	//12
	//for (int a = 10; a >= 1; a--) {
	//	printf("%d\n", a);
	//	}
	// 13
	//int b=0;
	//for (int a = 2; a <= 100; a += 2) {
	//	b = b + a;
	//}
	//printf("%d\n", b);
	//문제 3
	int a;
	printf("'더하기는 1번, 빼기는 2번,나누기는 3번,곱하기는 4번입니다.입력하실 곳은 여기 -->'");
	scanf_s("%d", &a);
	if (a == 1) {
		int x;
		printf("첫번쨰 수를 알려주세요:");
		scanf_s("%d", &x);
		int y;
		printf("두번쨰 수를 알려주세요:");
		scanf_s("%d", &y);
		int k;
		k = x + y;
		printf("%d\n", k);
	}
	else if (a == 2) {


		int x;
		printf("첫번쨰 수를 알려주세요:");
		scanf_s("%d", &x);
		int y;
		printf("두번쨰 수를 알려주세요:");
		scanf_s("%d", &y);
		int k;
		k = x - y;
		printf("%d\n", k);
	}
	else if (a == 3) {


		int x;
		printf("첫번쨰 수를 알려주세요:");
		scanf_s("%d", &x);
		int y;
		printf("두번쨰 수를 알려주세요:");
		scanf_s("%d", &y);
		int k;
		k = x * y;
		printf("%d\n", k);
	}

	else if (a == 4) {


		int x;
		printf("첫번쨰 수를 알려주세요:");
		scanf_s("%d", &x);
		int y;
		printf("두번쨰 수를 알려주세요:");
		scanf_s("%d", &y);
		int k;
		k = x / y;
		printf("%d\n", k);
	}
	else {
		printf("다시 입력해주세요");
	}
	
	return 0;
	}