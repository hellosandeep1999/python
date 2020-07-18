#include<stdio.h>
void main()
{
// Declare variables
int N,j,num,largest=0,smallest=1000,remd,i,count,numOfPairs=0;
int numbers[500],bitScore[500];
char tem;

// Read N
scanf("%d",&N);
j=0;

// Read N numbers to array
do {
scanf("%d%c", &numbers[j], &tem);
j++;
} while(tem != '\n');

// Find the bit score
for(j=0;j<N;j++)
{
num=numbers[j];
largest=0;
smallest=1000;

// Find largest and smallest digit
while (num > 0) {
remd = num % 10;
if (remd > largest)
{
largest = remd;
}
if (remd < smallest)
{
smallest = remd;
}

num = num / 10;
}
// To make it 2 digit divide it by 100
bitScore[j]=((largest*11)+(smallest*7))%100;
}

// Find the pairs
for(i=1;i<9;i++)
{
count=0;

// Check for even index
for(j=0;j<N;j=j+2)
{
// To get the most significant digit
num=bitScore[j]/10;
if(num==i)
count++;
}
//if two numbers found it forms one pair
if(count==2)
numOfPairs++;

// If more than 2 numbers found it make 2 pairs
else if(count>=3)
numOfPairs=numOfPairs+2;
count=0;

// Now check for odd index
for(j=1;j<N;j=j+2)
{
num=bitScore[j]/10;
if(num==i)
count++;
}
if(count==2)
numOfPairs++;
else if(count>=3)
numOfPairs=numOfPairs+2;
}

// Print the result
printf("%d", numOfPairs);

// Pause the screen
getchar();
}