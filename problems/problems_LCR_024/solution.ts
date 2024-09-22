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

function reverseList(head: ListNode | null): ListNode | null {
	const dummy: ListNode = new ListNode();
	let current: ListNode | null = head;
	while (current !== null) {
		const next: ListNode = current.next;
		current.next = dummy.next;
		dummy.next = current;
		current = next;
	}
	return dummy.next;
};

export function Solve(inputJsonElement: string): any {
	const inputValues: string[] = inputJsonElement.split("\n");
	const head: ListNode | null = IntArrayToLinkedList(JSON.parse(inputValues[0]));
	return LinkedListToIntArray(reverseList(head));
}
