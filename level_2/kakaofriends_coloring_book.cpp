#include <vector>
#include <iostream>
using namespace std;

void dfs(vector<vector<int>> picture, vector<vector<bool>>& visited, int m, int n, int i, int j, int target, int* count){
    if (visited[i][j] == false && target == picture[i][j]){
        visited[i][j] = true;
        *count = *count + 1;
    }
    else {
        return ;
    }
    if (i + 1 < m) { // 아래
        dfs(picture, visited, m, n, i + 1, j, target, count);
    }
    if (j + 1 < n) { // 오른쪽
        dfs(picture, visited, m, n, i, j + 1, target, count);
    }
    if (i - 1 >= 0) {
        dfs(picture, visited, m, n, i - 1, j, target, count);        
    }
    if (j - 1 >= 0) {
        dfs(picture, visited, m, n, i, j - 1, target, count);        
    }
}

// 전역 변수를 정의할 경우 함수 내에 초기화 코드를 꼭 작성해주세요.
vector<int> solution(int m, int n, vector<vector<int>> picture) {
    int number_of_area = 0;
    int max_size_of_one_area = 0;
    int count = 0;
    vector<vector<bool>> visited(m, vector<bool>(n, false));    
    
    for (int i = 0; i < m; i++){
        for (int j = 0; j < n; j++){
            if (visited[i][j] == false && picture[i][j] != 0){
                dfs(picture, visited, m, n, i, j, picture[i][j], &count);
                if (max_size_of_one_area < count){
                    max_size_of_one_area = count;
                }
                number_of_area++;
                count = 0;
            }
        }
    }
    
    vector<int> answer(2);
    answer[0] = number_of_area;
    answer[1] = max_size_of_one_area;
    return answer;
}
