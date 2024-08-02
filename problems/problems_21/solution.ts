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
    
};

export function Solve(inputJsonElement: string): any {
	const inputValues: string[] = inputJsonElement.split("\n");
	const list1: ListNode | null = IntArrayToLinkedList(JSON.parse(inputValues[0]));
	const list2: ListNode | null = IntArrayToLinkedList(JSON.parse(inputValues[1]));
	return LinkedListToIntArray(mergeTwoLists(list1, list2));
}
