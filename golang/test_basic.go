package golang

import (
	"encoding/json/v2"
	"fmt"
	"log"
	"os"
	"path"
	"reflect"
	"runtime"
	"strings"
	"testing"

	"github.com/stretchr/testify/assert"
)

const TestcaseFolderFmt = "%s/%s_%s/testcase"
const RunTimes = 10000

type TestCase struct {
	input string
	want  any
}

func processTestcase(problemPath string) (tests []TestCase) {
	inputs := make([]string, 0)
	var outputs any
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
		tests = append(tests, TestCase{input, outputs.([]any)[i]})
	}
	if len(inputs) == 0 {
		log.Fatalf("[ERROR] No testcases found! ProblemPath: %s", problemPath)
	}
	return
}

func compareGeneral(ast *assert.Assertions, want any, resp any) bool {
	respValue := reflect.ValueOf(resp)
	if num, ok := reflect.TypeAssert[int](respValue); ok {
		return ast.Equal(int(want.(float64)), num)
	}
	if num, ok := reflect.TypeAssert[int64](respValue); ok {
		return ast.Equal(int64(want.(float64)), num)
	}
	if num, ok := reflect.TypeAssert[float64](respValue); ok {
		return ast.InDelta(want, num, 1e-5)
	}
	if bytes, ok := reflect.TypeAssert[byte](respValue); ok {
		return ast.Equalf(want.(string)[0], bytes, "Expected: [%s], actual: [%s]", want, string(bytes))
	}
	if num2DArray, num2DArrayOk := reflect.TypeAssert[[][]int](respValue); num2DArrayOk {
		wantArray := want.([]any)
		if !ast.Equalf(len(wantArray), len(num2DArray), "Expected: [%v], actual: [%v]", want, resp) {
			return false
		}
		for i := 0; i < len(num2DArray); i++ {
			if !ast.Equalf(len(wantArray[i].([]any)), len(num2DArray[i]),
				"Expected: [%v], actual: [%v]", want, resp) {
				return false
			}
			for j := 0; j < len(num2DArray[i]); j++ {
				if !ast.Equalf(int(wantArray[i].([]any)[j].(float64)), num2DArray[i][j],
					"Expected: [%v], actual: [%v]", want, resp) {
					return false
				}
			}
		}
	} else if numArray, numArrayOk := reflect.TypeAssert[[]int](respValue); numArrayOk {
		if _, ok := want.([]any); !ok {
			return ast.Equal(int(want.(float64)), numArray[0], "Expected: [%v], actual: [%v]", want, resp)
		}
		if want == nil {
			return ast.Nil(resp, "Expected: [%v], actual: [%v]", want, resp)
		}
		wantArray := want.([]any)
		if !ast.Equalf(len(wantArray), len(numArray), "Expected: [%v], actual: [%v]", want, resp) {
			return false
		}
		for j := 0; j < len(numArray); j++ {
			if !ast.Equalf(int(wantArray[j].(float64)), numArray[j], "Expected: [%v], actual: [%v]", want, resp) {
				return false
			}
		}
	} else if stringArray, stringArrayOk := reflect.TypeAssert[[]string](respValue); stringArrayOk {
		if v, ok := want.([]string); ok {
			return ast.Equal(v, stringArray)
		}
		if !ast.Equalf(len(want.([]any)), len(stringArray),
			"Expected: [%v], actual: [%v]", want, resp) {
			return false
		}
		for i := 0; i < len(stringArray); i++ {
			if !ast.Equalf(want.([]any)[i], stringArray[i],
				"Expected: [%v], actual: [%v]", want, resp) {
				return false
			}
		}
	} else if string2DArray, string2DArrayOk := reflect.TypeAssert[[][]string](respValue); string2DArrayOk {
		wantArray := want.([]any)
		if !ast.Equalf(len(wantArray), len(string2DArray), "Expected: [%v], actual: [%v]", want, resp) {
			return false
		}

		for i := 0; i < len(string2DArray); i++ {
			if !ast.Equalf(len(wantArray[i].([]any)), len(string2DArray[i]),
				"Expected: [%v], actual: [%v]", want, resp) {
				return false
			}
			for j := 0; j < len(string2DArray[i]); j++ {
				if !ast.Equalf(len(wantArray[i].([]any)[j].(string)), len(string2DArray[i][j]),
					"Expected: [%v], actual: [%v]", want, resp) {
					return false
				}
				if !ast.Equalf(wantArray[i].([]any)[j], string2DArray[i][j],
					"Expected: [%v], actual: [%v]", want, resp) {
					return false
				}
			}
		}
	} else if boolArray, boolArrayOk := reflect.TypeAssert[[]bool](respValue); boolArrayOk {
		wantArray := want.([]any)
		if !ast.Equalf(len(wantArray), len(boolArray), "Expected: [%v], actual: [%v]", want, resp) {
			return false
		}
		for i := 0; i < len(boolArray); i++ {
			if !ast.Equalf(wantArray[i], boolArray[i], "Expected: [%v], actual: [%v]", want, resp) {
				return false
			}
		}
	} else if respArray, anyArrayOk := reflect.TypeAssert[[]any](respValue); anyArrayOk {
		defer func() {
			if recover() != nil {
				ast.ElementsMatch(want, resp)
			}
		}()
		if _, ok := want.([]any); !ok {
			return ast.Equal(int(want.(float64)), respArray[0], "Expected: [%v], actual: [%v]", want, resp)
		}
		wantArray := want.([]any)
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
	} else {
		return ast.Equal(want, resp)
	}
	return true
}

func checkSolve(ast *assert.Assertions, testcase TestCase, pkg func(inputJsonValues string) any) bool {
	gotResp := pkg(testcase.input)
	if !compareGeneral(ast, testcase.want, gotResp) {
		secondResp := pkg(testcase.input)
		if fmt.Sprintf("%v", gotResp) != fmt.Sprintf("%v", secondResp) {
			for range RunTimes {
				if compareGeneral(ast, testcase.want, secondResp) {
					return true
				}
				secondResp = pkg(testcase.input)
			}
		}
		return false
	}
	return true
}

func TestEach(t *testing.T, problemId string, problemFolder string, pkg func(inputJsonValues string) any) {
	ast := assert.New(t)
	t.Attr("problemId", problemId)
	tests := processTestcase(fmt.Sprintf(TestcaseFolderFmt, problemFolder, problemFolder, problemId))
	for j, testcase := range tests {
		t.Run(fmt.Sprintf("%s/Testcase#%d", problemId, j), func(t *testing.T) {
			fmt.Printf("Input: %v\nExpected: %v\n", testcase.input, testcase.want)
			if !checkSolve(ast, testcase, pkg) {
				t.FailNow()
			}
		})
	}
}
