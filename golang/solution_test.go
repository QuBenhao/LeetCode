package golang

import (
	"encoding/json"
	"fmt"
	"github.com/stretchr/testify/assert"
	problem "leetCode/problems/problems_2903"
	"log"
	"os"
	"path"
	"runtime"
	"strings"
	"testing"
)

const TestcaseFolderFmt = "problems/problems_%s/testcase"

var problemId string = "2903"

type TestCase struct {
	input string
	want  interface{}
}

func processTestcase() (tests []TestCase) {
	inputs := make([]string, 0)
	var outputs interface{}
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
		tests = append(tests, TestCase{input, outputs.([]interface{})[i]})
	}
	return
}

func compareGeneral(ast *assert.Assertions, want interface{}, resp interface{}) {
	switch resp.(type) {
	case int:
		ast.Equal(int(want.(float64)), resp.(int))
	case int64:
		ast.Equal(int64(want.(float64)), resp.(int64))
	case float64:
		ast.InDelta(want, resp, 1e-5)
	case [][]int:
		wantArray := want.([]interface{})
		respIntArray := resp.([][]int)
		if ast.Equalf(len(wantArray), len(respIntArray), "Expected: [%v], actual: [%v]", want, resp) {
			for i := 0; i < len(respIntArray); i++ {
				for j := 0; j < len(respIntArray[i]); j++ {
					ast.Equalf(int(wantArray[i].([]interface{})[j].(float64)), respIntArray[i][j], "Expected: [%v], actual: [%v]", want, resp)
				}
			}
		}
	case []int:
		wantArray := want.([]interface{})
		respIntArray := resp.([]int)
		if ast.Equalf(len(wantArray), len(respIntArray), "Expected: [%v], actual: [%v]", want, resp) {
			for j := 0; j < len(respIntArray); j++ {
				ast.Equalf(int(wantArray[j].(float64)), respIntArray[j], "Expected: [%v], actual: [%v]", want, resp)
			}
		}
	case []string:
		ast.Equal(want.([]string), resp)
	case []interface{}:
		defer func() {
			if recover() != nil {
				ast.ElementsMatch(want, resp)
			}
		}()
		respArray := resp.([]interface{})
		wantArray := want.([]interface{})
		if len(wantArray) == 0 {
			ast.Equal(wantArray, respArray)
		} else {
			if ast.Equalf(len(wantArray), len(respArray), "Expected: [%v], actual: [%v]", want, resp) {
				if respArray[0] != nil {
					switch respArray[0].(type) {
					case float64:
						ast.InDeltaSlicef(wantArray, respArray, 1e-5, "Expected: [%v], actual: [%v]", want, resp)
					default:
						ast.Equal(fmt.Sprintf("%v", want), fmt.Sprintf("%v", resp))
					}
				} else {
					ast.Equal(fmt.Sprintf("%v", want), fmt.Sprintf("%v", resp))
				}
			}
		}
	default:
		ast.Equal(want, resp)
	}
}

func TestSolution(t *testing.T) {
	ast := assert.New(t)
	tests := processTestcase()
	for i, testcase := range tests {
		t.Run(fmt.Sprintf("%s/Testcase#%d", problemId, i), func(t *testing.T) {
			gotResp := problem.Solve(testcase.input)
			compareGeneral(ast, testcase.want, gotResp)
		})
	}
}
