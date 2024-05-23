package qubhjava;

import com.alibaba.fastjson.JSON;
import com.alibaba.fastjson.JSONArray;

import java.util.ArrayList;
import java.util.List;


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
}
