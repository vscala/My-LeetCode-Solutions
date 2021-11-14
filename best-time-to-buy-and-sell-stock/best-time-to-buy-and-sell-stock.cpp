class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int mn = prices[0], out = 0;
        for (int price : prices) {
            if (price < mn) mn = price;
            else if (price - mn > out) out = price - mn;
        }
        return out;
    }
};