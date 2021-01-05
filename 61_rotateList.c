/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */

int get_length(struct ListNode* head) {
    int res = 0;
    while (head) {
        res++;
        head = head->next;
    }
    return res;
}

struct ListNode* rotateRight(struct ListNode* head, int k) {
    if (k == 0) {
        return head;
    } else if (head == NULL) {
        return NULL;
    } else if (head->next == NULL) {
        return head;
    }
    int len = get_length(head);
    k = k%len;
    if (k == 0) {
        return head;
    }
    
    struct ListNode* cur = head;
    for (int i = 0; i < len-k-1; i++) {
        cur = cur->next;
    }
    // Save head int tmp
    // Set head to last k elements
    // Set cur to null
    // iterate over new head, save tmp into end of new head 
    
    struct ListNode* tmp = head;
    head = cur->next;
    cur->next = NULL;
    cur = head;
    while (cur->next) {
        cur = cur->next;
    }
    cur->next = tmp;
    return head;
}
