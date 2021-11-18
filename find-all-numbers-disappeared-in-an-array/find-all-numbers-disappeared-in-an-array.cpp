class Solution {
public:
    vector<int> findDisappearedNumbers(vector<int>& nums) {
        for (int i = 0; i < nums.size(); i++) {
            while (nums[i] != i+1 && nums[i] != -1 && nums[nums[i]-1] != nums[i]) {
                if (nums[i]-1 < nums.size()) {
                    swap(nums[i], nums[nums[i]-1]);
                } else {
                    nums.push_back(-1);
                }
            }
        }
        vector<int> out;
        for (int i = 0; i < nums.size(); i++)
            if (nums[i] != i+1) out.push_back(i+1);
        return out;
    }
};