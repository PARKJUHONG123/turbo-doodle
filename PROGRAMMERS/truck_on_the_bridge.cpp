#include <string>
#include <vector>

using namespace std;

int solution(int bridge_length, int weight, vector<int> truck_weights) {
    int answer = 1, start_truck = 0, done_truck = -1;
    int on_weight = 0, size = truck_weights.size();
    vector<int> count(size, 0);

    while ( done_truck + 1 < size ){
        answer++;
        if (start_truck < size){
            if (weight >= on_weight + truck_weights[start_truck]){
                on_weight += truck_weights[start_truck];
                start_truck++;
            }
        }
        
        for (int i = done_truck + 1; i < start_truck; i++){
            count[i] += 1;
            if (count[i] == bridge_length){
                done_truck += 1;
                on_weight -= truck_weights[i];
            }
        }
    }
    return answer;
}
