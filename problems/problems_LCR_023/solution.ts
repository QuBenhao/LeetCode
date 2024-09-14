import {ListNode,IntArrayToIntersectionLinkedList,LinkedListToIntArray} from "../../typescript/models/listnode";

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

function getIntersectionNode(headA: ListNode | null, headB: ListNode | null): ListNode | null {
	let pa: ListNode | null = headA, pb: ListNode | null = headB;
	while (pa != pb) {
		pa = pa != null ? pa.next : headB;
		pb = pb != null ? pb.next : headA;
	}
	return pa;
};

export function Solve(inputJsonElement: string): any {
	const inputValues: string[] = inputJsonElement.split("\n");
	const iv: number = JSON.parse(inputValues[0]);
	const inputArray1: number[] = JSON.parse(inputValues[1]);
	const inputArray2: number[] = JSON.parse(inputValues[2]);
	const skipA: number = JSON.parse(inputValues[3]);
	const skipB: number = JSON.parse(inputValues[4]);
	const [headA, headB] = IntArrayToIntersectionLinkedList(iv, inputArray1, inputArray2, skipA, skipB);
	return LinkedListToIntArray(getIntersectionNode(headA, headB));
}
