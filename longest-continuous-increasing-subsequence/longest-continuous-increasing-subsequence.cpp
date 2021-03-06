class Solution {
public:
    int findLengthOfLCIS(vector<int>& nums) {
        int out = 1, cur = 1;
        for (int i = 1; i < nums.size(); i++) {
            if (nums[i] > nums[i-1]) {
                cur += 1;
                if (cur > out) out = cur;
            } else cur = 1;
        }
        return out;
    }
};