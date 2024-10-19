import {IntArrayToLinkedList,ListNode,LinkedListToIntArray} from "../../typescript/models/listnode";

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
function reverseLinkedList(head: ListNode | null): ListNode | null {
	let prev: ListNode | null = null;
	let current: ListNode | null = head;
	while (current !== null) {
		let next: ListNode | null = current.next;
		current.next = prev;
		prev = current;
		current = next;
	}
	return prev;
}

function addTwoNumbers(l1: ListNode | null, l2: ListNode | null): ListNode | null {
	l1 = reverseLinkedList(l1);
	l2 = reverseLinkedList(l2);
	let dummy: ListNode = new ListNode(0);
	let current: ListNode = dummy;
	let carry: number = 0;
	while (l1 !== null || l2 !== null) {
		let x: number = (l1 !== null) ? l1.val : 0;
		let y: number = (l2 !== null) ? l2.val : 0;
		let sum: number = x + y + carry;
		carry = Math.floor(sum / 10);
		current.next = new ListNode(sum % 10);
		current = current.next;
		if (l1 !== null) l1 = l1.next;
		if (l2 !== null) l2 = l2.next;
	}
	if (carry > 0) {
		current.next = new ListNode(carry);
	}
	return reverseLinkedList(dummy.next);
};

export function Solve(inputJsonElement: string): any {
	const inputValues: string[] = inputJsonElement.split("\n");
	const l1: ListNode | null = IntArrayToLinkedList(JSON.parse(inputValues[0]));
	const l2: ListNode | null = IntArrayToLinkedList(JSON.parse(inputValues[1]));
	return LinkedListToIntArray(addTwoNumbers(l1, l2));
}
