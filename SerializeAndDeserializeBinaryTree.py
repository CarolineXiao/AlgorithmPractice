# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        if root == None:
            return ""
        
        data = ""
        data = data + str(root.val)
        
        queue = []
        queue.append(root)
        
        while queue:
            node = queue.pop(0)
            data += ","
            if node.left != None:
                n_l = node.left
                data += str(n_l.val)
                queue.append(node.left)
            else:
                data += "null"
                
            data += ","
            if node.right != None:
                data += str(node.right.val)
                queue.append(node.right)
            else:
                data += "null"
        data = data.rstrip(",null")   
        return data
        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        if data == "":
            return None
        
        # make all nodes
        node = []
        for n in data.split():
            if n != 'null':
                new_node = TreeNode(n)
                node.append(new_node)
            else:
                node.append(None)
        
        left = 0
        right = 1
        
        while right < len(node):
            while node[left] == None:
                left += 1
            node[left].left = node[right]
            node[left].right = node[right+1]
            right += 2
            left += 1
            
        return node[0]

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))
