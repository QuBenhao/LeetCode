import {add} from "../add";
import {insert} from "../../problems/problems_57/solution";

describe("TestAdd", () => {
  it("should add two numbers correctly", () => {
    expect(add(1, 2)).toEqual(3);
  });
})

describe("TestMain", () => {
  it("Load Problem 57", () => {
    expect(insert([[1, 3], [6, 9]], [2, 5])).toEqual([[1, 5], [6, 9]]);
  })
})