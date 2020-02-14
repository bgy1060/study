#include<stdio.h>

int main(void){
	int n;
	int x[n];
	int i;
	int x_ud[n];
	int x_d[n];
	
	scanf("%d",&n);
	
	for(i=0;i<n;i++){
		scanf("%d",&x[i]);
		if (x[i]%10>=50){
			x_ud[i]=(x[i]-(x[i]%100))+100;	
		}
		else{
			x_ud[i]=x[i]-(x[i]%100);
		}
		
		x_d[i]=x[i]-(x[i]%100);
		
	}
	printf("\n");
	
	for (i=0;i<n;i++){
		printf("%d %d\n",x_ud[i],x_d[i]);
		
	}
	
}
