/**
 * Definition for node.
 * class Node {
 *     val: number
 *     prev: Node | null
 *     next: Node | null
 *     child: Node | null
 *     constructor(val?: number, prev? : Node, next? : Node, child? : Node) {
 *         this.val = (val===undefined ? 0 : val);
 *         this.prev = (prev===undefined ? null : prev);
 *         this.next = (next===undefined ? null : next);
 *         this.child = (child===undefined ? null : child);
 *     }
 * }
 */

function flatten(head: Node | null): Node | null {

};

export function Solve(inputJsonElement: string): any {
	const inputValues: string[] = inputJsonElement.split("\n");
	const head: Node | null = JSON.parse(inputValues[0]);
	return flatten(head);
}
