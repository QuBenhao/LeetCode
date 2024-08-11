import {ListNode,LinkedListToIntArray,IntArrayToLinkedList} from "../../typescript/models/listnode";

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

function removeNthFromEnd(head: ListNode | null, n: number): ListNode | null {
	let slow: ListNode | null = head, fast: ListNode | null = head;
	for (let i: number = 0; i < n; i++) {
		fast = fast?.next;
	}
	if (!fast) {
		return head?.next;
	}
	while (fast?.next) {
		slow = slow?.next;
		fast = fast.next;
	}
	slow!.next = slow!.next!.next;
	return head;
};

export function Solve(inputJsonElement: string): any {
	const inputValues: string[] = inputJsonElement.split("\n");
	const head: ListNode | null = IntArrayToLinkedList(JSON.parse(inputValues[0]));
	const n: number = JSON.parse(inputValues[1]);
	return LinkedListToIntArray(removeNthFromEnd(head, n));
}
