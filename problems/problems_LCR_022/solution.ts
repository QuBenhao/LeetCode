import {LinkedListToIntArray,IntArrayToLinkedListWithCycle,ListNode} from "../../typescript/models/listnode";

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

function detectCycle(head: ListNode | null): ListNode | null {
    if (head === null || head.next === null) {
		return null;
	}
	let slow: ListNode | null = head, fast: ListNode | null = head;
	while (fast !== null && fast.next !== null) {
		slow = slow!.next;
		fast = fast.next.next;
		if (slow === fast) {
			let ptr: ListNode | null = head;
			while (ptr !== slow) {
				ptr = ptr!.next;
				slow = slow!.next;
			}
			return ptr;
		}
	}
	return null;
};

export function Solve(inputJsonElement: string): any {
	const inputValues: string[] = inputJsonElement.split("\n");
	const inputArray: number[] = JSON.parse(inputValues[0]);
	const cyclePos: number = JSON.parse(inputValues[1]);
	const head: ListNode | null = IntArrayToLinkedListWithCycle(inputArray, cyclePos);
	const res: ListNode | null = detectCycle(head);
	return res === null ? null : res.val;
}
