#include <string>
#include <vector>
#include <iostream>
using namespace std;

void dfs(vector<int> numbers, int result, int target, int count, int length, int* answer) {
    if (count == length) {
        if (result == target) {
            *answer += 1;
        }
    }
    
    if (count < length) {
        dfs(numbers, result - numbers[count], target, count + 1, length, answer);
        dfs(numbers, result + numbers[count], target, count + 1, length, answer); 
    }

}

int solution(vector<int> numbers, int target) {
    int answer = 0;
    dfs(numbers, 0, target, 0, numbers.size(), &answer);
    cout << answer;
    return answer;
}
