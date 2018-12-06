#### 1. 二叉树添加节点
```
def add(self,elem):
	node = Node(elem)
	if self.root.elem == -1: #没有节根点，对根节点赋值
		self.root = node
		self.myQueue.append(self.root)
	else:
		treeNode = self.myQueue[0] #此节点的子树没有齐
		if treeNode.lchild == None: #添加节点时，从左边开始添加
			treeNode.lchild = node
			self.myQueue.append(treeNode.lchild)
		else:
			treeNode.rchild = node
			self.myQueue.append(treeNode.rchild)
			self.myQueue.pop(0) #如果该节点存在右子树，将此节点抛弃。
```

#### 2. 三种遍历，分别递归和非递归算法
```

result = []
def front_recursive(self,root):
	if root == None:
		return
	result.append(root.elem)
	self.front_recursive(root.lchild)
	self.front_recursive(root.rchild)

def front_stack(self,root):
	if root == None:
		return
	stack = []
	result = []
	node = root
	while node or stack:
		while node:
			result.append(node.elem)
			stack.append(node)
		node = stack.pop()
		node = node.right


def mid_recursive(self,root):
	if root == None:
		return
	self.mid_recursive(self.lchild)
	result.append(root.elem)
	self.mind_recursive(self.rchild)

def mid_stack(self,root):
	if root == None:
		return
	stack = []
	result = []
	while node or stack:
		while node:  # 从根节点开始，一直找到左子树
			stack.append(node)
			node = node.left
		node = stack.pop() #while结束，表示当前没有左子树了,最后一个 node.left为空，所以栈上保存的是最下面的左子树
		result.append(node.elem)
		node = node.right 


def later_recursive(self,root):
	if root == None:
		return
	self.later_recursive(self.lchild)
	self.later_recursive(self.rchild)
	result.append(root.elem)

def later_stack(self,root):
	if root == None:
		return
	stack1 = []
	stack2 = []
	result = []
	stack1.append(node)
	while stack1: #找出后序遍历的逆序
		node = stack1.pop()
		if node.lchild:
			stack1.append(node.lchild)
		if node.rchild:
			stack1.append(node.right)
		stack2.append(node)
	while stack2: #stack2为后序遍历的逆序，出栈后即为后序遍历的序列
		result.append(stack2.pop())

```

#### 3.层次遍历
```
def level_queue(self,root):
	if root == None:
		return
	queue = []
	node = root
	queue.append(node)
	while queue:
		node = queue.pop()
		result.append(node.elem)
		if node.left != None:
			queue.append(node.lchild)
		if node.right != None:
			queue.append(node.rchild)
```

#### 4.给出前序和中序，构建二叉树
要记住一点，递归的时候，如果构建左子树，两个参数都是表示左子树的序列，只是一个参数表示中序，一个参数表示前序。构建右子树同理
```
def buildTree(self, preorder, inorder):
   """
   :type preorder: List[int]
   :type inorder: List[int]
   :rtype: TreeNode
   """
   length = len(preorder)
   if length == 0:
       return None
   if length == 1:
       return TreeNode(preorder[0])
   root = TreeNode(preorder[0])
   index = inorder.index(root.val)
   root.left = self.buildTree(preorder[1:index+1],inorder[0:index])
   root.right = self.buildTree(preorder[index+1:length],inorder[index+1:length])
   return root
```
#### 5.给出后序和中序，构建二叉树
和上面思路差不多。
```
def buildTree(self,inorder,postorder):
	 length = len(inorder)
   if length == 0:
       return None
   if length == 1:
       return TreeNode(postorder[length-1])
   root = TreeNode(postorder[length-1])
   index = inorder.index(root.val)
   root.left = self.buildTree(inorder[0:index],postorder[0,index])
   root.right = self.buildTree(inorder[index+1:length],postorder[index+1:length-1]) 
```

#### 6.给定排序好的数组，把它转换为二叉查找树，要求生成的二叉查找树是平衡的。
https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/description/

因为数组已经排序好了，取中间的元素作为二叉查找树的根节点，然后递归生成。可以不区分奇偶，注意python3的除法问题即可
```
def sortedArrayToBST(self, nums):
   """
   :type nums: List[int]
   :rtype: TreeNode
   """
   length = len(nums)
   if length == 0:
       return None
   if length == 1:
       return TreeNode(nums[0])
   root = TreeNode(nums[length//2])
   root.left = self.sortedArrayToBST(nums[:length//2])
   root.right = self.sortedArrayToBST(nums[length//2+1:])
   return root
```

#### 7. 反向层次遍历二叉树,按层次输出
https://leetcode.com/problems/binary-tree-level-order-traversal-ii/description/
层次遍历结果反过来即可。
```
def levelOrderBottom(self, root):
   """
   :type root: TreeNode
   :rtype: List[List[int]]
   """
   tree = []
   if root == None:
       return tree
   curr_level = [root]
   while curr_level:
       level_list = []
       next_list = []
       for tmp in curr_level:
           level_list.append(tmp.val)
           if tmp.left != None:
               next_list.append(tmp.left)
           if tmp.right != None:
               next_list.append(tmp.right)
       tree.append(level_list)
       curr_level = next_list
   tree.reverse()
   return tree
```
#### 8.之字形层次遍历二叉树
https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/description/
其实也是层次遍历，和上面那题一样,加个奇偶判断就可以了。层次遍历基本都是这个套路
```
def zigzagLevelOrder(self, root):
   """
   :type root: TreeNode
   :rtype: List[List[int]]
   """
   tree = []
   if root == None:
       return tree
   curr_level = [root]
   num = 1
   while curr_level:
       curr_list = []
       next_list = []
    
       for tmp in curr_level:
           curr_list.append(tmp.val)
           if tmp.left:
               next_list.append(tmp.left)
           if tmp.right:
               next_list.append(tmp.right)
               
       if num % 2 == 0:
           curr_list.reverse()
       tree.append(curr_list)
       curr_level = next_list
       num += 1

   return tree
```
#### 9.二叉树路径总和
https://leetcode.com/problems/path-sum/description/
给定一棵树和一个和，判断是否存在根到叶子节点的路径，使得路径上节点总和为给定的值。必须贯穿到最下面的叶子节点。

题目说到从根到XX节点，那肯定是优先考虑先序遍历,或者深度优先。
然后就是二叉树题，没什么额外要求的话，优先考虑递归解决。
```
def hasPathSum(self, root, sum):
   """
   :type root: TreeNode
   :type sum: int
   :rtype: bool
   """
   if root == None:
       return False
   if root.left == None and root.right == None:
       return sum == root.val
   return self.hasPathSum(root.left,sum-root.val) or self.hasPathSum(root.right,sum-root.val)
```
#### 10.列举二叉树路径总和的结果
https://leetcode.com/problems/path-sum-ii/description/
这里需要使用嵌套函数


#### 11.二叉树的下一个节点
https://www.nowcoder.com/practice/9023a0c988684a53960365b889ceaf5e?tpId=13&tqId=11210&tPage=1&rp=1&ru=/ta/coding-interviews&qru=/ta/coding-interviews/question-ranking
这题分三个步骤，首先是通过next找到根节点，然后进行中序遍历，最后找到目标节点的下一个节点。
```
def GetNext(self, pNode):
        dummy = pNode
        while dummy.next:
            dummy = dummy.next
        #找到根节点
        self.result = []
        #中序遍历
        self.midReverse(dummy)
        #条件检查，输出目标节点
        if self.result.index(pNode) != len(self.result) -1:
            pIndex = self.result.index(pNode)
            return self.result[pIndex+1]
        else:
            return None
        
    def midReverse(self,node):
        if node == None:
            return 
        self.midReverse(node.left)
        self.result.append(node)
        self.midReverse(node.right)
```



