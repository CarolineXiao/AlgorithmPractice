class Solution {
public:
    string longestCommonPrefix(vector<string>& strs) {
        if (strs.size() == 0) {
            return "";
        }
        
        return getLongestCommonPrefix(strs, 0, strs.size()-1);
    }
    
    string getLongestCommonPrefix(vector<string>& strs, int l, int r) {
        if (l == r) {
            return strs[l];
        }
        else {
            int mid = (l + r)/2;
            string left = getLongestCommonPrefix(strs, l, mid);
            string right = getLongestCommonPrefix(strs, mid+1, r);
            return commonPrefix(left, right);
        }
    }
    
    string commonPrefix(string left, string right) {
        string commonPrefix = "";
        for (int i = 0; i < min(left.size(), right.size()); ++i) {
            cout << left[i] << " ";
            if (left[i] == right[i]) {
                commonPrefix+=left[i];
            }
            else {
                break;
            }
        }
        return commonPrefix;
    }
};
