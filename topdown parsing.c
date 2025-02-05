#include<stdio.h>
#include<ctype.h>
#include<string.h>
int match(char *input,char *rule)
{
    return (input==rule)==0;
}
int main()
{
    char input[]="a";
    char rule[]="a";
    if(match(input,rule))
    {
        printf("string %s is vaild rule %s",input,rule);
    }
    else
    {
        printf("string %s is not vaild for rule %s",input,rule);
    }
    return 0;
}   
