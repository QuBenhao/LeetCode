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

function IntArrayToLinkedListWithCycle(arr: Array<number>, pos: number): ListNode | null {
    const dummy: ListNode = new ListNode();
    let node: ListNode | null = dummy;
    let cycle: ListNode | null = null;
    for (let i: number = 0; i < arr.length; i++) {
        node.next = new ListNode(arr[i]);
        node = node?.next;
        if (i == pos) {
            cycle = node;
        }
    }
    node.next = cycle;
    return dummy.next;
}

function IntArrayToIntersectionLinkedList(iv: number, arr1: Array<number>, arr2: Array<number>,skipA: number, skipB: number): Array<ListNode> {
    const headA: ListNode | null = IntArrayToLinkedList(arr1);
    if (iv == 0 || skipA == arr1.length || skipB == arr2.length) {
        return [headA, IntArrayToLinkedList(arr2)];
    }
    let pa: ListNode | null = headA;
    for (let i: number = 0; i < skipA; i++) {
        pa = pa?.next;
    }
    const headB: ListNode | null = skipB == 0 ? pa : new ListNode(arr2[0]);
    let pb: ListNode | null = headB;
    for (let i: number = 1; i < skipB; i++) {
        pb!!.next = new ListNode(arr2[i]);
        pb = pb?.next;
    }
    pb.next = pa;
    return [headA, headB];
}


export {ListNode, LinkedListToIntArray, IntArrayToLinkedList, IntArrayToLinkedListWithCycle, IntArrayToIntersectionLinkedList};