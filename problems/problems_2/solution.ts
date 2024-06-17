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

function addTwoNumbers(l1: ListNode | null, l2: ListNode | null): ListNode | null {
    const dummy: ListNode = new ListNode();
	let cur: number = 0;
	for (let node: ListNode | null = dummy; l1 != null || l2 != null || cur > 0; node = node!!.next) {
		if (l1 != null) {
			cur += l1.val;
			l1 = l1.next;
		}
		if (l2 != null) {
			cur += l2.val;
			l2 = l2.next;
		}
		node!!.next = new ListNode(cur % 10);
		cur = Math.floor(cur / 10);
	}
	return dummy.next;
};

export function Solve(inputJsonElement: string): any {
	const splits: string[] = inputJsonElement.split("\n");
	const l1: ListNode | null = IntArrayToLinkedList(JSON.parse(splits[0]));
	const l2: ListNode | null = IntArrayToLinkedList(JSON.parse(splits[1]));
	return LinkedListToIntArray(addTwoNumbers(l1, l2));
}
