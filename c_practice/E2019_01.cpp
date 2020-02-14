#include<stdio.h>

int main(void){
	
	int n;
	int i=0;
	int sum=0;
	int m;
	
	scanf("%d",&n);
	
	for (i=0;i<n;i++){
		scanf("%d",&m);
		if(m%2!=0){
			sum+=m;
		}
	}
	
	printf("%d\n",sum);
	
	return 0;
}
