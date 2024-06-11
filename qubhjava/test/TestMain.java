package qubhjava.test;


import com.alibaba.fastjson.JSON;
import com.alibaba.fastjson.JSONArray;
import org.junit.jupiter.api.DynamicTest;
import org.junit.jupiter.api.TestFactory;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import problems.problems_2806.Solution;
import qubhjava.Testcase;

import java.io.File;
import java.io.FileInputStream;
import java.io.IOException;
import java.nio.charset.StandardCharsets;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collection;
import java.util.List;

import static org.testng.Assert.assertEquals;

public class TestMain {

    private static final Logger log = LoggerFactory.getLogger(TestMain.class);
    private static final String PROBLEM_ID = "2806";

    private Testcase[] loadTestcases() throws IOException {
        Testcase[] testcases = null;
        FileInputStream fis = null;
        try {
            File file = new File("problems/problems_" + PROBLEM_ID + "/testcase");
            fis = new FileInputStream(file);
            byte[] bytes = fis.readAllBytes();
            // convert to String and split lines
            String content = new String(bytes, StandardCharsets.UTF_8);
            log.info("Loading Testcases for problem {}", PROBLEM_ID);
            String[] splits = content.split("\n");
            JSONArray inputArray = JSON.parseArray(splits[0]);
            JSONArray outputArray = JSON.parseArray(splits[1]);
            testcases = new Testcase[inputArray.size()];
            for (int i = 0; i < inputArray.size(); i++) {
                String[] inputSplits = inputArray.getString(i).split("\n");
                testcases[i] = new Testcase(inputSplits, outputArray.get(i));
                log.info("Added {}", testcases[i]);
            }
        } catch (Exception exception) {
            log.error(exception.getMessage(), exception);
        } finally {
            if (fis != null) {
                fis.close();
            }
        }
        return testcases;
    }


    @TestFactory
    Collection<DynamicTest> test() throws IOException {
        log.info("Starting TestMain, test problem: {}", PROBLEM_ID);
        List<DynamicTest> tests = new ArrayList<>();
        Testcase[] testcases = loadTestcases();
        if (testcases == null || testcases.length == 0) {
            log.error("Load Testcases error");
            return tests;
        }
        Solution solution = new Solution();
        int idx = 0;
        for (Testcase testcase : testcases) {
            tests.add(DynamicTest.dynamicTest(
                    String.format("[Problem%s]Testcase%d: %s", PROBLEM_ID, idx++, Arrays.toString(testcase.getInput())),
                    () -> {
                        Object actual = solution.solve(testcase.getInput());
                        assertEquals(actual, testcase.getOutput());
                    }
            ));
        }
        return tests;
    }
}
