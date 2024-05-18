package qubh.leetcode.java;

import com.alibaba.fastjson.JSON;


public class Solution {
    public static void main(String[] args) {
        Object object = JSON.parse("[20,14,21,10]");
        System.out.println(object.getClass().getName());
        System.out.println(JSON.toJSONString(object));
    }
}
