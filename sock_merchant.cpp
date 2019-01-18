#include <iostream>
#include <map>

int main() {
    int n;
    int pairs_count=0;
    scanf("%d", &n);
    std::map<int,int> color_freq;

    for (int i=0; i<n; i++)
    {
        int color;
        scanf("%d", &color);
        color_freq[color]++;
    }
    
    std::map<int,int>::iterator itr;
    for (itr = color_freq.begin(); itr!=color_freq.end(); itr++)
        pairs_count += itr->second / 2;
    
    printf("%d\n", pairs_count);
    return 0;
}

