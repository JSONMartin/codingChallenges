    def getHeight(self,root):
        max_height = 0
        def traverse(root, cur_height):
            nonlocal max_height
            #print("Root data:%d" % root.data)
            #print("Cur Height:%d" % cur_height)
            if root.left != None:
                traverse(root.left, cur_height + 1)
            if root.right != None:
                traverse(root.right, cur_height + 1)
            else:
                max_height = max(max_height, cur_height) #set max height
        traverse(root, 0)
        #print(max_height)
        return max_height
