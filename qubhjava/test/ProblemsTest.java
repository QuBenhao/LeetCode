package qubhjava.test;


import org.junit.jupiter.api.DynamicTest;
import org.junit.jupiter.api.TestFactory;
import org.junit.jupiter.api.Timeout;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import qubhjava.BaseSolution;
import problems.problems_49.Solution;
import qubhjava.Testcase;

import java.io.IOException;
import java.lang.reflect.InvocationTargetException;
import java.util.ArrayList;
import java.util.Collection;
import java.util.List;


@Timeout(10)
public class ProblemsTest {

    private static final Logger log = LoggerFactory.getLogger(ProblemsTest.class);
	private static final String[][] PROBLEMS = {{"49", "problems"}};

    @TestFactory
    @SuppressWarnings("unchecked")
    Collection<DynamicTest> test() throws IOException, ClassNotFoundException, InstantiationException,
            IllegalAccessException, NoSuchMethodException, InvocationTargetException {
        List<DynamicTest> tests = new ArrayList<>();
        for (String[] problems : PROBLEMS) {
            log.info("Starting TestMain, test problem: {}", problems[0]);
            Testcase[] testcases = Common.loadTestcases(log, problems[0], problems[1]);
            if (testcases == null || testcases.length == 0) {
                log.error("Load Testcases error");
                return tests;
            }
            Class<BaseSolution> dynamicClass = (Class<BaseSolution>)
                    Class.forName(String.format("%s.%s_%s.Solution", problems[1], problems[1], problems[0]));
            BaseSolution baseSolution = dynamicClass.getDeclaredConstructor().newInstance();
            int idx = 0;
            for (Testcase testcase : testcases) {
                tests.add(Common.addTest(baseSolution, testcase, problems[0], idx++));
            }
        }
        return tests;
    }
}


