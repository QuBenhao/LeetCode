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

function mergeTwoLists(list1: ListNode | null, list2: ListNode | null): ListNode | null {
	const dummy: ListNode = new ListNode();
	let node: ListNode = dummy;
	while (list1 !== null || list2 !== null) {
		if (list2 === null || (list1 !== null && list1.val < list2.val)) {
			node.next = list1;
			list1 = list1.next;
		} else {
			node.next = list2;
			list2 = list2.next;
		}
		node = node.next;
	}
	return dummy.next;
};

export function Solve(inputJsonElement: string): any {
	const inputValues: string[] = inputJsonElement.split("\n");
	const list1: ListNode | null = IntArrayToLinkedList(JSON.parse(inputValues[0]));
	const list2: ListNode | null = IntArrayToLinkedList(JSON.parse(inputValues[1]));
	return LinkedListToIntArray(mergeTwoLists(list1, list2));
}
