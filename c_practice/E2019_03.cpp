#include<stdio.h>

int main(void){
	
	int n;
	scanf("%d",&n);
	printf("\n");
	
	int i,j;
	
	for(j=0;j<n;j++){
		for(i=0;i<j+1;i++){
			printf("*");
		}
		printf("\n");
	}
}
