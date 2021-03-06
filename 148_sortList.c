/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */

typedef struct ListNode* listNode;

listNode merge(listNode l1, listNode l2) {
    listNode aux = malloc(sizeof(struct ListNode));
    listNode cur = aux;
    
    while (l1 && l2) {
        if (l1->val < l2->val) {
            cur->next = l1;
            l1 = l1->next;
        } else {
            cur->next = l2;
            l2 = l2->next;
        }
        cur = cur->next;
        cur->next = NULL;
    }
    if (l1) {
        cur->next = l1;
    } else if (l2) {
        cur->next = l2;
    }
    return aux->next;
}

int getLen(listNode head) {
    listNode cur = head;
    int res = 0;
    while (cur) {
        res += 1;
        cur = cur->next;
    }
    return res;
}

listNode mergeSort(listNode head) {
    if (head == NULL) {
        return NULL;
    } else if (!head->next) {
        return head;
    } 
    
    int len = getLen(head)/2;
    listNode left,right;
    listNode cur = head;
    
    for (int i = 1; i < len; i++) {
        cur = cur->next;
    }
    left = head;
    right = cur->next;
    cur->next = NULL;
    
    left = mergeSort(left);
    right = mergeSort(right);
    return merge(left,right);
}

struct ListNode* sortList(listNode head){
    if (!head) {
        return head;
    }
    
    head = merge(head,NULL);
    listNode res = mergeSort(head);
    return res;
}

