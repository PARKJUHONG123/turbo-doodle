#include <string>
#include <vector>
#include <iostream>
using namespace std;

int solution(string name) {
    int answer = 0;
    int count = 0;
    int i = 0;
    const int alpha_length = 'Z' - 'A' + 1;

    int value = -1;
    int left_start = -1, right_start = -1;
    int left_count = 0, right_count = 0, temp_count = 0;
    vector<bool> visited(name.length(), false);
    
    for (int p = 0; p < name.length(); p++){
        if (name[p] == 'A'){
            visited[p] = true;
            count++;
        }
    }
    
    while(true){                
        if (visited[i] == false){
            visited[i] = true;
            value = name[i] - 'A';
            if (alpha_length - value < value){
                answer += (alpha_length - value);
            }
            else {
                answer += value;
            }
            count++;
        }
        
        if (count == name.length()) {
            break;
        }        

        // 왼쪽
        left_start = i - 1;
        while (left_start != i){
            left_count++;
            if (left_start <= -1) {
                left_start = name.length() - 1;
            }
            if (visited[left_start] == false){
                break;
            }
            left_start -= 1;
        } 

        // 오른쪽
        right_start = i + 1;
        
        while (right_start != i) {
            right_count++;
            if (right_start >= name.length()) {
                right_start = 0;
            }
            if (visited[right_start] == false){
                break;
            }            
            right_start += 1;
        }

        if (i + name.length() - left_start < right_start - i){
            i = left_start;
            temp_count = left_count;
        }
        else {
            i = right_start;
            temp_count = right_count;
        }
        answer += temp_count;        
        left_count = 0;
        right_count = 0;
    }
    return answer;
}
