function accountsMerge(accounts: string[][]): string[][] {
    let emailToIndex = new Map();
    let emailToName = new Map();
    let count = 0;
    for (const account of accounts) {
        for (let j = 1; j < account.length; j++) {
            if (!emailToIndex.has(account[j])) {
                emailToIndex.set(account[j], count++);
                emailToName.set(account[j], account[0])
            }
        }
    }
    const uf = new UnionFind(count);
    for (const account of accounts) {
        const firstIndex = emailToIndex.get(account[1]);
        for (let i = 2; i < account.length; i++) {
            const nextIndex = emailToIndex.get(account[i]);
            uf.union(firstIndex, nextIndex);
        }
    }
    let indexToEmails = new Map();
	for(const email of emailToIndex.keys()) {
        const index = uf.find(emailToIndex.get(email));
        const account = indexToEmails.get(index) || [];
        account.push(email);
        indexToEmails.set(index, account);
    }
    let result = [];
	for(const emails of indexToEmails.values()) {
        emails.sort();
        const name = emailToName.get(emails[0]);
        result.push([name, ...emails]);
    }
    return result;
};

class UnionFind {
    parent: any;
    constructor(n: number) {
        this.parent = new Array(n).fill(0).map((value, index) => index);
    }

    union(index1: number, index2: number) {
        this.parent[this.find(index2)] = this.find(index1);
    }

    find(index: number) {
        if (this.parent[index] !== index) {
            this.parent[index] = this.find(this.parent[index]);
        }
        return this.parent[index];
    }
}

export function Solve(inputJsonElement: string): any {
	const inputValues: string[] = inputJsonElement.split("\n");
	const accounts: string[][] = JSON.parse(inputValues[0]);
	return accountsMerge(accounts);
}
