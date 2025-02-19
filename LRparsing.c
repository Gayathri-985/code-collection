#include <stdio.h>
#include <string.h>
#include <stdbool.h>
bool isValidSequence(const char *str)
{
int i = 0;
bool seenOne = false;
// Loop through each character in the string
while (str[i] != '\0')
{
// If we see a '1', set the flag
if (str[i] == '1')
{
seenOne = true;
}
// If we see a '0' after seeing a '1', return false
else if (seenOne && str[i] == '0')
{
return false;
}
i++;
}
return true; // If we never see a '0' after a '1', sequence is valid
}
int main()
{
char input[100];
printf("Enter a string of 0s followed by 1s: ");
scanf("%99s", input);
if (isValidSequence(input))
{
printf("The string '%s' is valid.\n", input);
} else
{
printf("The string '%s' is not valid.\n", input);
}
return 0;
}
