/**
 * Definition for a binary tree node.
 * function TreeNode(val) {
 *     this.val = val;
 *     this.left = this.right = null;
 * }
 */
/**
 * @param {TreeNode} root
 * @return {number}
 */

function TreeNode(val) {
    this.val = val;
    this.left = this.right = null;
}

var maxDepth = function(root) {
  "use strict";
  let max = 1;
  if(!root) return 0;

  let traverse = (root, curDepth) => {
    max = Math.max(max, curDepth);
    if(!root) return;
    if(root.left) traverse(root.left, curDepth+1);
    if(root.right) traverse(root.right, curDepth+1);
  };

  traverse(root, 1);
  return max;
};