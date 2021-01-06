/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */


struct ListNode* deleteDuplicates(struct ListNode* head){
    struct ListNode* aux = malloc(sizeof(struct ListNode));
    aux->next = head;
    struct ListNode* cur = aux;
    
    while (cur->next && cur->next->next) {
        if (cur->next->val == cur->next->next->val) {
            int v = cur->next->val;
            struct ListNode* fwd = cur->next->next->next;
            while (fwd) {
                if (fwd->val == v) {
                    fwd = fwd->next;
                } else {
                    break;
                }
            }
            cur->next = fwd;
        } else {
            cur = cur->next;
        }
    }
    return aux->next;
}
