// LeetCode: https://leetcode.com/problems/longest-palindromic-substring

#include <iostream>
#include <vector>
#include <string>
    
std::string longest_palindrome(const std::string& s) {
    /**
     * Faster method to find the longest palindrome in a string.
     * Uses a dynamic programming approach.
     * 
     * DP table size: n x n -> O(n^2)
     * DP row: start index for substring
     * DP col: end index for substring
     * DP entry: 1 if palindrome, 0 otherwise
     * 
     * 1) Initialize DP table with all length-1 and length-2 palindromes O(n)
     * 2) Iterate through length-3 substrings onwards and check previous entries in table
     * 
     * Complexity: O(n^2)
     */
    int i, j, length;
    
    // Current max plaindrome length and indices
    int max_length = 1;
    int longest[2] = {0, 0};
    
    if (s.size() == 1)
        return s;
    
    // DP table
    std::vector<std::vector<int>> table;
    table.reserve(s.size());
    
    // Init table with length-1 and -2 palindromes
    for (i = 0; i < s.size(); i++) {
        std::vector<int> row;
        row.resize(s.size());
        
        row[i] = 1;
        
        // Record any length-2 palindromes as longest
        if (i < s.size()-1 && s[i] == s[i+1]) {
            row[i+1] = 1;
            max_length = 2;
            longest[0] = i;
            longest[1] = i+1;
        }                
        
        table.push_back(row);
    }
    
    // Find all > length-3 palindromes (where l is length-1)
    for (int l = 2; l < s.size(); l++) {
        for (i = 0, j = i + l; j < s.size(); i++, j++) {
            if (s[i] == s[j] && table[i+1][j-1]) {
                table[i][j] = 1;
                length = j - i + 1;
                
                if (length > max_length) {
                    max_length = length;
                    longest[0] = i;
                    longest[1] = j;
                }
            }
            else
                table[i][j] = 0;
        }
    }
    
    // Return longest found palindrome
    return s.substr(longest[0], longest[1]-longest[0] + 1);
}

int main() {
    std::cout << longest_palindrome("abbba") << std::endl;
    return 0;
}
