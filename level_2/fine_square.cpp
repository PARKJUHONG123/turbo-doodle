using namespace std;

long long solution(int w,int h)
{
	long long answer = 1;
    int tw = w, th = h, temp = -1;
    int count = 0, i = 0, j = 0;
    
    if (tw < th){
        temp = tw;
        tw = th;
        th = temp;
    }
    
    // euclidean gcd
    /*
        12 8
        8 4
        4 4
        4 0    
    */
    while(th != 0){
        temp = tw % th;
        tw = th;
        th = temp;
    }
    
    int a = w / tw; // 2 (8 / 4)
    int b = h / tw; // 3 (12 / 4)
    
    // in one sector, diagnosis runs through below (b) + right (a)
    // but start point is same, so needs to minus one block (-1)
    answer = (long long)w * (long long)h - tw * (a + b - 1);
	return answer;
}
