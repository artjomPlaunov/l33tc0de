/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     struct TreeNode *left;
 *     struct TreeNode *right;
 * };
 */
void aux(struct TreeNode* root, struct TreeNode* new);

struct TreeNode* insertIntoBST(struct TreeNode* root, int val){
    struct TreeNode* new_node = malloc(sizeof(struct TreeNode));
    new_node->val = val;
    new_node->left = NULL;
    new_node->right = NULL;
    if (root == NULL) {
        return new_node;
    }
    aux(root, new_node);
    return root;
}

void aux(struct TreeNode* root, struct TreeNode* new) {
    if (new->val > root->val) {
        if (root->right == NULL) {
            root->right = new;
        } else {
            aux(root->right, new);
        }
    } else {
        if (root->left == NULL) {
            root->left = new;
        } else {
            aux(root->left, new);
        }
    }
}
