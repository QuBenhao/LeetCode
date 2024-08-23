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
    
};

export function Solve(inputJsonElement: string): any {
	const inputValues: string[] = inputJsonElement.split("\n");
	const head: _Node | null = JSONArrayToNodeRandom(JSON.parse(inputValues[0]));
	return NodeRandomToJSONArray(copyRandomList(head));
}
