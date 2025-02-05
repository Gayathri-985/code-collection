#include<stdio.h>
#include<ctype.h>
#include<string.h>
void lexicalanalyzers(char *input)
{
	 int i=0;
	 while(input[i])
	 {
	 	if(isalpha(input[i]))
	 	{
	 	     printf("\n identifers::%c",input[i]);	
		}
		else if(isdigit(input[i]))
		{
			printf("\n number::%c",input[i]);
		}
		else
		{
			printf("\n symbol ::%c",input[i]);
		}
		 i++;
	 }
}
int main()
{
	char string[]="x=3+2";
	int i=0;
	printf("Entered code is");
	while(string[i])
	{
		printf("%c",string[i]);
		i++;
	}
	   lexicalanalyzers(string);
	   return 0;
}

