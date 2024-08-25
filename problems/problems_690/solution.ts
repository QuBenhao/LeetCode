/**
 * Definition for Employee.
 * class Employee {
 *     id: number
 *     importance: number
 *     subordinates: number[]
 *     constructor(id: number, importance: number, subordinates: number[]) {
 *         this.id = (id === undefined) ? 0 : id;
 *         this.importance = (importance === undefined) ? 0 : importance;
 *         this.subordinates = (subordinates === undefined) ? [] : subordinates;
 *     }
 * }
 */

function getImportance(employees: Employee[], id: number): number {
	
};

export function Solve(inputJsonElement: string): any {
	const inputValues: string[] = inputJsonElement.split("\n");
	const employees: Employee[] = JSON.parse(inputValues[0]);
	const id: number = JSON.parse(inputValues[1]);
	return getImportance(employees, id);
}
