class Solution {
public:
    int dp[1001];
    int combinationSum4(vector<int>& nums, int target) {
        for (int i = 0; i < 1001; i++)
            dp[i] = -1;
        
        return count(0, nums, target);
    }
    
    int count(int cur, vector<int>& nums, int target) {
        if (cur == target) return 1;
        if (cur > target) return 0;
        if (dp[cur] != -1) return dp[cur];

        dp[cur] += 1;
        for (int num : nums)
            dp[cur] += count(cur + num, nums, target);
        return dp[cur];            
    }
};