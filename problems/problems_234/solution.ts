import {IntArrayToLinkedList,ListNode} from "../../typescript/models/listnode";

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

function isPalindrome(head: ListNode | null): boolean {
    const vals: number[] = [];
	while (head != null) {
		vals.push(head.val);
		head = head.next;
	}
	for (let left: number = 0, right: number = vals.length - 1; left < right; left++, right--) {
		if (vals[left] != vals[right]) return false;
	}
	return true;
};

export function Solve(inputJsonElement: string): any {
	const splits: string[] = inputJsonElement.split("\n");
	const head: ListNode | null = IntArrayToLinkedList(JSON.parse(splits[0]));
	return isPalindrome(head);
}
