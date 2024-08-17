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

function reverseKGroup(head: ListNode | null, k: number): ListNode | null {
    
};

export function Solve(inputJsonElement: string): any {
	const inputValues: string[] = inputJsonElement.split("\n");
	const head: ListNode | null = IntArrayToLinkedList(JSON.parse(inputValues[0]));
	const k: number = JSON.parse(inputValues[1]);
	return LinkedListToIntArray(reverseKGroup(head, k));
}
