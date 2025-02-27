use serde_json::{json, Value};


struct FoodRatings {

}


/** 
 * `&self` means the method takes an immutable reference.
 * If you need a mutable reference, change it to `&mut self` instead.
 */
impl FoodRatings {

    fn new(foods: Vec<String>, cuisines: Vec<String>, ratings: Vec<i32>) -> Self {
        
    }
    
    fn change_rating(&self, food: String, new_rating: i32) {
        
    }
    
    fn highest_rated(&self, cuisine: String) -> String {
        
    }
}

/**
 * Your FoodRatings object will be instantiated and called as such:
 * let obj = FoodRatings::new(foods, cuisines, ratings);
 * obj.change_rating(food, newRating);
 * let ret_2: String = obj.highest_rated(cuisine);
 */

#[cfg(feature = "solution_2353")]
pub fn solve(input_string: String) -> Value {
	let input_values: Vec<String> = input_string.split('\n').map(|x| x.to_string()).collect();
	let operators: Vec<String> = serde_json::from_str(&input_values[0]).expect("Failed to parse input");
	let op_values: Vec<Vec<Value>> = serde_json::from_str(&input_values[1]).expect("Failed to parse input");
	let foods_obj: Vec<String> = serde_json::from_value(op_values[0][0].clone()).expect("Failed to parse input");
	let cuisines_obj: Vec<String> = serde_json::from_value(op_values[0][1].clone()).expect("Failed to parse input");
	let ratings_obj: Vec<i32> = serde_json::from_value(op_values[0][2].clone()).expect("Failed to parse input");
	let mut obj = FoodRatings::new(foods_obj, cuisines_obj, ratings_obj);
	let mut ans = vec![None];
	for i in 1..operators.len() {
		match operators[i].as_str() {
			"changeRating" => {
				let food: String = serde_json::from_value(op_values[i][0].clone()).expect("Failed to parse input");
				let new_rating: i32 = serde_json::from_value(op_values[i][1].clone()).expect("Failed to parse input");
				obj.change_rating(food, new_rating);
				ans.push(None);
			},
			"highestRated" => {
				let cuisine: String = serde_json::from_value(op_values[i][0].clone()).expect("Failed to parse input");
				ans.push(Some(obj.highest_rated(cuisine)));
			},
			_ => ans.push(None),
		}
	}
	json!(ans)
}
