package qubhjava;

import java.util.ArrayList;
import java.util.List;

import com.alibaba.fastjson.JSON;
import com.alibaba.fastjson.JSONArray;

import qubhjava.models.ListNode;
import qubhjava.models.TreeNode;


public abstract class BaseSolution {

    public abstract Object solve(String[] values);

    protected int[] jsonArrayToIntArray(String jsonString) {
        JSONArray jsonArray = JSON.parseArray(jsonString);
        int[] result = new int[jsonArray.size()];
        for (int i = 0; i < jsonArray.size(); i++) {
            result[i] = Integer.parseInt(jsonArray.getString(i));
        }
        return result;
    }

    protected int[][] jsonArrayToInt2DArray(String jsonString) {
        JSONArray jsonArray = JSON.parseArray(jsonString);
        int[][] result = new int[jsonArray.size()][];
        for (int i = 0; i < jsonArray.size(); i++) {
            JSONArray innerArray = jsonArray.getJSONArray(i);
            result[i] = new int[innerArray.size()];
            for (int j = 0; j < innerArray.size(); j++) {
                result[i][j] = Integer.parseInt(innerArray.getString(j));
            }
        }
        return result;
    }

    protected String[] jsonArrayToStringArray(String jsonString) {
        JSONArray jsonArray = JSON.parseArray(jsonString);
        String[] result = new String[jsonArray.size()];
        for (int i = 0; i < jsonArray.size(); i++) {
            result[i] = jsonArray.getString(i);
        }
        return result;
    }

    protected String[][] jsonArrayToString2DArray(String jsonString) {
        JSONArray jsonArray = JSON.parseArray(jsonString);
        String[][] result = new String[jsonArray.size()][];
        for (int i = 0; i < jsonArray.size(); i++) {
            JSONArray innerArray = jsonArray.getJSONArray(i);
            result[i] = new String[innerArray.size()];
            for (int j = 0; j < innerArray.size(); j++) {
                result[i][j] = innerArray.getString(j);
            }
        }
        return result;
    }

    protected List<Integer> jsonArrayToIntList(String jsonString) {
        JSONArray jsonArray = JSON.parseArray(jsonString);
        List<Integer> result = new ArrayList<>(jsonArray.size());
        for (int i = 0; i < jsonArray.size(); i++) {
            result.add(Integer.parseInt(jsonArray.getString(i)));
        }
        return result;
    }

    protected List<List<Integer>> jsonArrayTo2DIntList(String jsonString) {
        JSONArray jsonArray = JSON.parseArray(jsonString);
        List<List<Integer>> result = new ArrayList<>(jsonArray.size());
        for (int i = 0; i < jsonArray.size(); i++) {
            JSONArray innerArray = jsonArray.getJSONArray(i);
            result.add(new ArrayList<>(innerArray.size()));
            for (int j = 0; j < innerArray.size(); j++) {
                result.get(i).add(Integer.parseInt(innerArray.getString(j)));
            }
        }
        return result;
    }

    protected ListNode jsonArrayToListNode(String jsonString) {
        int[] arr = jsonArrayToIntArray(jsonString);
        return ListNode.IntArrayToLinkedList(arr);
    }

    protected ListNode[] jsonArrayToListNodeArray(String jsonString) {
        JSONArray jsonArray = JSON.parseArray(jsonString);
        ListNode[] result = new ListNode[jsonArray.size()];
        for (int i = 0; i < jsonArray.size(); i++) {
            result[i] = jsonArrayToListNode(jsonArray.getString(i));
        }
        return result;
    }

    protected char[] jsonArrayToCharArray(String jsonString) {
        JSONArray jsonArray = JSON.parseArray(jsonString);
        char[] result = new char[jsonArray.size()];
        for (int i = 0; i < jsonArray.size(); i++) {
            result[i] = jsonArray.getString(i).charAt(0);
        }
        return result;
    }

    protected char[][] jsonArrayToChar2DArray(String jsonString) {
        JSONArray jsonArray = JSON.parseArray(jsonString);
        char[][] result = new char[jsonArray.size()][];
        for (int i = 0; i < jsonArray.size(); i++) {
            JSONArray innerArray = jsonArray.getJSONArray(i);
            result[i] = new char[innerArray.size()];
            for (int j = 0; j < innerArray.size(); j++) {
                result[i][j] = innerArray.getString(j).charAt(0);
            }
        }
        return result;
    }

    protected List<String> jsonArrayToStringList(String jsonString) {
        JSONArray jsonArray = JSON.parseArray(jsonString);
        List<String> result = new ArrayList<>(jsonArray.size());
        for (int i = 0; i < jsonArray.size(); i++) {
            result.add(jsonArray.getString(i));
        }
        return result;
    }

    protected List<List<String>> jsonArrayToString2DList(String jsonString) {
        JSONArray jsonArray = JSON.parseArray(jsonString);
        List<List<String>> result = new ArrayList<>(jsonArray.size());
        for (int i = 0; i < jsonArray.size(); i++) {
            result.add(jsonArrayToStringList(jsonArray.getString(i)));
        }
        return result;
    }

    protected String jsonStringToString(String jsonString) {
        return jsonString.replaceAll("\"", "");
    }

    protected TreeNode[] jsonArrayToTreeNodeArray(String jsonString) {
        JSONArray jsonArray = JSON.parseArray(jsonString);
        TreeNode[] result = new TreeNode[jsonArray.size()];
        for (int i = 0; i < jsonArray.size(); i++) {
            result[i] = TreeNode.ArrayToTreeNode(jsonArray.getString(i));
        }
        return result;
    }

    protected List<TreeNode> jsonArrayToTreeNodeList(String jsonString) {
        JSONArray jsonArray = JSON.parseArray(jsonString);
        List<TreeNode> result = new ArrayList<>(jsonArray.size());
        for (int i = 0; i < jsonArray.size(); i++) {
            result.add(TreeNode.ArrayToTreeNode(jsonArray.getString(i)));
        }
        return result;
    }

}
