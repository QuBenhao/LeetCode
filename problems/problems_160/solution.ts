import {ListNode,IntArrayToLinkedList,LinkedListToIntArray, IntArrayToIntersectionLinkedList} from "../../typescript/models/listnode";

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
		pa = pa == null ? headB : pa.next;
		pb = pb == null ? headA : pb.next;
	}
	return pa;
};

export function Solve(inputJsonElement: string): any {
	const inputValues: string[] = inputJsonElement.split("\n");
	const iv: number = JSON.parse(inputValues[0]);
	const arrA: number[] = JSON.parse(inputValues[1]);
	const arrB: number[] = JSON.parse(inputValues[2]);
	const skipA: number = JSON.parse(inputValues[3]);
	const skipB: number = JSON.parse(inputValues[4]);
	const [headA, headB] = IntArrayToIntersectionLinkedList(arrA, arrB, iv, skipA, skipB);
	const result: ListNode | null = getIntersectionNode(headA, headB);
	return result ? result.val : null;
}
