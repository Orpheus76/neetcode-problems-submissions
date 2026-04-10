class Solution {
public:
    int removeElement(vector<int>& nums, int val) {
        
        for (int i=0; i<nums.size() - 1; i++) {
            if (nums[i] == val) {
                nums[i].delete;
                val++;
            }
        }

        return k;
    }
};