class TextEditor {
    constructor() {
        
    }

    addText(text: string): void {
        
    }

    deleteText(k: number): number {
        
    }

    cursorLeft(k: number): string {
        
    }

    cursorRight(k: number): string {
        
    }
}

/**
 * Your TextEditor object will be instantiated and called as such:
 * var obj = new TextEditor()
 * obj.addText(text)
 * var param_2 = obj.deleteText(k)
 * var param_3 = obj.cursorLeft(k)
 * var param_4 = obj.cursorRight(k)
 */

export function Solve(inputJsonElement: string): any {
	const inputValues: string[] = inputJsonElement.split("\n");
	const operators: string[] = JSON.parse(inputValues[0]);
	const opValues: any[][] = JSON.parse(inputValues[1]);
	const ans: any[] = [null];
	const obj: TextEditor = new TextEditor();
	for (let i: number = 1; i < operators.length; i++) {
		if (operators[i] == "addText") {
			obj.addText(opValues[i][0]);
			ans.push(null);
			continue;
		}
		if (operators[i] == "deleteText") {
			ans.push(obj.deleteText(opValues[i][0]));
			continue;
		}
		if (operators[i] == "cursorLeft") {
			ans.push(obj.cursorLeft(opValues[i][0]));
			continue;
		}
		if (operators[i] == "cursorRight") {
			ans.push(obj.cursorRight(opValues[i][0]));
			continue;
		}
		ans.push(null);
	}
	return ans;
}
