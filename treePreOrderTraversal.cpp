/*
// Definition for a Node.
class Node {
public:
    int val;
    vector<Node*> children;

    Node() {}

    Node(int _val) {
        val = _val;
    }

    Node(int _val, vector<Node*> _children) {
        val = _val;
        children = _children;
    }
};
*/
class Solution {
public:
    vector<int> preorder(Node* root) {
        vector<int> tree;
        if (root == NULL) {
            return tree;
        }
        tree.push_back(root->val);
        appendValue(root, tree);
        return tree;
        
        
    }
    
    void appendValue(Node* root, vector<int>& tree) {
        if (root->children.size() == 0) {
            return;
        }
        for (int i = 0; i < root->children.size(); ++i) {
            Node* newRoot = root->children[i];
            tree.push_back(newRoot->val);
            appendValue(newRoot, tree);
        }
    }
};
