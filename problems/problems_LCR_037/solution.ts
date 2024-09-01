function asteroidCollision(asteroids: number[]): number[] {
    const stack: number[] = [];
    for (const asteroid of asteroids) {
        let flag: boolean = true;
        while (stack.length > 0 && stack[stack.length - 1] > 0 && asteroid < 0) {
            const prev: number = stack.pop();
            if (-asteroid > prev) {
                continue;
            }
            if (-asteroid === prev) {
                flag = false;
                break;
            }
            stack.push(prev);
            flag = false;
            break;
        }
        if (flag) {
            stack.push(asteroid);
        }
    }
    return stack;
}

export function Solve(inputJsonElement: string): any {
    const inputValues: string[] = inputJsonElement.split("\n");
    const asteroids: number[] = JSON.parse(inputValues[0]);
    return asteroidCollision(asteroids);
}
