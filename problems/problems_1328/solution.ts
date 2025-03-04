function breakPalindrome(palindrome: string): string {
    
};

export function Solve(inputJsonElement: string): any {
	const inputValues: string[] = inputJsonElement.split("\n");
	const palindrome: string = JSON.parse(inputValues[0]);
	return breakPalindrome(palindrome);
}
