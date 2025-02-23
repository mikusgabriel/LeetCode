
// 19. Remove Nth Node From End of List
// Solved
// Medium
// Topics
// Companies
// Hint
// Given the head of a linked list, remove the nth node from the end of the list and return its head.

 

// Example 1:


// Input: head = [1,2,3,4,5], n = 2
// Output: [1,2,3,5]
// Example 2:

// Input: head = [1], n = 1
// Output: []
// Example 3:

// Input: head = [1,2], n = 1
// Output: [1]

/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     public int val;
 *     public ListNode next;
 *     public ListNode(int val=0, ListNode next=null) {
 *         this.val = val;
 *         this.next = next;
 *     }
 * }
 */

public class Solution {
    public ListNode RemoveNthFromEnd(ListNode head, int n) {
        if (head == null){
            return head;
        }
        

        ListNode curr = head;
        int lenght = 0;

        while(curr != null){
            lenght++;
            curr = curr.next;
        } 

        if(lenght == n){
            return head.next;
        }
        int posWanted = lenght - n;

        curr = head;
        lenght = 0;
        while(curr != null){
            lenght++;
            if(lenght == posWanted){
                
                if(curr.next.next != null){
                    curr.next = curr.next.next;
                }else{
                    curr.next = null;
                }
            }
            curr = curr.next;
        }

        return head;

        
    }
}
