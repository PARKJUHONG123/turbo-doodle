#include <string>
#include <vector>
using namespace std;

int solution(vector<int> priorities, int location) {
    int answer = 0;
    int max_index = -1, max_value = -1;
    int size = priorities.size();
    int temp_value = -1;
    int i = 0;
    
    while(i < size) {
        for (int j = i; j < size; j++){
            if (max_value < priorities[j]){
                max_value = priorities[j];
                max_index = j;
            }
        }

        if (max_index != i){
            if (location == i){
                location = size - 1;
            }
            else if (location >= i && location < size){
                location--;
            }
            
            temp_value = priorities[i];
            for (int j = i; j < size - 1; j++){
                priorities[j] = priorities[j + 1];
            }
            priorities[size - 1] = temp_value;
        }
        else{
            i = i + 1;
        }
        max_value = -1;
        max_index = -1;
    }
    answer = location + 1;
    return answer;
}
