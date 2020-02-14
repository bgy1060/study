#include <stdio.h>

int money[8]={50000,10000,5000,1000,500,100,50,10};

int main(void){

	int m,n;
	int charge=0;
	int money_type=0;
	int money_count=0;
	int i=0;	
	
	scanf("%d",&m);
	scanf("%d",&n);
	
	charge=m-n;
	
	for (i=0;i<8;i++){
		if(charge>=money[i]){
			money_type++;
			money_count+=charge/money[i];
			charge=charge%money[i];
		}
	}
	
	printf("%d %d\n",money_type,money_count);
	
}
