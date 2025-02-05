#include<stdio.h>
#include<ctype.h>
#include<string.h>
#define MAX_PRODUCTIONS 10
#define MAX_SYMBOLS 10
#define SYMBOL_LEN 1
char first[MAX_SYMBOLS][MAX_SYMBOLS]; 
char follow[MAX_SYMBOLS][MAX_SYMBOLS];
int n_productions; 

void calc_first(char symbol, int q1, int q2);
void calc_follow(char symbol);
void addToResult(char* result, char symbol);
int main()
{
int i;
char choice;
char symbol;
printf("Enter the number of productions: ");
scanf("%d%c", &n_productions, &choice);

for(i = 0; i < n_productions; i++)
{
printf("Enter production %d (e.g., E=T): ", i + 1);
scanf("%s", productions[i][0]); 
printf(" -> ");
scanf("%s", productions[i][1]); 
}

do {
printf("\n1. First Set\n2. Follow Set\n3. Exit\n Enter your choice: ");
scanf("%d%c", &i, &choice);
switch(i)
{
case 1:
printf("Enter the symbol to find FIRST: ");
scanf("%c%c", &symbol, &choice);
printf("FIRST(%c) = { ", symbol);
calc_first(symbol, 0, 0);
printf("}\n");
break;
case 2:
printf("Enter the symbol to find FOLLOW: ");
scanf("%c%c", &symbol, &choice);
printf("FOLLOW(%c) = { ", symbol);
calc_follow(symbol);
printf("}\n");
break;
default:
printf("Exiting...\n");
return 0;
}
}
while(1);
return 0;
}

void calc_first(char symbol, int q1, int q2) {
}

void calc_follow(char symbol) {
}

void addToResult(char* result, char symbol)
{
int len = strlen(result);
for(int i = 0; i < len; i++)
{
if(result[i] == symbol)
{
return;
}
}
result[len] = symbol;
result[len + 1] = '\0';
}
