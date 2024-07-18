import {ListNode, IntArrayToLinkedListWithCycle} from "../../typescript/models/listnode";

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

function hasCycle(head: ListNode | null): boolean {
    if (head == null) {
		return false;
	}
	let slow: ListNode | null = head, fast: ListNode | null = head;
	while (fast != null && fast.next != null) {
		slow = slow?.next;
		fast = fast.next.next;
		if (slow == fast) {
			return true;
		}
	}
	return false;
};

export function Solve(inputJsonElement: string): any {
	const inputValues: string[] = inputJsonElement.split("\n");
	const array: number[] = JSON.parse(inputValues[0]);
	const pos: number = JSON.parse(inputValues[1]);
	const head: ListNode | null = IntArrayToLinkedListWithCycle(array, pos);
	return hasCycle(head);
}
