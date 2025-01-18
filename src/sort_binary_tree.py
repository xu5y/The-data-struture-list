class Node():

    def __init__(self, key):
        self.val = key
        self.right = None
        self.left = None


class Two_Tree(object):

    def __init__(self):
        self.root = None

    #创建排序二叉树
    def insert(self, key):
        if self.root is None:
            self.root = Node(key)
        else:
            self._insert(self.root, key)

    def _insert(self, node, key):
        if key < node.val:
            if node.left is None:
                node.left = Node(key)
            else:
                self._insert(node.left, key)
        else:
            if key > node.val:
                if node.right is None:
                    node.right = Node(key)
                else:
                    self._insert(node.right, key)

    #查找二叉树
    def search(self, key):
        return self._search(self.root, key)

    def _search(self, node, key):
        if node is None:
            return False

        if key == node.val:
            return True
        elif key < node.val:
            return self._search(node.left, key)
        else:
            return self._search(node.right, key)

    #删除值
    def delete(self, key):
        self.root = self._delete(self.root, key)

    #如果是删除叶子节点，直接删，
    # 如果删除只有左或右子树的节点，直接让下面的子树代替它，，
    # 删除都有的，找到左子树中的最大节点/右子树的最小节点，代替要删除的节点，然后删除原位置的那个节点

    #先写一个找到最小值的
    def find_minimun(self,node):
        current = node  #不然会改变node的值
        while current.left is not None:
            current = current.left
        return current
#_delete函数，这里最好用root，因为root已经初始化好了
# 如果用node,在用户输入的时候需要再输入一个根节点的值，但是用户在输入的时候不可能去想你的根节点是什么值，

    def _delete(self, root, key):

        #第66-72，只是为了判断key值能不能等于Node.val
        if root is None:
            return root#返回root,保证代码一致性
        else:
            if key < root.val:
                root.left = self._delete(root.left, key)
            elif key > root.val:
                root.right = self._delete(root.right, key)
            else:  #key=node.val
                #1：节点只有一个左子树或者一个右子树
                if root.left is None:
                    root = root.right
                    return root
                elif root.right is None:
                    root = root.left
                    return root

#2：节点有2个节点，以右节点的最小作为根节点，然后删除该节点
                current = self.find_minimun(root.right)
                root.val = current.val
                root.right = self._delete(root.right, current.val)#必须传入root,right,如果传入root的话，前面已经让root.val=cuurent.val了，再调用的话，会无限循坏，即每次都尝试删除同一个节点。

        return root

    def inorder_traval(self, ):
        result = []
        self._inorder_traval(self.root, result)
        return result

    def _inorder_traval(self, node, result):
        if node:
            self._inorder_traval(node.left, result)
            result.append(node.val)
            self._inorder_traval(node.right, result)


#测试案例
if __name__ == "__main__" :
    test_tree = Two_Tree()
    #插入和遍历通过下面的insert和print语句可以检查到有无错误
    test_tree.insert(50)  #这里不用再写Node节点，直接输入key值就行
    test_tree.insert(30)
    test_tree.insert(40)
    test_tree.insert(120)
    test_tree.insert(600)
    test_tree.insert(700)
    test_tree.insert(90)

    print("中序遍历：", test_tree.inorder_traval())
    #检查search函数
    print("查找30:",test_tree.search(30))
    #检查删除函数
    test_tree.delete(120)