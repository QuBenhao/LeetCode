package qubhjava.test;


import java.io.FileInputStream;
import java.io.IOException;
import java.lang.reflect.InvocationTargetException;
import java.util.ArrayList;
import java.util.Collection;
import java.util.List;

import org.junit.jupiter.api.DynamicTest;
import org.junit.jupiter.api.TestFactory;
import org.junit.jupiter.api.Timeout;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.testng.util.Strings;

import com.alibaba.fastjson.JSONArray;
import com.alibaba.fastjson.JSONException;
import com.alibaba.fastjson.JSONObject;

import io.github.cdimascio.dotenv.Dotenv;
import io.github.cdimascio.dotenv.DotenvException;
import qubhjava.BaseSolution;
import qubhjava.Testcase;

@Timeout(10)
public class ProblemsTest {

    private static final Logger log = LoggerFactory.getLogger(ProblemsTest.class);
	private static String[][] PROBLEMS;

    static {
        List<String> problemsList = new ArrayList<>();
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
        try {
            // read json daily-{problemFolder}.json
            FileInputStream fis = new FileInputStream(String.format("daily-%s.json", problemFolder));
            byte[] bytes = fis.readAllBytes();
            String content = new String(bytes);
            JSONObject jsonObject = JSONObject.parseObject(content);
            JSONArray problemsArray = jsonObject.getJSONArray("plans");
            PROBLEMS = new String[problemsArray.size()/2][2];
            for (int i = 0; i < problemsArray.size(); i+=2) {
                PROBLEMS[i/2][0] = problemsArray.getString(i);
                PROBLEMS[i/2][1] = problemsArray.getString(i + 1);
                log.info("Loaded problem {} in folder {}", problemsArray.getString(i), problemsArray.getString(i + 1));
            }
            log.info("Loaded {} problems for plans", problemsArray.size()/2);
        } catch (IOException e) {
            log.error("Error reading daily-{problemFolder}.json", e);
        } catch (JSONException e) {
            log.error("Error parsing JSON from daily-{problemFolder}.json", e);
        }
    }

    @TestFactory
    @SuppressWarnings("unchecked")
    Collection<DynamicTest> test() throws IOException, ClassNotFoundException, InstantiationException,
            IllegalAccessException, NoSuchMethodException, InvocationTargetException {
        List<DynamicTest> tests = new ArrayList<>();
        int testcaseIdx = 1;
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
                log.info("Add [{}] Testcase {}", problems[0], testcaseIdx++);
                tests.add(Common.addTest(baseSolution, testcase, problems[0], idx++));
            }
        }
        return tests;
    }
}


