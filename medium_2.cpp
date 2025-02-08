// 2. Add Two Numbers
// Solved
// Medium
// Topics
// Companies
// You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

// You may assume the two numbers do not contain any leading zero, except the number 0 itself.

 

// Example 1:


// Input: l1 = [2,4,3], l2 = [5,6,4]
// Output: [7,0,8]
// Explanation: 342 + 465 = 807.
// Example 2:

// Input: l1 = [0], l2 = [0]
// Output: [0]
// Example 3:

// Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
// Output: [8,9,9,9,0,0,0,1]
#include <iostream>

struct ListNode
{
    int val;
    ListNode *next;
    ListNode() : val(0), next(nullptr) {}
    ListNode(int x) : val(x), next(nullptr) {}
    ListNode(int x, ListNode *next) : val(x), next(next) {}
};

class Solution
{
public:
    ListNode *addTwoNumbers(ListNode *l1, ListNode *l2)
    {

        int extra_number = 0;
        ListNode *returnList = new ListNode();
        ListNode *head = returnList;
        while (l1 || l2 || extra_number != 0)
        {
            int sum = 0;
            int *ptr = &sum;
            if (l1)
            {
                *ptr = *ptr + l1->val;
                std::cout << *ptr << "\n";
                l1 = l1->next;
            }
            if (l2)
            {
                *ptr = *ptr + l2->val;
                std::cout << *ptr << "\n";

                l2 = l2->next;
            }
            *ptr += extra_number;
            extra_number = 0;
            while (sum > 9)
            {
                *ptr -= 10;
                extra_number++;
            }
            std::cout << sum << "\n";

            head->val = *ptr;

            if (l1 || l2 || extra_number)
            {
                head->next = new ListNode();
                head = head->next;
            }
        }

        return returnList;
    }
};
