#include<iostream>
using namespace std;


void char_by_char(string m){

}

bool is_blocksizeValid(int block_size , int textSize){
    if(block_size <= 1 || block_size >= textSize)
        return false;
    return true;
}

void blockwise(){
    
}


int main(){
    string m;  cin >> m; // plain text

    cout << endl << "Enter 1 if u want to encrypt character by character" << endl;
    cout << "Enter 2 if u want to encrypt your message block wise" << endl;
    int option; cin >> option;
    switch (option)
    {
    case 1:
        char_by_char(m);
        break;
    
    case 2:
        do{
            cout << "Enter the block size u want" << endl;
            int block_size; cin >> block_size;
            if(is_blocksizeValid(block_size,m.size())){
                blockwise();
                break;
            }

        }while (1);
        break;
    }
    return 0;
}
// We