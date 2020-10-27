#include <math.h>

/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */


struct ListNode* addTwoNumbers(struct ListNode* l1, struct ListNode* l2){
    int power = 0;
    int result = 0;
    int carry = 0;        
        
    struct ListNode *head = malloc(sizeof(struct ListNode));
    head->next = NULL;
    struct ListNode *curr = head;
    
    while (l1 && l2) {
        int current = l1->val + l2->val + carry;   
        carry = current / 10;
        curr->next = malloc(sizeof(struct ListNode));
        curr->next->val = current%10;
        curr->next->next = NULL;
        curr = curr->next;
        l1 = l1->next;
        l2 = l2->next;
    }
    while (l1) {
        int current = l1->val + carry;
        carry = current/10;
        curr->next = malloc(sizeof(struct ListNode));
        curr->next->val = current%10;
        curr->next->next = NULL;
        curr = curr->next;
        l1 = l1->next;
    }
    while (l2) {
        int current = l2->val + carry;
        carry = current/10;
        curr->next = malloc(sizeof(struct ListNode));
        curr->next->val = current%10;
        curr->next->next = NULL;
        curr = curr->next;
        l2= l2->next;
    }
    
    if (carry) {
        curr->next = malloc(sizeof(struct ListNode));
        curr->next->val = carry;
        curr->next->next = NULL;
    }
    
    return head->next;
}
