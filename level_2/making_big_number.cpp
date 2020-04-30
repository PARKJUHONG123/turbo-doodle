#include <string>
#include <vector>
#include <iostream>
using namespace std;

string solution(string number, int k) {
    int start_point = 0;
    
    while (k > 0) {
        if (number[start_point] < number[start_point + 1]){
            number.erase(start_point, 1);
            start_point = 0;
            k--;
        }
        else {
            start_point++;
        }
        
        if (start_point + 1 >= number.length()){
            while(k > 0){
                number.erase(start_point, 1);
                k--;
            }
        }
    }
    
    return number;
}
