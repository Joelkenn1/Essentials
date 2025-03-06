# include <stdio.h>
# include <ctype.h>
# include <stdlib.h>
# include <string.h>

struct States {
    char name[100];
    int letters;
};

void getName(char name[]){
    
    char in_name[100];
    scanf("%s", in_name);
    strcpy(name, in_name);
    
        
}

int main(int argc, char *argv[]){
    
    struct States x;

    struct States inputs[atoi(argv[1])];

    // Recieving state input names and their lengths. Storing each state in a array.
    for(int i = 0; i < atoi(argv[1]); i++){
        
        printf("Please input name for state %d:\n", i+1);
        getName(x.name);
        x.letters = strlen(x.name);
        inputs[i] = x;
    }
    

    int largest = inputs[0].letters;
    int bc = 0;
    
    int smallest = inputs[0].letters;
    int sc = 0;

    
    //get largest/smallest letter counts
    for(int i = 0; i < atoi(argv[1]); i++){
        if(inputs[i].letters >= largest){
            largest = inputs[i].letters;
            }
    }

    for(int i = 0; i < atoi(argv[1]); i++){
        if(inputs[i].letters <= smallest){
            smallest = inputs[i].letters;
            }
      }

    
    //get sizes for arrays
    for(int i = 0; i < atoi(argv[1]); i++){
        if(inputs[i].letters == largest){
            bc++;
            }
        }

    for(int i = 0; i < atoi(argv[1]); i++){
        if(inputs[i].letters == smallest){
            sc++;
            }
        }

    
    int largest_words[bc];
    int smallest_words[sc];

    bc = 0;
    sc = 0;

    
    //populating arrays
    for(int i = 0; i < atoi(argv[1]); i++){
        if(inputs[i].letters == largest){
            largest_words[bc] = i;
            bc++;
            }
        else if(inputs[i].letters == smallest){
            smallest_words[sc] = i;
            sc++;
            }
        }


    printf("Which of the following two groups do you want to print? (1) ");
    printf("states with the largest number of letters in names (2) states ");
    printf("with the least number of letters in names.\n");

    int selection;

    scanf("%d", &selection);

    //receiving user input
    if(selection == 1){

        for(int i = 0; i < sizeof(largest_words)/sizeof(largest_words[0]); i++){
            printf("%s has %d letters in its name.\n", inputs[largest_words[i]].name, inputs[largest_words[i]].letters);
            }
        }

    if(selection == 2){

        for(int i = 0; i < sizeof(smallest_words)/sizeof(smallest_words[0]); i++){
            printf("%s has %d letters in its name.\n", inputs[smallest_words[i]].name, inputs[smallest_words[i]].letters);
            }
        }

    
}

















