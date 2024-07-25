import * as ts from "typescript";

var _ = require('lodash-contrib');
import {
    IntArrayToIntersectionLinkedList,
    IntArrayToLinkedList,
    IntArrayToLinkedListWithCycle,
    LinkedListToIntArray,
    ListNode
} from "./models/listnode";
import {JSONArrayToTreeNode, JSONArrayToTreeNodeArray, TreeNode, TreeNodeToJSONArray} from "./models/treenode";
import {Queue} from "@datastructures-js/queue";
import {MaxPriorityQueue, MinPriorityQueue, PriorityQueue} from "@datastructures-js/priority-queue";

const vm = require('node:vm');

// @ts-ignore
export function CompareResults(script: vm.Script, inputJson: any, outputJson: any) {
    const context = {
        testInputJsonString: inputJson, execResult: null as any,
        ListNode,
        IntArrayToLinkedList,
        LinkedListToIntArray,
        IntArrayToLinkedListWithCycle,
        IntArrayToIntersectionLinkedList,
        TreeNode,
        TreeNodeToJSONArray,
        JSONArrayToTreeNode,
        JSONArrayToTreeNodeArray,
        Queue,
        PriorityQueue,
        MinPriorityQueue,
        MaxPriorityQueue,
    };
    vm.createContext(context); // Contextify the object.
    script.runInContext(context, {timeout: 3000});
    const result: any = context.execResult;
    try {
        if (_.isFloat(outputJson)) {
            expect(result).toBeCloseTo(outputJson);
        } else if (_.isArray(result) && !_.isArray(outputJson)) {
            expect(result[0]).toEqual(outputJson);
        } else {
            expect(result).toEqual(outputJson);
        }
    } catch (Failed) {
        script.runInContext(context, {timeout: 3000});
        let iterResult: any = context.execResult;
        if (_.isEqual(result, iterResult)) {
            throw Failed;
        }
        for (let j: number = 0; j < 10000; j++) {
            try {
                if (_.isFloat(outputJson)) {
                    expect(iterResult).toBeCloseTo(outputJson);
                } else if (_.isArray(iterResult) && !_.isArray(outputJson)) {
                    expect(iterResult[0]).toEqual(outputJson);
                } else {
                    expect(iterResult).toEqual(outputJson);
                }
                return;
            } catch (FailedIter) {
                if (j === 9999) {
                    throw FailedIter;
                }
            }
            script.runInContext(context, {timeout: 3000});
            iterResult = context.execResult;
        }
    }
}