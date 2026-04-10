class Solution {
public:
    int removeElement(vector<int>& nums, int val) {
        
        int k = 0;

        for (int i=0; i<nums.size() - 1; i++) {
            if (nums[i] == val) {
                nums[i].delete;
                k++;
            }
        }

        return k ;
    }
};