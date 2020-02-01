/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
class Solution {
public:
    ListNode* mergeTwoLists(ListNode* l1, ListNode* l2) {
        ListNode *p1 = l1;
        ListNode *p2 = l2;
        
        ListNode *newList = NULL;
        ListNode *cur = NULL;
        
        
        while (!(p1 == NULL && p2 == NULL)) {
            if ((p2 == NULL) || ((p2 !=NULL && p1!=NULL) && ((*p1).val <= (*p2).val))) {
                if (cur == NULL) {
                    newList = new ListNode((*p1).val);
                    cur = newList;
                }
                else {
                    (*cur).next = new ListNode((*p1).val);
                    cur = (*cur).next;
                }
                p1 = (*p1).next;
            }
            else {
                if (cur == NULL) {
                    newList = new ListNode((*p2).val);
                    cur = newList;
                }
                else {
                    (*cur).next = new ListNode((*p2).val);
                    cur = (*cur).next;
                }
                p2 = (*p2).next;
            }
        }
        return newList;
    }
};
