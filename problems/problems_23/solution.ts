import {ListNode,LinkedListToIntArray,IntArrayToLinkedList} from "../../typescript/models/listnode";
import {MinPriorityQueue} from "@datastructures-js/priority-queue";

/**
 * Definition for singly-linked list.
 * class ListNode {
 *     val: number
 *     next: ListNode | null
 *     constructor(val?: number, next?: ListNode | null) {
 *         this.val = (val===undefined ? 0 : val)
 *         this.next = (next===undefined ? null : next)
 *     }
 * }
 */

function mergeKLists(lists: Array<ListNode | null>): ListNode | null {
    const pq = new MinPriorityQueue({ priority: (node: ListNode) => node.val });
    for (const head of lists) {
        if (head) {
            pq.enqueue(head);
        }
    }
    const dummy: ListNode = new ListNode();
    let cur: ListNode = dummy;
    while (!pq.isEmpty()) {
        const node = pq.dequeue().element;
        cur.next = node;
        cur = cur.next;
        if (node.next) {
            pq.enqueue(node.next);
        }
    }
    return dummy.next;
}

export function Solve(inputJsonElement: string): any {
	const inputValues: string[] = inputJsonElement.split("\n");
	const jsonArray0: any = JSON.parse(inputValues[0]);
	const lists: Array<ListNode | null> = [];
	for (let i = 0; i < jsonArray0.length; i++) {
		lists.push(IntArrayToLinkedList(jsonArray0[i]));
	}
	return LinkedListToIntArray(mergeKLists(lists));
}
