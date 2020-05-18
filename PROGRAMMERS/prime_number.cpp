#include <string>
#include <vector>
#include <iostream>
using namespace std;

bool is_prime (int number) {
    if (number == 0 || number == 1) {
        return false;
    }
    
    else if (number == 2 || number == 3) {
        return true;
    }
    
    else {
        for (int i = 2; i < number; i++) {
            if (number % (i) == 0) {
                return false;
            }
            else if (number < i * i) {
                return true;
            }
        }        
    }
}

void dfs_C(vector<int>& storage, bool* visited, string numbers, string value, int count, int length) {
    if (count == length) {
        if (value[0] != '0') {
            int integer_value = atoi(value.c_str());
            bool result = is_prime(integer_value);
            if (result == true) {
                storage.push_back(integer_value);
            }                    
        }
        return;
    }
    
    for (int i = 0; i < length; i++) {
        if (visited[i] == false) {
            visited[i] = true;
            dfs_C(storage, visited, numbers, value + numbers[i], count + 1, length);
            visited[i] = false;
        }
    }
}

void dfs_P(vector<int>& storage, string numbers, string value, int count, int length) {
    if (count == length) {
	if (value[0] != '0') {
            int integer_value = atoi(value.c_str());
    	    bool result = is_prime(integer_value);
            if (result == true) {
                storage.push_back(integer_value);
	    }
        }
    return ;
    }

    for (int i = 0; i < length; i++) {
        dfs_P(storage, numbers, value + numbers[i], count + 1, length);
    }
}



int solution(string numbers) {
    int answer = 0;
    bool* visited = new bool[numbers.length()];
    for (int i = 0; i < numbers.length(); i++) {
        visited[i] = false;
    }
    
    vector<int> storage;
    for (int i = 0; i <= numbers.length(); i++) {
        dfs_C(storage, visited, numbers, "", i, numbers.length());
    }
    
    answer = storage.size();
    if (answer == 0) {
        
    }
    else {
        int temp = -1;
        for (int i = 0; i < storage.size(); i++){
            for (int j = i + 1; j < storage.size(); j++) {
                if (storage[i] < storage[j]) {
                    temp = storage[i];
                    storage[i] = storage[j];
                    storage[j] = temp;
                }
            }
        }
        
        
        for (int i =0; i < storage.size() - 1; i++){
            if (storage[i] == storage[i + 1]) {
                answer -= 1;
            }
        }        
    }
    
    
    return answer;
}
