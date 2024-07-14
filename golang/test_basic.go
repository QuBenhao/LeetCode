package golang

import (
	"encoding/json"
	"fmt"
	"github.com/stretchr/testify/assert"
	"log"
	"os"
	"path"
	"runtime"
	"strings"
	"testing"
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

func compareGeneral(ast *assert.Assertions, want interface{}, resp interface{}) {
	switch resp.(type) {
	case int:
		ast.Equal(int(want.(float64)), resp.(int))
	case int64:
		ast.Equal(int64(want.(float64)), resp.(int64))
	case float64:
		ast.InDelta(want, resp, 1e-5)
	case byte:
		ast.Equalf(want.(string)[0], resp, "Expected: [%s], actual: [%s]", want, string(resp.(byte)))
	case [][]int:
		wantArray := want.([]interface{})
		respIntArray := resp.([][]int)
		if !ast.Equalf(len(wantArray), len(respIntArray), "Expected: [%v], actual: [%v]", want, resp) {
			return
		}
		for i := 0; i < len(respIntArray); i++ {
			if !ast.Equalf(len(wantArray[i].([]interface{})), len(respIntArray[i]),
				"Expected: [%v], actual: [%v]", want, resp) {
				return
			}
			for j := 0; j < len(respIntArray[i]); j++ {
				ast.Equalf(int(wantArray[i].([]interface{})[j].(float64)), respIntArray[i][j],
					"Expected: [%v], actual: [%v]", want, resp)
			}
		}
	case []int:
		wantArray := want.([]interface{})
		respIntArray := resp.([]int)
		if !ast.Equalf(len(wantArray), len(respIntArray), "Expected: [%v], actual: [%v]", want, resp) {
			return
		}
		for j := 0; j < len(respIntArray); j++ {
			ast.Equalf(int(wantArray[j].(float64)), respIntArray[j], "Expected: [%v], actual: [%v]", want, resp)
		}

	case []string:
		ast.Equal(want.([]string), resp)
	case [][]string:
		wantArray := want.([]interface{})
		respStrArray := resp.([][]string)
		if !ast.Equalf(len(wantArray), len(respStrArray), "Expected: [%v], actual: [%v]", want, resp) {
			return
		}

		for i := 0; i < len(respStrArray); i++ {
			if !ast.Equalf(len(wantArray[i].([]interface{})), len(respStrArray[i]),
				"Expected: [%v], actual: [%v]", want, resp) {
				return
			}
			for j := 0; j < len(respStrArray[i]); j++ {
				if !ast.Equalf(len(wantArray[i].([]interface{})[j].(string)), len(respStrArray[i][j]),
					"Expected: [%v], actual: [%v]", want, resp) {
					return
				}
				ast.Equalf(wantArray[i].([]interface{})[j], respStrArray[i][j],
					"Expected: [%v], actual: [%v]", want, resp)
			}
		}

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
			return
		}
		if ast.Equalf(len(wantArray), len(respArray), "Expected: [%v], actual: [%v]", want, resp) {

			if respArray[0] == nil {
				ast.Equal(fmt.Sprintf("%v", want), fmt.Sprintf("%v", resp))
				return
			}
			switch respArray[0].(type) {
			case float64:
				ast.InDeltaSlicef(wantArray, respArray, 1e-5, "Expected: [%v], actual: [%v]", want, resp)
			default:
				ast.Equal(fmt.Sprintf("%v", want), fmt.Sprintf("%v", resp))
			}
		}
	default:
		ast.Equal(want, resp)
	}
}

func TestEach(t *testing.T, problemId string, problemFolder string, pkg func(inputJsonValues string) interface{}) {
	ast := assert.New(t)
	tests := processTestcase(fmt.Sprintf(TestcaseFolderFmt, problemFolder, problemFolder, problemId))
	for j, testcase := range tests {
		t.Run(fmt.Sprintf("%s/Testcase#%d", problemId, j), func(t *testing.T) {
			gotResp := pkg(testcase.input)
			compareGeneral(ast, testcase.want, gotResp)
		})
	}
}
