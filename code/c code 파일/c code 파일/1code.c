#include <stdio.h>
#include <stdlib.h>  // atoi, atof �Լ� ����ϱ����� ���̺귯�� stdlib.h

int main() {
	//1
	//printf("hello");
	//return 0;
	// 2
	//printf("hello, world\n");
	//printf("���� ���: %d\n", 10);
	// 3
	//int a = 20;
	//float b = 3.14;
	//char c = 'A';
	//printf("%d\n",a);
	//printf("%f\n",b);
	//printf("%c\n",c);
	// 4
	//int a;
	//	printf("���̸� �Է��Ͻÿ�");
	//	scanf_s("%d", &a);
	//	printf("%d",a);
	// 5
	//int a;
	//printf("����:");
	//scanf_s("%d", &a);*/
	//if (a == 3) {
	//	printf("��¥ ¥������");
	//}
	//else {
	//	printf("���ݵ�");
	//}
	// 6
	//int score;
		//printf("������ �Է��ϼ���: ");
		//scanf_s("%d", &score);
		//if (score >= 90) {
		//	printf("A ���\n");
		//}
		//else if (score >= 80) {
		//	printf("B ���\n");
		//}
		//else if (score >= 70) {
		//	printf("C ���\n");
		//}
		//else {
		//	printf("����� ����Դϴ�.\n");
		//return 0 ;
		//}
	//1�� ����
	//100���� �ִ���
	//int a; 
	//	printf("����� ������?");
	//	scanf_s("%d", &a);
	//	if (a >= 75) {
	//		if (a == 100) {
	//			printf("�� 100�� �̶�� ���� ����Ͻʴϴ�");
	//		}
	//		else {
	//			printf("�����մϴ� ����� ��� �ϼ̽��ϴ�");
	//		}
	//	}
	//	else {
	//		printf("�ƽ����� ���� ��ȸ��");
	//	}
	//2������
	//int a;
	//	printf("�̹� �⵵�� ��¥�� ��� �ǽô°���--->");
	//	scanf_s("%d", &a);
	//	if (a % 4 == 0) {
	//		if (a % 100 ==0){
	//			printf("�����");
	//		}
	//		else if(a%400==0){
	//			printf("������");
	//		}
	//		else {
	//			printf("������");
	//		}
	//	}
	//	else{
	//		printf("�����");
	//	}
	//7
	//int myNum = 15;        // ���� + �ʱ�ȭ
	//int myNum;             // ����
	//myNum = 15;            // ���߿� �� ����
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
	//int y = (int)x;  // x�� ������ ���� ��ȯ �� y = 3
	//printf("%d\n", y);
	//10
	//char strInt[] = "123";
	//char strFloat[] = "3.14";
	//int num = atoi(strInt);        // ���ڿ� �� ����
	//float fnum = atof(strFloat);   // ���ڿ� �� �Ǽ�
	//printf("���� ��ȯ: %d\n", num);
	//printf("�Ǽ� ��ȯ: %f\n", fnum);
	// 11
	//char a[10]; 
	//char b[10];
	//int s;
	//	scanf_s("%s", a, (unsigned)_countof(a));//a=10
	//	scanf_s("%s", b, (unsigned)_countof(b));//b=20
	//	int num = atoi(a);        // ���ڿ� �� ����
	//	int nam = atoi(b);
	//	printf("���� ��ȯ: %d\n", num);
	//	printf("���� ��ȯ: %d\n", nam);
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
	//���� 3
	int a;
	printf("'���ϱ�� 1��, ����� 2��,������� 3��,���ϱ�� 4���Դϴ�.�Է��Ͻ� ���� ���� -->'");
	scanf_s("%d", &a);
	if (a == 1) {
		int x;
		printf("ù���� ���� �˷��ּ���:");
		scanf_s("%d", &x);
		int y;
		printf("�ι��� ���� �˷��ּ���:");
		scanf_s("%d", &y);
		int k;
		k = x + y;
		printf("%d\n", k);
	}
	else if (a == 2) {


		int x;
		printf("ù���� ���� �˷��ּ���:");
		scanf_s("%d", &x);
		int y;
		printf("�ι��� ���� �˷��ּ���:");
		scanf_s("%d", &y);
		int k;
		k = x - y;
		printf("%d\n", k);
	}
	else if (a == 3) {


		int x;
		printf("ù���� ���� �˷��ּ���:");
		scanf_s("%d", &x);
		int y;
		printf("�ι��� ���� �˷��ּ���:");
		scanf_s("%d", &y);
		int k;
		k = x * y;
		printf("%d\n", k);
	}

	else if (a == 4) {


		int x;
		printf("ù���� ���� �˷��ּ���:");
		scanf_s("%d", &x);
		int y;
		printf("�ι��� ���� �˷��ּ���:");
		scanf_s("%d", &y);
		int k;
		k = x / y;
		printf("%d\n", k);
	}
	else {
		printf("�ٽ� �Է����ּ���");
	}
	
	return 0;
	}