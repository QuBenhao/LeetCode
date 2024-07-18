import {ListNode, IntArrayToLinkedListWithCycle} from "../../typescript/models/listnode";

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

function detectCycle(head: ListNode | null): ListNode | null {
    if (head == null) {
        return null;
    }
    let slow: ListNode | null = head, fast: ListNode | null = head;
    while (true) {
        if (fast == null || fast.next == null) {
            return null;
        }
        slow = slow?.next;
        fast = fast.next.next;
        if (slow == fast) {
            break;
        }
    }
    slow = head;
    while (slow != fast) {
        slow = slow?.next;
        fast = fast?.next;
    }
    return slow;
};

export function Solve(inputJsonElement: string): any {
    const inputValues: string[] = inputJsonElement.split("\n");
    const array: number[] = JSON.parse(inputValues[0]);
    const pos: number = JSON.parse(inputValues[1]);
    const head: ListNode | null = IntArrayToLinkedListWithCycle(array, pos);
    const result: ListNode | null = detectCycle(head);
    return result == null ? null : result.val;
}
