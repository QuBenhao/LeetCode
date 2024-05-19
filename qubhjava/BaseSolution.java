package qubhjava;

import com.alibaba.fastjson.JSON;
import com.alibaba.fastjson.JSONArray;


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
}
