package golang

import (
	"encoding/json"
	"fmt"
	"github.com/stretchr/testify/assert"
	problem "leetCode/problems/1553"
	"log"
	"math"
	"os"
	"path"
	"runtime"
	"strings"
	"testing"
)

const TestcaseFolderFmt = "problems/%s/testcase"

var problemId string = "1553"

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

func TestSolution(t *testing.T) {
	ast := assert.New(t)
	tests := processTestcase()
	for i, testcase := range tests {
		t.Run(fmt.Sprintf("%s/Testcase#%d", problemId, i), func(t *testing.T) {
			gotResp := problem.Solve(testcase.input)
			switch testcase.want.(type) {
			case float64:
				switch gotResp.(type) {
				case float64:
					ast.LessOrEqual(1e-5, math.Abs(testcase.want.(float64)-gotResp.(float64)))
				case int:
					ast.Equal(int(testcase.want.(float64)), gotResp.(int))
				case int64:
					ast.Equal(int64(testcase.want.(float64)), gotResp.(int64))
				default:
					ast.Equal(testcase.want, gotResp)
				}
			case []interface{}:
				wantArray := testcase.want.([]interface{})
				defer func() {
					if recover() != nil {
						respIntArray := gotResp.([]int)
						if ast.Equalf(len(wantArray), len(respIntArray), "Expected: [%v], actual: [%v]", testcase.want, gotResp) {
							for j := 0; j < len(respIntArray); j++ {
								ast.Equal(int(wantArray[j].(float64)), respIntArray[j], "Expected: [%v], actual: [%v]", testcase.want, gotResp)
							}
						}
					}
				}()
				respArray := gotResp.([]interface{})
				if len(wantArray) == 0 || len(respArray) == 0 {
					ast.Equalf(len(wantArray), len(respArray), "Expected: [%v], actual: [%v]", testcase.want, gotResp)
				} else {
					switch wantArray[0].(type) {
					case float64:
						{
							switch respArray[0].(type) {
							case float64:
								if ast.Equalf(len(wantArray), len(respArray), "Expected: [%v], actual: [%v]", testcase.want, gotResp) {
									for j := 0; j < len(wantArray); j++ {
										ast.LessOrEqualf(1e-5, math.Abs(wantArray[j].(float64)-respArray[j].(float64)), "Expected: [%v], actual: [%v]", testcase.want, gotResp)
									}
								}
							case int:
								if ast.Equalf(len(wantArray), len(respArray), "Expected: [%v], actual: [%v]", testcase.want, gotResp) {
									for j := 0; j < len(wantArray); j++ {
										if wantArray[j] == nil {
											ast.Nil(respArray[j])
										} else {
											ast.Equalf(int(wantArray[j].(float64)), respArray[j].(int), "Expected: [%v], actual: [%v]", testcase.want, gotResp)
										}
									}
								}
							default:
								ast.Equal(wantArray, respArray)
							}
						}
					default:
						ast.Equal(wantArray, respArray)
					}
				}
			default:
				ast.Equal(testcase.want, gotResp)
			}
		})
	}
}
