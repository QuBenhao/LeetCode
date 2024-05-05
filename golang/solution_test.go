package golang

import (
	"encoding/json"
	"fmt"
	"github.com/stretchr/testify/assert"
	problem "leetCode/problems/741"
	"log"
	"os"
	"path"
	"reflect"
	"runtime"
	"strings"
	"testing"
)

const TestcaseFolderFmt = "problems/%s/testcase"

var problemId string = "741"

type TestCase struct {
	input string
	want  interface{}
}

func processTestcase() (tests []TestCase) {
	inputs := make([]string, 0)
	outputs := make([]interface{}, 0)
	_, b, _, _ := runtime.Caller(0)
	basePath := path.Dir(path.Dir(b))
	testcasePath := path.Join(basePath, fmt.Sprintf(TestcaseFolderFmt, problemId))
	testcaseContent, readErr := os.ReadFile(testcasePath)
	if readErr != nil {
		log.Fatal(readErr)
	}
	testcasesStr := string(testcaseContent)
	testcasesSplit := strings.Split(testcasesStr, "\n")
	inputErr := json.Unmarshal([]byte(testcasesSplit[0]), &inputs)
	if inputErr != nil {
		log.Fatal(inputErr)
	}
	outputErr := json.Unmarshal([]byte(testcasesSplit[1]), &outputs)
	if outputErr != nil {
		log.Fatal(outputErr)
	}
	for i, input := range inputs {
		tests = append(tests, TestCase{input, outputs[i]})
	}
	return
}

func TestSolution(t *testing.T) {
	ast := assert.New(t)
	tests := processTestcase()
	for i, testcase := range tests {
		t.Run(fmt.Sprintf("%s/Testcase#%d", problemId, i), func(t *testing.T) {
			gotResp := problem.Solve(testcase.input)
			v := reflect.ValueOf(testcase.want)
			if v.Kind() == reflect.Slice {
				// TODO: Not able to compare type currently
				if !ast.Equal(fmt.Sprintf("%v", testcase.want), fmt.Sprintf("%v", gotResp)) {
					t.Errorf("[%s] Solution want %v, got %v", problemId, testcase.want, gotResp)
				}
			} else {
				// TODO: Not able to compare type currently
				if !ast.Equal(fmt.Sprintf("%#v", testcase.want), fmt.Sprintf("%#v", gotResp)) {
					t.Errorf("[%s] Solution want %v, got %v", problemId, testcase.want, gotResp)
				}
			}
		})
	}
}
