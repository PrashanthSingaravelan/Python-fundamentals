#include<stdio.h>
#include<stdlib.h>

int main()
{
int i,j;
int sum1=0,sum2=0,fsum=0;
int n=2;
int arr[2][2];

for(i=0;i<n;i++)
    for(j=0;j<n;j++)
  {
    scanf("%d",&arr[i][j]);
  }

for(i=0;i<n;i++)
    for(j=0;j<n;j++)
      if(i==j)
        {
          sum1=sum1+arr[i][j];
        }

for(i=0,j=n-1;i<n,j>=0;i++,j--)
   {
      sum2=sum2+arr[i][j];
   }

fsum=sum2-sum1;
printf("%d",abs(fsum));
return 0;
}
