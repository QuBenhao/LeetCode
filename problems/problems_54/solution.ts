function spiralOrder(matrix: number[][]): number[] {
    const ans: number[] = [];
    const m: number = matrix.length, n: number = matrix[0].length;
    for (let left: number = 0, right: number = n - 1, top: number = 0, bottom: number = m - 1;
         left <= right && top <= bottom; left++, right--, top++, bottom--) {
        for (let i: number = left; i <= right; i++) {
            ans.push(matrix[top][i]);
        }
        for (let i: number = top + 1; i <= bottom; i++) {
            ans.push(matrix[i][right]);
        }
        if (left < right && top < bottom) {
            for (let i: number = right - 1; i >= left; i--) {
                ans.push(matrix[bottom][i]);
            }
            for (let i: number = bottom - 1; i > top; i--) {
                ans.push(matrix[i][left]);
            }
        }
    }
    return ans;
};

export function Solve(inputJsonElement: string): any {
    const inputValues: string[] = inputJsonElement.split("\n");
    const matrix: number[][] = JSON.parse(inputValues[0]);
    return spiralOrder(matrix);
}
