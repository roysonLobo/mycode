#include <stdio.h>
int getSum(int n)
{
    int sum = 0;
    int fsum=0;
    for (int i=0;i<n+1;i++){
        while (i != 0) {
            sum = sum + i % 10;
            i = i / 10;
        }
        if(sum%2==0){
            fsum=fsum+sum;
        }
    }
    return fsum;
}
// Driver code
int main()
{
    int n;
    scanf("%d",&n);
    printf(" %d ", getSum(n));
    return 0;
}