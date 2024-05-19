package qubhjava;

import com.alibaba.fastjson.JSON;

public class Testcase {

    /**
     * JSON input String
     */
    private final String[] input;

    /**
     * JSON output
     */
    private final Object output;

    public Testcase(String[] input, Object output) {
        this.input = input;
        this.output = output;
    }

    public String[] getInput() {
        return input;
    }

    public Object getOutput() {
        return output;
    }

    @Override
    public String toString() {
        return String.format("Testcase input=%s, Output=%s", JSON.toJSONString(input), JSON.toJSONString(output));
    }
}
