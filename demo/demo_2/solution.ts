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

function addTwoNumbers(l1: ListNode | null, l2: ListNode | null): ListNode | null {
    
};

export function Solve(inputJsonElement: string): any {
	const splits: string[] = inputJsonElement.split("\n");
	const l1: ListNode | null = IntArrayToLinkedList(JSON.parse(splits[0]));
	const l2: ListNode | null = IntArrayToLinkedList(JSON.parse(splits[1]));
	return LinkedListToIntArray(addTwoNumbers(l1, l2));
}
