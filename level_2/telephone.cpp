#include <string>
#include <vector>
using namespace std;

bool solution(vector<string> phone_book) {
    bool answer = true;
    int length = -1;
    
    for (int i = 0; i < phone_book.size(); i++) {
        for (int j = 0; j < phone_book.size(); j++){
            length = phone_book[i].length();
            if (phone_book[i] == phone_book[j].substr(0, length)) {
                if (i != j) {
                    answer = false;
                    break;
                }
            }
            
            if (answer == false) {
                break;
            }
        }
    }
    return answer;
}
