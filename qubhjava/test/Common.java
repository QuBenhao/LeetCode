package qubhjava.test;

import com.alibaba.fastjson.JSON;
import com.alibaba.fastjson.JSONArray;
import org.junit.jupiter.api.DynamicTest;
import org.slf4j.Logger;
import qubhjava.BaseSolution;
import qubhjava.Testcase;

import java.io.File;
import java.io.FileInputStream;
import java.io.IOException;
import java.math.BigDecimal;
import java.nio.charset.StandardCharsets;
import java.time.Duration;
import java.util.Arrays;
import java.util.List;

import static org.junit.jupiter.api.Assertions.assertTimeoutPreemptively;
import static org.testng.Assert.assertEquals;

public class Common {

    public static Testcase[] loadTestcases(Logger log, String problemId, String problemFolder) throws IOException {
        Testcase[] testcases = null;
        FileInputStream fis = null;
        try {
            File file = new File(problemFolder + "/" + problemFolder + "_" + problemId + "/testcase");
            if (!file.exists()) {
                log.info("Problem folder [{}] not found, try premiums...", problemFolder);
                file = new File("premiums/premiums_" + problemId + "/testcase");
            }
            fis = new FileInputStream(file);
            byte[] bytes = fis.readAllBytes();
            // convert to String and split lines
            String content = new String(bytes, StandardCharsets.UTF_8);
            log.info("Loading Testcases for problem {}", problemId);
            String[] splits = content.split("\n");
            JSONArray inputArray = JSON.parseArray(splits[0]);
            JSONArray outputArray = JSON.parseArray(splits[1]);
            testcases = new Testcase[inputArray.size()];
            for (int i = 0; i < inputArray.size(); i++) {
                String input_string = inputArray.getString(i);
                if (input_string.startsWith("\"") && input_string.endsWith("\"")) {
                    input_string = input_string.substring(1, input_string.length() - 1);
                }
                String[] inputSplits = input_string.split("\n");
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

    public static DynamicTest addTest(BaseSolution solution, Testcase testcase, String problemId, int idx) {
        return DynamicTest.dynamicTest(
                String.format("[Problem%s]Testcase%d: %s", problemId, idx, Arrays.toString(testcase.getInput())),
                () -> assertTimeoutPreemptively(Duration.ofSeconds(3), () -> {
                    Object actual = solution.solve(testcase.getInput());
                    try {
                        compareResult(testcase, actual);
                    } catch (AssertionError ae) {
                        Object iterActual = solution.solve(testcase.getInput());
                        if (iterActual == actual) {
                            throw ae;
                        }
                        for (int i = 0; i < 10000; i++) {
                            try {
                                compareResult(testcase, iterActual);
                                return;
                            } catch (AssertionError assErr) {
                                if (i == 9999) {
                                    throw assErr;
                                }
                            }
                            iterActual = solution.solve(testcase.getInput());
                        }
                    }
                })
        );
    }

    private static void compareResult(Testcase testcase, Object actual) {
        switch (testcase.getOutput()) {
            case BigDecimal output -> {
                BigDecimal actualNumber = (BigDecimal) actual;
                assertEquals(actualNumber.doubleValue(), output.doubleValue(), 1e-4);
            }
            case Double output -> assertEquals((Double) actual, output, 1e-4d);
            case Float output -> assertEquals((Float) actual, output, 1e-4f);
            case null, default -> {
                if (actual instanceof Iterable<?> && !(testcase.getOutput() instanceof Iterable<?>)) {
                    assertEquals(((Iterable<?>)actual).iterator().next(), testcase.getOutput());
                } else {
                    assertEquals(actual, testcase.getOutput());
                }
            }
        }
    }
}
