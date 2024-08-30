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

function sortList(head: ListNode | null): ListNode | null {
	if (head === null || head.next === null) {
		return head;
	}
	let slow: ListNode | null = head, fast: ListNode | null = head.next;
	while (fast != null && fast.next != null) {
		slow = slow!.next;
		fast = fast.next.next;
	}
	let right: ListNode | null = sortList(slow!.next);
	slow!.next = null;
	let left: ListNode | null = sortList(head);
	const dummy: ListNode = new ListNode(0);
	let node: ListNode = dummy;
	while (left !== null && right !== null) {
		if (left.val < right.val) {
			node.next = left;
			left = left.next;
		} else {
			node.next = right;
			right = right.next;
		}
		node = node.next;
	}
	node.next = left === null ? right : left;
	return dummy.next;
};

export function Solve(inputJsonElement: string): any {
	const inputValues: string[] = inputJsonElement.split("\n");
	const head: ListNode | null = IntArrayToLinkedList(JSON.parse(inputValues[0]));
	return LinkedListToIntArray(sortList(head));
}
