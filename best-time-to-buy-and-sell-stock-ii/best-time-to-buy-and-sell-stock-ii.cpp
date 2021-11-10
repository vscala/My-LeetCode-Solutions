class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int out = 0;
        int cur = prices[0];
        for (int i = 0; i < prices.size(); i++) {
            if (prices[i] > cur) {
                out += prices[i] - cur;
                cur = prices[i];
            } else if (prices[i] < cur) {
                cur = prices[i];
            }
        }
        return out;
    }
};