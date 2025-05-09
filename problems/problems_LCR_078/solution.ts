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

function mergeKLists(lists: Array<ListNode | null>): ListNode | null {

};

export function Solve(inputJsonElement: string): any {
	const inputValues: string[] = inputJsonElement.split("\n");
	const jsonArray0: any = JSON.parse(inputValues[0]);
	const lists: Array<ListNode | null> = [];
	for (let i = 0; i < jsonArray0.length; i++) {
		lists.push(IntArrayToLinkedList(jsonArray0[i]));
	}
	return LinkedListToIntArray(mergeKLists(lists));
}
