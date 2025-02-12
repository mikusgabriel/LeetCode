
// Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.

// Assume the environment does not allow you to store 64-bit integers (signed or unsigned).

 

// Example 1:

// Input: x = 123
// Output: 321
// Example 2:

// Input: x = -123
// Output: -321
// Example 3:

// Input: x = 120
// Output: 21
 









#include <iostream>
#include <string>
#include <climits>  // For INT_MIN and INT_MAX



class Solution {
    public:
        int reverse(int x) {
    
            bool isNeg = false;
            if(x<0){
                isNeg=true;
            }
            std::string string_x = std::to_string(x);
            for(int i=0;i<string_x.size()/2;i++){
                // char* first_ptr = &string_x[i];
                // char* second_ptr = &string_x[string_x.size()-1-i];
    
                // char temp = *first_ptr;
                // *first_ptr = *second_ptr;
                // *second_ptr = temp;
    
    
                char temp = string_x[i];
                string_x[i] = string_x[string_x.size()-1-i];
                string_x[string_x.size()-1-i] = temp;
        
            }
            long long reversedNum = std::stoll(string_x);
    
            if(INT_MIN  <= reversedNum && reversedNum <=  INT_MAX){
    
                return isNeg ? -1 * reversedNum : reversedNum;
            }else{
                return 0;
            }
    
          
    
            
        }
    };
