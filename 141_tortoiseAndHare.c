/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
bool hasCycle(struct ListNode *head) {
    if (head == NULL || head->next == NULL) {
        return false;
    } 
    struct ListNode *tortoise = head;
    struct ListNode *hare = head->next;
    
    while (tortoise && hare) {
        if (tortoise == hare) {
            return true;
        }
        tortoise = tortoise->next;
        if (hare->next && hare->next->next) {
            hare = hare->next->next;
        } else {
            return false;
        }
    }
    return false;
}
