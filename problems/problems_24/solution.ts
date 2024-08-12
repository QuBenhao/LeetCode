import {ListNode,IntArrayToLinkedList,LinkedListToIntArray} from "../../typescript/models/listnode";

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

function swapPairs(head: ListNode | null): ListNode | null {
    const dummy: ListNode = new ListNode(0, head);
	let prev: ListNode = dummy, cur: ListNode | null = head;
	while (cur && cur.next) {
		const nxt: ListNode = cur.next;
		cur.next = nxt.next;
		nxt.next = cur;
		prev.next = nxt;
		prev = cur;
		cur = cur.next;
	}
	return dummy.next;
};

export function Solve(inputJsonElement: string): any {
	const inputValues: string[] = inputJsonElement.split("\n");
	const head: ListNode | null = IntArrayToLinkedList(JSON.parse(inputValues[0]));
	return LinkedListToIntArray(swapPairs(head));
}
