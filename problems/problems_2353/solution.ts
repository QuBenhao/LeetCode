class FoodRatings {
    constructor(foods: string[], cuisines: string[], ratings: number[]) {
        
    }

    changeRating(food: string, newRating: number): void {
        
    }

    highestRated(cuisine: string): string {
        
    }
}

/**
 * Your FoodRatings object will be instantiated and called as such:
 * var obj = new FoodRatings(foods, cuisines, ratings)
 * obj.changeRating(food,newRating)
 * var param_2 = obj.highestRated(cuisine)
 */

export function Solve(inputJsonElement: string): any {
	const inputValues: string[] = inputJsonElement.split("\n");
	const operators: string[] = JSON.parse(inputValues[0]);
	const opValues: any[][] = JSON.parse(inputValues[1]);
	const ans: any[] = [null];
	const obj: FoodRatings = new FoodRatings(opValues[0][0], opValues[0][1], opValues[0][2]);
	for (let i: number = 1; i < operators.length; i++) {
		if (operators[i] == "changeRating") {
			obj.changeRating(opValues[i][0], opValues[i][1]);
			ans.push(null);
			continue;
		}
		if (operators[i] == "highestRated") {
			ans.push(obj.highestRated(opValues[i][0]));
			continue;
		}
		ans.push(null);
	}
	return ans;
}
