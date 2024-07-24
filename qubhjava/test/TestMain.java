package qubhjava.test;


import io.github.cdimascio.dotenv.Dotenv;
import io.github.cdimascio.dotenv.DotenvException;
import org.junit.jupiter.api.DynamicTest;
import org.junit.jupiter.api.TestFactory;
import org.junit.jupiter.api.Timeout;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import problems.problems_2844.Solution;
// import premiums.premiums_1056.Solution;
import org.testng.util.Strings;
import qubhjava.Testcase;

import java.io.IOException;
import java.util.ArrayList;
import java.util.Collection;
import java.util.List;

@Timeout(10)
public class TestMain {

    private static final Logger log = LoggerFactory.getLogger(TestMain.class);
    private static final String PROBLEM_ID = "2844";

    private Testcase[] loadTestcases() throws IOException {
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
        return Common.loadTestcases(log, PROBLEM_ID, problemFolder);
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
            tests.add(Common.addTest(solution, testcase, PROBLEM_ID, idx++));
        }
        return tests;
    }
}

