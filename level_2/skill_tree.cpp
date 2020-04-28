#include <string>
#include <vector>

using namespace std;

int set_max(int size, int n, int *arr){

}

int solution(string skill, vector<string> skill_trees) {
    int answer = 0;
    int *arr = new int[skill.length()];
    bool wrong = false;
    int size = -1;
    string temp;
    
    for (int i = 0; i < skill_trees.size(); i++){
        temp = skill_trees[i];
        size = temp.length();
        
        for (int j = 0; j < skill.length(); j++){
            arr[j] = size + 1;
        }
        
        for (int j = 0; j < temp.length(); j++){
            for (int k = 0; k < skill.length(); k++){
                if (skill[k] == temp[j]){
                    arr[k] = j;
                }
            }
        }
        
        for (int j = 0; j < skill.length() - 1; j++){
            if (arr[j] > arr[j + 1]){
                wrong = true;
                break;
            }
        }
        if (wrong == false){
            answer += 1;
        }
        wrong = false;
    }
    
    return answer;
}
