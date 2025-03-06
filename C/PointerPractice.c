# include <stdio.h>
# include <ctype.h>
# include <stdlib.h>

int main() {

    //declares a float-pointer variable 'px'
    float *px;

    float x = 6.5;

    //px stores the address of x
    px = &x;

    //This is how you output addresses 'use (void*)' <-- Prints the address of x
    printf("%p\n", (void*) px);

    //This is how you use pointers to print the value of variables 'use * + pointer variable' <-- Prints 6.5
    printf("%f\n", *px);

     //declares a float-pointer variable 'pc'
    char *pc;

    char c = 'o';


    
    //Also stores the address of x. Since the pointer type is char, you must do an explicit cast
    pc = (char *) px;

    //Prints the address of x again
    printf("%p\n", (void*) pc);

    //Now stores the address of c
    pc = &c;

    //Prints the address of c
    printf("%p\n", (void*) pc); 

    //Comparing addresses
    if((void *) px < (void *) pc){
        printf("T\n");
    }
    else{
        printf("F\n");
    }

    
    //'sizeof' prints the number of bytes in a type or variable
    printf("%d\n", sizeof(pc));

     //declares a float-pointer variable 'pd'
    int *pd;

    //Also stores the address of c. Since the pointer type is int, you must do an explicit cast
    pd = (int*) pc;

    //Prints o and the int value of the char 'o' <-- based on ASCII table
    printf("%d %c\n", *pc, *pd);

    
    //declares a char array e
    char e[10];

    //declares a char-pointer variable 'pe'
    char *pe;

    //pointers can point to arrays because they are usually used to point to lists of bytes(addresses)
    pe = e;

    // e will print a random char
    printf("%c", e);
}