class Solution {
public:
    int maxSatisfaction(vector<int>& satisfaction) {
        sort(satisfaction.begin(), satisfaction.end());
        int cur = 0, out = 0;
        for (int i = satisfaction.size() - 1; i >= 0; i--) {
            cur += satisfaction[i];
            if (cur > 0) out += cur;
            else break;
        }
        return out;
    }
};