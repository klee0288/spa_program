#include<stdio.h>

int main() 
{ 
    Date dt1 = {1, 2, 2000}; 
    Date dt2 = {1, 2, 2004}; 
  
    printf("Answer is %d\n" , getDifference(dt1, dt2));
  
    return 0; 
} 
