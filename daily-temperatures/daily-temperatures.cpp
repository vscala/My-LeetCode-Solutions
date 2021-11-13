class Solution {
public:
    vector<int> dailyTemperatures(vector<int>& temps) {
        std::reverse(temps.begin(), temps.end());
        vector<int> out;
        int seen[71];
        std::fill_n(seen, 71, -1);
        
        for (int i = 0; i < temps.size(); i++) {
            int ind = temps[i] - 30;
            seen[ind] = i;
            
            int best = temps.size() + 1;
            for (int j = ind + 1; j <= 70; j++) 
                if (seen[j] != -1 and i - seen[j] < best)
                    best = i - seen[j];
            if (best == temps.size() + 1) out.push_back(0);
            else out.push_back(best);
        }
        
        std::reverse(out.begin(), out.end());
        return out;
    }
};