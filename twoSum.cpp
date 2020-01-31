class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        map<int, int> hashmap;
        map<int, int>::iterator it;
        int pos = 0;
        
        while (pos < nums.size()) {
            it = hashmap.find(target-nums[pos]);
            if (it != hashmap.end()) {
                return {it->second, pos};
            }
            else {
                hashmap.insert(pair<int, int>(nums[pos], pos));
                pos++;
            }
        }
        
        return nums;
    }
};
