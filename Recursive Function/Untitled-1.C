#include<stdio.h>
#include<conio.h>
using namespace std;
int fun(int i) 
{ 
  if ( i%2!=0 ) return (i++); 
  else return fun(fun( i - 1 )); 
} 
  
int main() 
{ 
  printf("%d",fun(200));
  getchar(); 
  return 0; 
} 
