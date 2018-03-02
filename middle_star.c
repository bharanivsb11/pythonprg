#include<stdio.h>
#include<string.h>
int main()
{
char r[10];
int a;
scanf("%s",r);
a=strlen(r);
if(a%2==0)
{
r[(a/2)-1]='*';
}
else
{
r[a/2]='*';
}
printf("%s",r);
return 0;
}
