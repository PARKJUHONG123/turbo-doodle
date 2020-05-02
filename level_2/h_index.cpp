#include <string>
#include <vector>
#include <iostream>
using namespace std;

int solution(vector<int> citations) {
    int answer = 0;
    int n = citations.size();
    int count = 0, h_max = 0;
    
    for (int h = 0; h <= n; h++) {        
        for (int i = 0; i < n; i++) {
            
            if (citations[i] >= h) {
                count++;
                if (count == h) {
                    if (h_max < count) {
                        h_max = count;
                        break;
                    }
                }
            }
            
        }
        count = 0;
    }
    
    answer = h_max;
    return answer;
}
