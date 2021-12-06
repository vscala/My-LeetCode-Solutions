class Solution {
public:
    int minCostToMoveChips(vector<int>& position) {
        int even = 0;
        for (int num : position) even += num % 2;
        if (even < position.size() - even) return even;
        return position.size() - even;
    }
};