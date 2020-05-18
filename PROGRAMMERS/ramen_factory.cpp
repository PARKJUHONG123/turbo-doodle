#include <string>
#include <vector>
#include <queue>
#include <iostream>
using namespace std;

int solution(int stock, vector<int> dates, vector<int> supplies, int k) {
    int answer = 0;
    int index = 0;
    priority_queue<int> pq;
    
    for (int i = 0 ; i < k; i++) {
        if (i == dates[index]) {
            pq.push(supplies[index]);
            if (index != dates.size() - 1) {
                index += 1;
            }
        }
        if (stock == 0) {
            stock += pq.top();
            pq.pop();
            answer += 1;
        }
        stock -= 1;
    }
    
    return answer;
}
