package qubhjava.test;


import com.alibaba.fastjson.JSON;
import com.alibaba.fastjson.JSONArray;
import io.github.cdimascio.dotenv.Dotenv;
import io.github.cdimascio.dotenv.DotenvException;
import org.junit.jupiter.api.DynamicTest;
import org.junit.jupiter.api.TestFactory;
import org.junit.jupiter.api.Timeout;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import problems.problems_2734.Solution;
// import premiums.premiums_1056.Solution;
import org.testng.util.Strings;
import qubhjava.Testcase;

import java.io.File;
import java.io.FileInputStream;
import java.io.IOException;
import java.math.BigDecimal;
import java.nio.charset.StandardCharsets;
import java.time.Duration;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collection;
import java.util.List;

import static org.junit.jupiter.api.Assertions.assertTimeoutPreemptively;
import static org.testng.Assert.assertEquals;

@Timeout(10)
public class TestMain {

    private static final Logger log = LoggerFactory.getLogger(TestMain.class);
    private static final String PROBLEM_ID = "2734";

    private Testcase[] loadTestcases() throws IOException {
        Testcase[] testcases = null;
        FileInputStream fis = null;
        try {
            String problemFolder = null;
            try {
                Dotenv dotenv = Dotenv.load();
                problemFolder = dotenv.get("PROBLEM_FOLDER", "");
            } catch (DotenvException e) {
                log.error("Error load .env file", e);
            }
            if (Strings.isNullOrEmpty(problemFolder)) {
                problemFolder = "problems";
            }
            File file = new File(problemFolder + "/" + problemFolder + "_" + PROBLEM_ID + "/testcase");
            if (!file.exists()) {
                log.info("Problem folder [{}] not found, try premiums...", problemFolder);
                file = new File("premiums/premiums_" + PROBLEM_ID + "/testcase");
            }
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
                    () -> assertTimeoutPreemptively(Duration.ofSeconds(3), () -> {
                        Object actual = solution.solve(testcase.getInput());
                        switch (testcase.getOutput()) {
                            case BigDecimal output -> {
                                BigDecimal actualNumber = (BigDecimal) actual;
                                assertEquals(actualNumber.doubleValue(), output.doubleValue(), 1e-4);
                            }
                            case Double output -> assertEquals((Double) actual, output, 1e-4d);
                            case Float output -> assertEquals((Float) actual, output, 1e-4f);
                            case null, default -> assertEquals(actual, testcase.getOutput());
                        }
                    })
            ));
        }
        return tests;
    }
}
