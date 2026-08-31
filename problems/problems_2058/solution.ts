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

function nodesBetweenCriticalPoints(head: ListNode | null): number[] {
    // 最小距离来自相邻临界点，最大距离来自首尾临界点
    let first = 0, prev = 0, mn = Number.MAX_SAFE_INTEGER;
    let a = head!, b = head!.next!, c = head!.next!.next;
    for (let i = 2; c; ++i) {
        if (b.val > a.val && b.val > c.val || b.val < a.val && b.val < c.val) {
            if (prev) mn = Math.min(mn, i - prev);
            else first = i;
            prev = i;
        }
        a = b; b = c; c = c.next;
    }
    return mn === Number.MAX_SAFE_INTEGER ? [-1, -1] : [mn, prev - first];
};

export function Solve(inputJsonElement: string): any {
	const inputValues: string[] = inputJsonElement.split("\n");
	const head: ListNode | null = IntArrayToLinkedList(JSON.parse(inputValues[0]));
	return nodesBetweenCriticalPoints(head);
}
