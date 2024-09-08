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

function mergeNodes(head: ListNode | null): ListNode | null {
	const dummy: ListNode | null = new ListNode(0);
	let node: ListNode | null = dummy, current: ListNode | null = head.next;
	while (current !== null) {
		let s: number = 0;
		while (current !== null && current.val !== 0) {
			s += current.val;
			current = current.next;
		}
		node.next = new ListNode(s);
		node = node.next;
		if (current !== null) {
			current = current.next;
		}
	}
	return dummy.next;
};

export function Solve(inputJsonElement: string): any {
	const inputValues: string[] = inputJsonElement.split("\n");
	const head: ListNode | null = IntArrayToLinkedList(JSON.parse(inputValues[0]));
	return LinkedListToIntArray(mergeNodes(head));
}
