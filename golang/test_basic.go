package golang

import (
	"encoding/json"
	"fmt"
	"log"
	"os"
	"path"
	"runtime"
	"strings"
	"testing"

	"github.com/stretchr/testify/assert"
)

const TestcaseFolderFmt = "%s/%s_%s/testcase"

type TestCase struct {
	input string
	want  interface{}
}

func processTestcase(problemPath string) (tests []TestCase) {
	inputs := make([]string, 0)
	var outputs interface{}
	_, b, _, _ := runtime.Caller(0)
	basePath := path.Dir(path.Dir(b))
	testcasePath := path.Join(basePath, problemPath)
	testcaseContent, readErr := os.ReadFile(testcasePath)
	if readErr != nil {
		log.Fatal(readErr)
	}
	testcasesStr := string(testcaseContent)
	testcasesSplit := strings.Split(testcasesStr, "\n")
	if inputErr := json.Unmarshal([]byte(testcasesSplit[0]), &inputs); inputErr != nil {
		log.Fatal(inputErr)
	}
	if outputErr := json.Unmarshal([]byte(testcasesSplit[1]), &outputs); outputErr != nil {
		log.Fatal(outputErr)
	}
	for i, input := range inputs {
		tests = append(tests, TestCase{input, outputs.([]interface{})[i]})
	}
	return
}

func compareGeneral(ast *assert.Assertions, want interface{}, resp interface{}) bool {
	switch resp.(type) {
	case int:
		return ast.Equal(int(want.(float64)), resp.(int))
	case int64:
		return ast.Equal(int64(want.(float64)), resp.(int64))
	case float64:
		return ast.InDelta(want, resp, 1e-5)
	case byte:
		return ast.Equalf(want.(string)[0], resp, "Expected: [%s], actual: [%s]", want, string(resp.(byte)))
	case [][]int:
		wantArray := want.([]interface{})
		respIntArray := resp.([][]int)
		if !ast.Equalf(len(wantArray), len(respIntArray), "Expected: [%v], actual: [%v]", want, resp) {
			return false
		}
		for i := 0; i < len(respIntArray); i++ {
			if !ast.Equalf(len(wantArray[i].([]interface{})), len(respIntArray[i]),
				"Expected: [%v], actual: [%v]", want, resp) {
				return false
			}
			for j := 0; j < len(respIntArray[i]); j++ {
				if !ast.Equalf(int(wantArray[i].([]interface{})[j].(float64)), respIntArray[i][j],
					"Expected: [%v], actual: [%v]", want, resp) {
					return false
				}
			}
		}
	case []int:
		wantArray := want.([]interface{})
		respIntArray := resp.([]int)
		if !ast.Equalf(len(wantArray), len(respIntArray), "Expected: [%v], actual: [%v]", want, resp) {
			return false
		}
		for j := 0; j < len(respIntArray); j++ {
			if !ast.Equalf(int(wantArray[j].(float64)), respIntArray[j], "Expected: [%v], actual: [%v]", want, resp) {
				return false
			}
		}
	case []string:
		if v, ok := want.([]string); ok {
			ast.Equal(v, resp)
			return false
		}
		if !ast.Equalf(len(want.([]interface{})), len(resp.([]string)),
			"Expected: [%v], actual: [%v]", want, resp) {
			return false
		}
		for i := 0; i < len(resp.([]string)); i++ {
			if !ast.Equalf(want.([]interface{})[i], resp.([]string)[i],
				"Expected: [%v], actual: [%v]", want, resp) {
				return false
			}
		}
	case [][]string:
		wantArray := want.([]interface{})
		respStrArray := resp.([][]string)
		if !ast.Equalf(len(wantArray), len(respStrArray), "Expected: [%v], actual: [%v]", want, resp) {
			return false
		}

		for i := 0; i < len(respStrArray); i++ {
			if !ast.Equalf(len(wantArray[i].([]interface{})), len(respStrArray[i]),
				"Expected: [%v], actual: [%v]", want, resp) {
				return false
			}
			for j := 0; j < len(respStrArray[i]); j++ {
				if !ast.Equalf(len(wantArray[i].([]interface{})[j].(string)), len(respStrArray[i][j]),
					"Expected: [%v], actual: [%v]", want, resp) {
					return false
				}
				if !ast.Equalf(wantArray[i].([]interface{})[j], respStrArray[i][j],
					"Expected: [%v], actual: [%v]", want, resp) {
					return false
				}
			}
		}
	case []interface{}:
		defer func() {
			if recover() != nil {
				ast.ElementsMatch(want, resp)
			}
		}()
		respArray := resp.([]interface{})
		if _, ok := want.([]interface{}); !ok {
			return ast.Equal(int(want.(float64)), respArray[0], "Expected: [%v], actual: [%v]", want, resp)
		}
		wantArray := want.([]interface{})
		if len(wantArray) == 0 {
			return ast.Equal(wantArray, respArray)
		}
		if ast.Equalf(len(wantArray), len(respArray), "Expected: [%v], actual: [%v]", want, resp) {
			if respArray[0] == nil {
				return ast.Equal(fmt.Sprintf("%v", want), fmt.Sprintf("%v", resp))
			}
			switch respArray[0].(type) {
			case float64:
				return ast.InDeltaSlicef(wantArray, respArray, 1e-5, "Expected: [%v], actual: [%v]", want, resp)
			default:
				return ast.Equal(fmt.Sprintf("%v", want), fmt.Sprintf("%v", resp))
			}
		} else {
			return false
		}
	default:
		return ast.Equal(want, resp)
	}
	return true
}

func checkSolve(ast *assert.Assertions, testcase TestCase, pkg func(inputJsonValues string) interface{}) {
	gotResp := pkg(testcase.input)
	if !compareGeneral(ast, testcase.want, gotResp) {
		secondResp := pkg(testcase.input)
		if fmt.Sprintf("%v", gotResp) != fmt.Sprintf("%v", secondResp) {
			for i := 0; i < 10000; i++ {
				if compareGeneral(ast, testcase.want, secondResp) {
					return
				}
				secondResp = pkg(testcase.input)
			}
		}
	}
}

func TestEach(t *testing.T, problemId string, problemFolder string, pkg func(inputJsonValues string) interface{}) {
	ast := assert.New(t)
	tests := processTestcase(fmt.Sprintf(TestcaseFolderFmt, problemFolder, problemFolder, problemId))
	for j, testcase := range tests {
		t.Run(fmt.Sprintf("%s/Testcase#%d", problemId, j), func(t *testing.T) {
			checkSolve(ast, testcase, pkg)
		})
	}
}
