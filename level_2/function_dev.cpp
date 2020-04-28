#include <string>
#include <vector>

using namespace std;

vector<int> solution(vector<int> progresses, vector<int> speeds) {
    vector<int> answer;
    bool wrong = false;
    int count = 0, max_count = 0;
    int total = 0;
    
    while(true){
        for (int i = progresses.size() - 1; i >= 0; i--){
            if (progresses[i] < 100){
                progresses[i] += speeds[i];
            }
            else{
                for (int j = i; j >= 0; j--){
                    if (progresses[j] < 100){
                        wrong = true;
                        break;
                    }
                    count++;
                }
                
                if (wrong == false){
                    if (max_count < count){
                        max_count = count;
                    }
                }
                wrong = false;
                count = 0;
            }
        }
        
        if (max_count != 0){
            if (answer.empty()){
                answer.push_back(max_count);
                total = max_count;
            }
            else{
                if (max_count > total){
                    answer.push_back(max_count - total);
                    total = max_count;
                }
            }
            
            if (max_count == progresses.size()){
                break;
            }            
            max_count = 0;
        }
    }
    
    return answer;
}
