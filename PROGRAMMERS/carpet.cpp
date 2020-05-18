#include <string>
#include <vector>
#include <iostream>
using namespace std;

vector<int> solution(int brown, int red) {
    vector<int> answer;
    
    int total = brown + red;
    int a, b;
    
    for (a = 1; a <= total; a++) {
        b = total / a;

        if (a > b) {
            break;
        }
        
        if (a * b == total) {
            if ( (a - 2) * (b - 2) == red ) {
                answer.push_back(b);
                answer.push_back(a);
            }
        }
    }
    
    
    return answer;
}
