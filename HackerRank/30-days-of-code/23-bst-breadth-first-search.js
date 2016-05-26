var queue = [];
queue.unshift(root);
while(queue.length > 0) {
    let node = queue.pop();
    process.stdout.write(node.data + ' ');
    if(node.left) { queue.unshift(node.left); }
    if(node.right) { queue.unshift(node.right); }
}
