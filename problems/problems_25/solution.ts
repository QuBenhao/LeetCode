import {LinkedListToIntArray,IntArrayToLinkedList,ListNode} from "../../typescript/models/listnode";

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

function reverseKGroup(head: ListNode | null, k: number): ListNode | null {
	if (head == null) {
		return null;
	}
	let node: ListNode | null = head;
	for (let i: number = 0; i < k - 1; i++) {
		if (node == null) {
			return head;
		}
		node = node.next;
	}
	if (node == null) {
		return head;
	}
	node.next = reverseKGroup(node.next, k);
	const last: ListNode | null = node.next;
	let tail: ListNode | null = last;
	while (head != last) {
		const next: ListNode | null = head.next;
		head.next = tail;
		tail = head;
		head = next;
	}
	return node;
};

export function Solve(inputJsonElement: string): any {
	const inputValues: string[] = inputJsonElement.split("\n");
	const head: ListNode | null = IntArrayToLinkedList(JSON.parse(inputValues[0]));
	const k: number = JSON.parse(inputValues[1]);
	return LinkedListToIntArray(reverseKGroup(head, k));
}
