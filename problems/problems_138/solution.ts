import {JSONArrayToNodeRandom,NodeRandom as _Node,NodeRandomToJSONArray} from "../../typescript/models/node.random";

/**
 * Definition for _Node.
 * class _Node {
 *     val: number
 *     next: _Node | null
 *     random: _Node | null
 * 
 *     constructor(val?: number, next?: _Node, random?: _Node) {
 *         this.val = (val===undefined ? 0 : val)
 *         this.next = (next===undefined ? null : next)
 *         this.random = (random===undefined ? null : random)
 *     }
 * }
 */


function copyRandomList(head: _Node | null): _Node | null {
	if (head === null) {
		return null;
	}
	let current: _Node | null = head;
	while (current !== null) {
		const copy: _Node = new _Node(current.val, null, null);
		copy.next = current.next;
		current.next = copy;
		current = copy.next;
	}
	current = head;
	while (current !== null) {
		if (current.random !== null) {
			current.next!.random = current.random.next;
		}
		current = current.next!.next;
	}
	current = head;
	const newHead: _Node = head.next;
	while (current !== null) {
		const copied = current.next;
		current.next = copied!.next;
		copied.next = current.next !== null ? current.next.next : null;
		current = current.next;
	}
	return newHead;
};

export function Solve(inputJsonElement: string): any {
	const inputValues: string[] = inputJsonElement.split("\n");
	const head: _Node | null = JSONArrayToNodeRandom(JSON.parse(inputValues[0]));
	return NodeRandomToJSONArray(copyRandomList(head));
}
