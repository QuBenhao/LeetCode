package qubhjava.test;


import io.github.cdimascio.dotenv.Dotenv;
import io.github.cdimascio.dotenv.DotenvException;
import org.junit.jupiter.api.DynamicTest;
import org.junit.jupiter.api.TestFactory;
import org.junit.jupiter.api.Timeout;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.testng.util.Strings;
import qubhjava.Testcase;

import java.io.IOException;
import java.util.ArrayList;
import java.util.Collection;
import java.util.List;
import com.alibaba.fastjson.JSONException;
import com.alibaba.fastjson.JSONObject;
import qubhjava.BaseSolution;
import java.io.FileInputStream;
import java.lang.reflect.InvocationTargetException;
import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.Paths;


@Timeout(10)
public class TestMain {

    private static final Logger log = LoggerFactory.getLogger(TestMain.class);
    private static final String PROBLEM_ID, PROBLEM_FOLDER;
    private static final String RESOLVED_PROBLEM_ID;  // Problem ID after resolving link

    static {
        String problemId = null;
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
        PROBLEM_FOLDER = problemFolder;
        try {
            // read json daily-{problemFolder}.json
            FileInputStream fis = new FileInputStream(String.format("daily-%s.json", problemFolder));
            byte[] bytes = fis.readAllBytes();
            String content = new String(bytes);
            JSONObject jsonObject = JSONObject.parseObject(content);
            problemId = jsonObject.getString("daily");
        } catch (IOException e) {
            log.error("Error reading daily-{problemFolder}.json", e);
        } catch (JSONException e) {
            log.error("Error parsing JSON from daily-{problemFolder}.json", e);
        }
        if (Strings.isNullOrEmpty(problemId)) {
            throw new RuntimeException("Problem ID is not set in daily-{problemFolder}.json");
        }
        PROBLEM_ID = problemId;

        // Resolve link if exists (with cycle detection)
        String resolvedProblemId = problemId;
        String resolvedFolder = problemFolder;
        java.util.Set<String> visited = new java.util.HashSet<>();
        visited.add(problemId);

        while (true) {
            try {
                Path linkPath = Paths.get(resolvedFolder, String.format("%s_%s", resolvedFolder, resolvedProblemId), "link.json");
                if (!Files.exists(linkPath)) {
                    break;
                }
                String linkContent = new String(Files.readAllBytes(linkPath));
                JSONObject linkJson = JSONObject.parseObject(linkContent);
                String linkTo = linkJson.getString("link_to");
                String linkFolder = linkJson.containsKey("link_folder") ? linkJson.getString("link_folder") : resolvedFolder;
                String reason = linkJson.getString("reason");

                if (visited.contains(linkTo)) {
                    log.error("Circular link detected involving problem {}", linkTo);
                    break;
                }
                visited.add(linkTo);

                log.info("Problem {} is linked to {}: {}", resolvedProblemId, linkTo, reason != null ? reason : "No reason provided");
                resolvedProblemId = linkTo;
                resolvedFolder = linkFolder;
            } catch (IOException e) {
                log.error("Error reading link.json", e);
                break;
            }
        }
        RESOLVED_PROBLEM_ID = resolvedProblemId;

        log.info("Problem ID: {}, Problem Folder: {}, Resolved Problem ID: {}", PROBLEM_ID, PROBLEM_FOLDER, RESOLVED_PROBLEM_ID);
    }

    @TestFactory
    Collection<DynamicTest> test() throws IOException, ClassNotFoundException, InstantiationException,
            IllegalAccessException, NoSuchMethodException, InvocationTargetException {
        log.info("Starting TestMain, test problem: {}", PROBLEM_ID);
        List<DynamicTest> tests = new ArrayList<>();
        Testcase[] testcases = Common.loadTestcases(log, PROBLEM_ID, PROBLEM_FOLDER);
        if (testcases == null || testcases.length == 0) {
            log.error("Load Testcases error");
            return tests;
        }
        Class<BaseSolution> dynamicClass = (Class<BaseSolution>)Class.forName(String.format("%s.%s_%s.Solution", PROBLEM_FOLDER, PROBLEM_FOLDER, RESOLVED_PROBLEM_ID));
        BaseSolution baseSolution = dynamicClass.getDeclaredConstructor().newInstance();
        int idx = 0;
        for (Testcase testcase : testcases) {
            tests.add(Common.addTest(baseSolution, testcase, PROBLEM_ID, idx++));
        }
        return tests;
    }
}

