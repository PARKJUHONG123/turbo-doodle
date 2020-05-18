#include <string>
#include <vector>
#include <iostream>
#define SIZE 3

using namespace std;

vector<int> get_digit(int input) {
    vector<int> output(SIZE);
    int divide = 100;
    
    for (int i = 0; i < SIZE; i++) {
        output[i] = input / divide;
        input %= divide;
        divide /= 10;
    }
    
    return output;
}

int ball_count(vector<int> input, vector<int> result) {
    int count = 0;
    for (int i = 0; i < SIZE; i++) {
        for (int j = 0; j < SIZE; j++) {
            if (input[i] == result[j]) {
                if (i != j) {
                    count++;
                }
            }
        }
    }
    return count;
}

int strike_count(vector<int> input, vector<int> result) {
    int count = 0;
    for (int i = 0; i < SIZE; i++) {
        if (input[i] == result[i]) {
            count++;
        }
    }
    
    return count;
}

bool right_condition(vector<int> num_input) {
    if (num_input[0] == 0 || num_input[1] == 0 || num_input[2] == 0) {
        return false;
    }
    
    if (num_input[0] == num_input[1] || num_input[0] == num_input[2] || num_input[1] == num_input[2]) {
        return false;
    }
    
    return true;
}

int solution(vector<vector<int>> baseball) {
    int answer = 0, count = 0;
    vector<int> num_input, baseball_input;
    
    for (int num = 123; num <= 987; num++) {
        num_input = get_digit(num);
        if (right_condition(num_input) == false) {
            continue;
        }
        
        for (int i = 0; i < baseball.size(); i++) {
            baseball_input = get_digit(baseball[i][0]);
            if (baseball[i][1] == strike_count(baseball_input, num_input)) {   
                if (baseball[i][2] == ball_count(baseball_input, num_input)) {
                    count++;
                }
            }
            else {
                break;
            }
        } 
        if (count == baseball.size()) {
            cout << num << endl;
            answer += 1;
        }
        count = 0;
    }
    return answer;
}



