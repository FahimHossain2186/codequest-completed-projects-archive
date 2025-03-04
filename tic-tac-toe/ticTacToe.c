#include <stdio.h>
#include <stdlib.h>
#include <time.h>

char input[3][3];

void printBoard(){

    printf("\n %c | %c | %c ", input[0][0], input[0][1], input[0][2]);
    printf("\n---|---|---");
    printf("\n %c | %c | %c ", input[1][0], input[1][1], input[1][2]);
    printf("\n---|---|---");
    printf("\n %c | %c | %c ", input[2][0], input[2][1], input[2][2]);
    printf("\n");

}

void resetBoard(){

    for(int x = 0; x < 3; x++)
        for(int y = 0; y < 3; y++)
            input[x][y] = ' ';
}

int emptyspace(){
    
    int count = 9;

    for(int x = 0; x < 3; x++)
        for(int y = 0; y < 3; y++)
            if(input[x][y] != ' ')
                count--;

    return count;
}

void player(){

    int row, column;

    while(1){

        printf("Enter row #(1-3): ");
        scanf("%d", &row);
        row--;
        printf("Enter column #(1-3): ");
        scanf("%d", &column);
        column--;

        if(input[row][column] != ' ')   printf("Invalid Move!!\n");
        else{
            input[row][column] = 'X';
            break;
        }
    }
    

}

void computer(){

    //random input

    int row, column;

    do{
        row = rand() % 3; //To ensure the random number is always between 0 to 2
        column = rand() % 3;

    }while(input[row][column] != ' ');

    input[row][column] = 'O';

}

void impossible360(){

    int row, column;

    //1st move

    if(emptyspace() == 9){

        row     = (rand() % 2) * 2; //To ensure the random number is always between 0 or 2
        column  = (rand() % 2) * 2;
        input[row][column] = 'O';
    }
    
    //2nd move

    else if(emptyspace() == 7){

        if(input[0][0] == 'O'){
            if(input[0][1] == 'X' || input[0][2] == 'X' || input[1][2] == 'X'){
                input[2][0] = 'O';
            }
            else if(input[1][0] == 'X' || input[2][0] == 'X' || input[2][1] == 'X'){
                input[0][2] = 'O';
            }
            else if(input[1][1] == 'X'){
                input[2][2] = 'O';
            }
            else if(input[2][2] == 'X'){
                int row = (rand() % 2) * 2;
                int column = 2 - row;
                input[row][column] = 'O'; 
            }
        }
    
        else if(input[0][2] == 'O'){
            if(input[0][1] == 'X' || input[0][0] == 'X' || input[1][0] == 'X'){
                input[2][2] = 'O';
            }
            else if(input[1][2] == 'X' || input[2][2] == 'X' || input[2][1] == 'X'){
                input[0][0] = 'O';
            }
            else if(input[1][1] == 'X'){
                input[2][0] = 'O';
            }
            else if(input[2][0] == 'X'){
                int row = (rand() % 2) * 2;
                int column = row;
                input[row][column] = 'O'; 
            }
        }
    
        else if(input[2][0] == 'O'){
            if(input[1][0] == 'X' || input[0][0] == 'X' || input[0][1] == 'X'){
                input[2][2] = 'O';
            }
            else if(input[2][1] == 'X' || input[2][2] == 'X' || input[1][2] == 'X'){
                input[0][0] = 'O';
            }
            else if(input[1][1] == 'X'){
                input[0][2] = 'O';
            }
            else if(input[0][2] == 'X'){
                int row = (rand() % 2) * 2;
                int column = row;
                input[row][column] = 'O'; 
            }
        }
    
        else if(input[2][2] == 'O'){
            if(input[2][1] == 'X' || input[2][0] == 'X' || input[1][0] == 'X'){
                input[0][2] = 'O';
            }
            else if(input[1][2] == 'X' || input[0][2] == 'X' || input[0][1] == 'X'){
                input[2][0] = 'O';
            }
            else if(input[1][1] == 'X'){
                input[0][0] = 'O';
            }
            else if(input[0][0] == 'X'){
                int row = (rand() % 2) * 2;
                int column = 2 - row;
                input[row][column] = 'O'; 
            }
        }
    }
    
    //3rd move

    else if(emptyspace() == 5){
        if(input[0][0] == 'O' && input[0][2] == 'O'){
            if(input[0][1] == 'X' && input[1][0] == 'X')        input[2][2] = 'O';
            else if(input[0][1] == 'X' && input[2][0] == 'X')   input[2][2] = 'O';
            else if(input[2][1] == 'X' && input[0][1] == 'X')   input[1][1] = 'O';
            else if(input[2][2] == 'X' && input[0][1] == 'X')   input[2][0] = 'O';
            else if(input[2][1] == 'X' && input[0][1] == 'X')   input[2][0] = 'O';
            else                                                input[0][1] = 'O';
        }

        else if (input[0][0] == 'O' && input[2][0] == 'O') {
            if (input[0][1] == 'X' && input[1][0] == 'X')        input[2][2] = 'O';
            else if (input[0][2] == 'X' && input[1][0] == 'X')   input[2][2] = 'O';
            else if (input[1][2] == 'X' && input[1][0] == 'X')   input[1][1] = 'O';
            else if (input[2][2] == 'X' && input[1][0] == 'X')   input[0][2] = 'O';
            else if (input[2][1] == 'X' && input[1][0] == 'X')   input[0][2] = 'O';
            else                                                 input[1][0] = 'O';
        }
    
        else if (input[2][0] == 'O' && input[2][2] == 'O') {
            if (input[1][0] == 'X' && input[2][1] == 'X')        input[0][2] = 'O';
            else if (input[0][0] == 'X' && input[2][1] == 'X')   input[0][2] = 'O';
            else if (input[0][1] == 'X' && input[2][1] == 'X')   input[1][1] = 'O';
            else if (input[0][2] == 'X' && input[2][1] == 'X')   input[0][0] = 'O';
            else if (input[1][2] == 'X' && input[2][1] == 'X')   input[0][0] = 'O';
            else                                                 input[2][1] = 'O';
        }
    
        else if (input[0][2] == 'O' && input[2][2] == 'O') {
            if (input[0][1] == 'X' && input[1][2] == 'X')        input[2][0] = 'O';
            else if (input[0][0] == 'X' && input[1][2] == 'X')   input[2][0] = 'O';
            else if (input[1][0] == 'X' && input[1][2] == 'X')   input[1][1] = 'O';
            else if (input[2][0] == 'X' && input[1][2] == 'X')   input[0][0] = 'O';
            else if (input[2][1] == 'X' && input[1][2] == 'X')   input[0][0] = 'O';
            else                                                 input[1][2] = 'O';
        }

        else if ((input[0][0] == 'O' && input[2][2] == 'O') || (input[0][2] == 'O' && input[2][0] == 'O')) {
            // If an 'X' is found in a non-center diagonal position, mirror the move
            if          (input[0][1] == 'X' && input[2][1] == ' ')      input[2][1] = 'O';
            else if     (input[1][0] == 'X' && input[1][2] == ' ')      input[1][2] = 'O';
            else if     (input[1][2] == 'X' && input[1][0] == ' ')      input[1][0] = 'O';
            else if     (input[2][1] == 'X' && input[0][1] == ' ')      input[0][1] = 'O';
            
            else if     (input[0][0] == 'X' && input[2][2] == ' ')      input[2][2] = 'O';
            else if     (input[2][2] == 'X' && input[0][0] == ' ')      input[0][0] = 'O';
            else if     (input[0][2] == 'X' && input[2][0] == ' ')      input[2][0] = 'O';
            else if     (input[2][0] == 'X' && input[0][2] == ' ')      input[0][2] = 'O';
        }
    }

    //4th move

    else if(emptyspace() == 3){

        if(input[1][1] == 'O'){

            if(input[0][0] == ' ')          input[0][0] = 'O';
            else if(input[0][2] == ' ')     input[0][2] = 'O';
            else if(input[2][0] == ' ')     input[2][0] = 'O';
            else if(input[2][2] == ' ')     input[2][2] = 'O';    
        }

        else if (input[0][0] == 'O' && input[0][2] == 'O' && input[2][2] == 'O'){
            
            if(input[1][1] == ' ')          input[1][1] = 'O';
            else if(input[0][1] == ' ')     input[0][1] = 'O';
            else if(input[1][2] == ' ')     input[1][2] = 'O';
        }

        else if (input[0][2] == 'O' && input[2][2] == 'O' && input[2][0] == 'O'){
            
            if(input[1][1] == ' ')          input[1][1] = 'O';
            else if(input[2][1] == ' ')     input[2][1] = 'O';
            else if(input[1][2] == ' ')     input[1][2] = 'O';
        }

        else if (input[2][0] == 'O' && input[0][0] == 'O' && input[0][2] == 'O'){
            
            if(input[1][1] == ' ')          input[1][1] = 'O';
            else if(input[0][1] == ' ')     input[0][1] = 'O';
            else if(input[1][0] == ' ')     input[1][0] = 'O';
        }

        else if (input[2][2] == 'O' && input[2][0] == 'O' && input[0][0] == 'O'){
            
            if(input[1][1] == ' ')          input[1][1] = 'O';
            else if(input[2][1] == ' ')     input[2][1] = 'O';
            else if(input[1][0] == ' ')     input[1][0] = 'O';
        }

        else if (input[0][0] == 'O' && input[2][2] == 'O') {
            // If an 'X' is found in a non-center diagonal position, mirror the move
            if          (input[0][1] == 'X' && input[2][1] == ' ')      input[2][1] = 'O';
            else if     (input[1][0] == 'X' && input[1][2] == ' ')      input[1][2] = 'O';
            else if     (input[1][2] == 'X' && input[1][0] == ' ')      input[1][0] = 'O';
            else if     (input[2][1] == 'X' && input[0][1] == ' ')      input[0][1] = 'O';

            else if     (input[1][2] == 'X' && input[0][1] == ' ')      input[0][1] = 'O';
            else if     (input[0][1] == 'X' && input[1][2] == ' ')      input[1][2] = 'O';
            else if     (input[0][1] == 'X' && input[2][1] == ' ')      input[2][1] = 'O';
            else if     (input[2][1] == 'X' && input[0][1] == ' ')      input[0][1] = 'O';
        }

        else if(input[0][2] == 'O' && input[2][0] == 'O'){
            
            if          (input[0][1] == 'X' && input[2][1] == ' ')      input[2][1] = 'O';
            else if     (input[1][0] == 'X' && input[1][2] == ' ')      input[1][2] = 'O';
            else if     (input[1][2] == 'X' && input[1][0] == ' ')      input[1][0] = 'O';
            else if     (input[2][1] == 'X' && input[0][1] == ' ')      input[0][1] = 'O';

            else if     (input[1][2] == 'X' && input[2][1] == ' ')      input[2][1] = 'O';
            else if     (input[2][1] == 'X' && input[1][2] == ' ')      input[1][2] = 'O';
            else if     (input[0][1] == 'X' && input[1][0] == ' ')      input[1][0] = 'O';
            else if     (input[1][0] == 'X' && input[0][1] == ' ')      input[0][1] = 'O';
        }
        
    }
    
    //5th move

    else if(emptyspace() == 1){

        if ((input[0][0] == 'O' && input[2][2] == 'O') || (input[0][2] == 'O' && input[2][0] == 'O')) {
            // If an 'X' is found in a non-center diagonal position, mirror the move
            if          (input[0][1] == 'X' && input[2][1] == ' ')      input[2][1] = 'O';
            else if     (input[1][0] == 'X' && input[1][2] == ' ')      input[1][2] = 'O';
            else if     (input[1][2] == 'X' && input[1][0] == ' ')      input[1][0] = 'O';
            else if     (input[2][1] == 'X' && input[0][1] == ' ')      input[0][1] = 'O';

            else if     (input[0][0] == 'X' && input[2][2] == ' ')      input[2][2] = 'O';
            else if     (input[2][2] == 'X' && input[0][0] == ' ')      input[0][0] = 'O';
            else if     (input[0][2] == 'X' && input[2][0] == ' ')      input[2][0] = 'O';
            else if     (input[2][0] == 'X' && input[0][2] == ' ')      input[0][2] = 'O';
        }
    }
}

char winnerCheck(){

    for (int i = 0; i < 3; i++) {
        
        if (input[i][0] == input[i][1] && input[i][0] == input[i][2] && input[i][0] != ' ')     return input[i][0];  // Row check

        if (input[0][i] == input[1][i] && input[0][i] == input[2][i] && input[0][i] != ' ')     return input[0][i];  // Column check
    }

    // Diagonal checks
    if (input[0][0] == input[1][1] && input[0][0] == input[2][2] && input[0][0] != ' ')         return input[0][0];
    if (input[0][2] == input[1][1] && input[0][2] == input[2][0] && input[0][2] != ' ')         return input[0][2];

    return ' ';     
}

void printWinner(char winner){

    if(winner == 'X')       printf("You win!!!");
    else if(winner == 'O')  printf("You Lose!!!");
    else                    printf("Its a Draw!!!");
}

int newgame(){

    char winner = ' '; int exit_choice;
   
    srand(time(0));

    resetBoard();
    
    while(winner == ' ' &&  emptyspace() != 0){
        
        printBoard();

        player();
        winner = winnerCheck();
        if(winner != ' ' || emptyspace() == 0) break;

        computer();
        winner = winnerCheck();
        if(winner != ' ' || emptyspace() == 0) break;
        
    }

    printBoard();
    printWinner(winner);

    printf("Do you want to play another round?");
    printf("\n 1. Yes :(  2. No :D\n");

        do{

            scanf("%d", &exit_choice);

            if (exit_choice == 1) {
                newgame(); 
            }

            else if (exit_choice == 2){
                printf("Exiting the Game.....\n");
                return 0; 
            }
        }while (exit_choice != 1 && exit_choice != 2); 
}

int impossibleGame(){

    char winner = ' '; int exit_choice;
   
    srand(time(0));

    resetBoard();
    
    while(winner == ' ' &&  emptyspace() != 0){

        impossible360();

        printBoard();

        winner = winnerCheck();
        if(winner != ' ' || emptyspace() == 0) break;

        player();
        winner = winnerCheck();
        if(winner != ' ' || emptyspace() == 0) break;
 
    }

    printBoard();
    printWinner(winner);

    printf("Do you want to get crushed another time?");
    printf("\n 1. Yes :D  2. No :{\n");

        do{

            scanf("%d", &exit_choice);

            if (exit_choice == 1) {
                impossibleGame(); 
            }

            else if (exit_choice == 2){
                printf("Exiting the Game.....\n");
                return 0; 
            }
        }while (exit_choice != 1 && exit_choice != 2); 
}

int main(){

    int choice, exit_choice;

    printf("Welcome to Tic Tac Toe");
    printf("\n1. NEW GAME");
    printf("\n2. LEVEL IMPOSSIBLE");
    printf("\n3. EXIT\n");

    do{
        scanf("%d", &choice);
    }while(choice != 1 && choice != 2 && choice != 3);

    if (choice == 1) {
        newgame();
    } 
    
    else if (choice == 2) {
        impossibleGame();
    }  

    else if (choice == 3) {

        printf("Are you sure you want to exit?");
        printf("\n 1. Yes :(  2. No :D\n");

        do{

            scanf("%d", &exit_choice);

            if (exit_choice == 1) {
                printf("Exiting the Game.....\n");
                return 0; 
            }

            else if (exit_choice == 2){
                //Restart to Main Menu
                printf("\n");
                main();
            }

        }while (exit_choice != 1 && exit_choice != 2);        
            
    }
    return 0;

}
