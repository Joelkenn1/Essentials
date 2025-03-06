#include <stdio.h>
#include <pthread.h>
#include <assert.h>

void *proc(void *arg) {//we can use other function names than proc
	printf("arg=%s\n", arg);

	return (void *)2016;
}//proc

int main() {
	int r;
	pthread_t x;
	void *result = &result;
    char p[100] = "34";
    
	//creating the thread
	r=pthread_create(&x, NULL, proc, (void *)p);

    // main thread waits for x to execute without storing the return value
	//pthread_join(x, NULL);

    // main thread waits for x to execute while storing its return value
    pthread_join(x, result);

    // exits the x thread and updates the return value to 99
    //pthread_exit((void *)99);

    
    printf("result=%d\n", result);
    
	return 0; 
}//main
