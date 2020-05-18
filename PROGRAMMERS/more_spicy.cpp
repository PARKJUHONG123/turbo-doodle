#include <string>
#include <vector>
#include <queue>
#include <iostream>
using namespace std;

int solution(vector<int> scoville, int K) {
    int answer = 0;
    int first = -1, second = -1;
    priority_queue< int, vector<int>, greater<int> > pq;
    for (int i = 0; i < scoville.size(); i++) {
        pq.push(scoville[i]);
    }

    while (true) {
        answer += 1;
        
        if (pq.size() == 1) {
            answer = -1;
            break;
        }        
        
        first = pq.top();
	    pq.pop();

        second = pq.top();
        pq.pop();
    
        pq.push(first + second * 2);
        
        if (pq.top() > K) {
            break;
        }
    }
    
    return answer;
}
