/**
 * Definition for a binary tree node.
 * function TreeNode(val) {
 *     this.val = val;
 *     this.left = this.right = null;
 * }
 */
/**
 * @param {TreeNode} root
 * @param {TreeNode} p
 * @param {TreeNode} q
 * @return {TreeNode}
 */
var lowestCommonAncestor = function(root, p, q) {
    let pOrQfound = false;
    let pFound = false;
    let qFound = false;

    let traverse = (node, stack, el) => {
        if(!node) return;

        stack.push(node);

        if (node === el) {
            return node;
        }

        if (node.val > el.val) {
            traverse(node.left, stack, el);
        }
        else {
            traverse(node.right, stack, el);
        }
    };

    let pStack = [];
    let qStack = [];

    traverse(root, pStack, p);
    traverse(root, qStack, q);

    console.log("Pstack length:" + pStack.length)
    console.log("Qstack length:" + qStack.length)

    if(pStack.length > qStack.length) {
        let j = 0;
        while (j < pStack.length) {
            console.log("Checking:" + pStack[j])
            if(pStack[j] !== qStack[j]) {
                return pStack[j-1];
            }
            j++;
        }
    }
    else {
        let j = 0;
        while (j < qStack.length) {
            if(pStack[j] !== qStack[j]) {
                return qStack[j-1];
            }
            j++;
        }
    }
};
