// 55. Jump Game
// Solved
// Medium
// Topics
// Companies
// You are given an integer array nums. You are initially positioned at the array's first index, and each element in the array represents your maximum jump length at that position.

// Return true if you can reach the last index, or false otherwise.

 

// Example 1:

// Input: nums = [2,3,1,1,4]
// Output: true
// Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.
// Example 2:

// Input: nums = [3,2,1,0,4]
// Output: false
// Explanation: You will always arrive at index 3 no matter what. Its maximum jump length is 0, which makes it impossible to reach the last index.
 

// Constraints:


public class Solution {
    public bool CanJump(int[] nums) {

        Dictionary<int, bool> openWith = new Dictionary<int, bool>();
        return recursivePath(0,nums,openWith);

        
    }

    public bool recursivePath(int index,int[] nums,Dictionary<int, bool>  openWith){
        
        if(index == nums.Length -1){
            return true;
        }else if(nums[index] == 0){
            return false;
        }

        bool result;
        for(int i=nums[index];i>0;i--){
            if(index + i<nums.Length){
                if(openWith.ContainsKey(index+i)){
                    result = openWith[index+i];
                }else{
                    result = recursivePath(index + i,nums,openWith);
                    openWith[index+i] = result;
                }
                
                if(result){
                    return true;
                }
            }
        }
        return false;
        



    }
}
