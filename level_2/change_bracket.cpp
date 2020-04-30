#include <string>
#include <vector>
using namespace std;

string recursive(string w){
    bool right_sentence = true;
    int count = 0;
    int i = 0;
    
    if (w == ""){
        return "";
    }
    
    for (i = 0; i < w.length(); i++){
        if (w[i] == '(') {
            count++;
        }
        else {
            count--;
        }
        if (count == 0) {
            break;
        }
    }
    
    string u = w.substr(0, i + 1);
    string v = w.substr(i + 1, w.length() - i);
    
    for (i = 0; i < u.length(); i++){
        if (u[i] == '(') {
            count++;
        }
        else {
            count--;
        }
        if (count < 0) {
            right_sentence = false;
            break;
        }
    }
    
    if (right_sentence == true) {
        u += recursive(v);
        return u;
    }
    
    else {
        string temp;
        temp += '(';
        temp += recursive(v);
        temp += ')';
        
        u.erase(0, 1);
        u.erase(u.length() -1, 1);
        
        for (int j = 0; j < u.length(); j++){
            if (u[j] == '('){
                temp += ')';
            }
            else {
                temp += '(';
            }
        }
        return temp;
    }    
}

string solution(string p) {
    string answer = "";
    int count = 0;
    int i = 0;
    
    answer = recursive(p);
    return answer;
}
