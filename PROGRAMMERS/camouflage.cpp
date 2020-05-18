#include <string>
#include <vector>
#include <map>
#include <iostream>
using namespace std;

int solution(vector<vector<string>> clothes) {
    int answer = 1;
    multimap<string, string> cloth_multimap;
    map<string, string> key_map;
    vector<int> count;
    
    for (int i = 0; i < clothes.size(); i++) {
        cloth_multimap.insert(make_pair(clothes[i][1], clothes[i][0]));
        key_map.insert(make_pair(clothes[i][1], clothes[i][0]));
    }
    
    for (auto i = key_map.begin(); i != key_map.end(); i++) {
        int count_value = cloth_multimap.count(i->first);
        cout << i->first << " : " << count_value << endl;
        count.push_back(count_value);
    }
    

    for (int i = 0; i < count.size(); i++) {
        answer *= (count[i] + 1);
    }
    answer -= 1;
    
    
    
    return answer;
}
