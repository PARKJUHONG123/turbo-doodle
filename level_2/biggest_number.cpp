#include <string>
#include <vector>
#include <iostream>
#include <algorithm>

using namespace std;

string solution(vector<int> numbers) {
    string answer = "";
    const int size = 4;
    
    // digit   i
    // 10      0
    // 100     1
    // 1000    2
    // 10000   3
    
    vector<vector<int>> digit_value(size);
    vector<int> digit_number(size); // 10, 100, 1000, 10000
    
    int digit = 1;
    for (int i = 0; i < size; i++){
        digit *= 10;
        digit_number[i] = digit;
    }
    
    for (int i = 0; i < numbers.size(); i++){
        for (int j = 0; j < size; j++){
            if (numbers[i] / digit_number[j] == 0){
                digit_value[j].push_back(numbers[i]);
                break;
            }
        }
    }
    
    int temp = -1;
    int except_count = 0;
    bool all_zero = false;

    for (int i = 0; i < size; i++){
        for (int j = 0; j < digit_value[i].size(); j++){
            for (int k = j + 1; k < digit_value[i].size(); k++){
                if (digit_value[i][j] < digit_value[i][k]){
                    temp = digit_value[i][j];
                    digit_value[i][j] = digit_value[i][k];
                    digit_value[i][k] = temp;
                }
            }
            
            if (i == 0) {
                if (digit_value[i].size() > 0) {
                    if (digit_value[i][0] == 0) {
                        all_zero = true;
                    }
                }
            }        
        }
        except_count += digit_value[i].size();
    }
    
    if (all_zero == true){
        if (except_count - digit_value[0].size() == 0){
            while(!digit_value[0].empty()){
                digit_value[0].pop_back();                
            }
            digit_value[0].push_back(0);
        }
    }
    
    
    int total_count = 0;
    for (int i = 0; i < size; i++){
        total_count += digit_value[i].size();
    }    

    vector<int> start_point(size, 0);
    int max_value = -1, max_index = -1;
    int maked_value = -1, first_value = -1;
    int count = 0;
    
    while(count < total_count){
        
    for (int i = 0; i < size; i++){
        
        //
        if (start_point[i] < digit_value[i].size()){
            maked_value = digit_value[i][start_point[i]];
            first_value = maked_value / (digit_number[i] / 10);
            
            if (i == 0 || i == 2){
                for (int j = i + 1; j < size; j++){
                    maked_value *= 10;
                    maked_value += first_value;
                }
            }
            
            else if (i == 1){
                maked_value = maked_value + 100 * maked_value;                
            }
            
            if (max_value < maked_value){
                max_value = maked_value;
                max_index = i;
            }                    
        }
        //
    }
    
    if (start_point[max_index] < digit_value[max_index].size()){
        answer += to_string(digit_value[max_index][start_point[max_index]]);
        start_point[max_index] += 1;
        count += 1;
    }
    
    max_value = -1;
    max_index = -1;
    maked_value = -1;
    first_value = -1;
        
    }


    return answer;
}
