class ListNode {
    val: number
    next: ListNode | null

    constructor(val?: number, next?: ListNode | null) {
        this.val = (val === undefined ? 0 : val)
        this.next = (next === undefined ? null : next)
    }
}

function LinkedListToIntArray(node: ListNode | null): Array<number> {
    const ans: Array<number> = [];
    while (node != null) {
        ans.push(node.val);
        node = node.next;
    }
    return ans;
}

function IntArrayToLinkedList(arr: Array<number>): ListNode | null {
    const dummy: ListNode = new ListNode();
    let node: ListNode | null = dummy;
    for (const v of arr) {
        node.next = new ListNode(v);
        node = node?.next;
    }
    return dummy.next;
}


export {ListNode, LinkedListToIntArray, IntArrayToLinkedList};