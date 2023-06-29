#include<stdio.h>
#include<string.h>
void display(char c[]){
    printf("%s", c);
}
int lens(char c[]){
    int cnt = 0;
    for(int i = 0; c[i] != '\0'; i++){
        cnt++;
    }
    return cnt;
}
void Del(char c[], int pos){
    /*
    0 1 2 3
    a b c d
    a c c d
    a c d d

    pos = 2

    a b c d
    a c d d
    c[n-1] = '\0'
    pos = 2
    c[1] = c[2]
    c[2] = c[3]
    */
   int n = lens(c);
   for(int i = pos; i < n; i++){
        c[i-1] = c[i];
   }
   c[n-1] = '\0';
   display(c);
}
int main()
{
    
    // char c = 'B' + 32;
    // char c = 'a' - 32;
    // printf("%c", c);
    // Ap dụng vào bài biến chữ thường thành chữ hoa
    char s[9] = "11111aaa";
    // for(int i = 0; i < 5; i++){
    //     s[i] = s[i] - 32;
    // }
    // printf("%s", s);
    // kiem tra chu so
    int cnt_nb = 0, nb_ch = 0;
    for(int i = 0; i <9; i++){
        if(s[i] >= 48 && s[i] <= 57 )cnt_nb++;
        if(s[i] >= 65 && s[i] <= 90 || s[i] >= 97 && s[i] <= 122) nb_ch++;
    }
    printf("So luong chu so: %d\n", cnt_nb);
    printf("So luong chu cai: %d\n", nb_ch);


    return 0;
}
// Cho em hỏi: Nếu em code như sau 
// (vị trí xóa của em bắt đầu từ 0),
//  thì code cảu em nó bị hạn chế về gì k a?