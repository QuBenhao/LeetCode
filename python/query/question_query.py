QUESTION_INFO_QUERY = """\n
query questionTitle($titleSlug: String!) {\n
  question(titleSlug: $titleSlug) {\n
    questionId\n
    questionFrontendId\n
    title\n
    titleSlug\n
    isPaidOnly\n
    difficulty\n
    likes\n
    dislikes\n
    categoryTitle\n
  }\n
}\n
"""

QUESTION_DESC_QUERY = """\n
query questionContent($titleSlug: String!) {\n
  question(titleSlug: $titleSlug) {\n
    content\n
    editorType\n
    mysqlSchemas\n
    dataSchemas\n
  }\n
}\n
"""

QUESTION_CODE_QUERY = """\n
query questionEditorData($titleSlug: String!) {\n
  question(titleSlug: $titleSlug) {\n
    questionId\n
    questionFrontendId\n
    codeSnippets {\n
      lang\n
      langSlug\n
      code\n
    }\n
    envInfo\n
    enableRunCode\n
    hasFrontendPreview\n
    frontendPreviews\n
  }\n
}\n
"""

QUESTION_TESTCASE_QUERY = """\n
query consolePanelConfig($titleSlug: String!) {\n
  question(titleSlug: $titleSlug) {\n
    questionId\n
    questionFrontendId\n
    questionTitle\n
    enableRunCode\n
    enableSubmit\n
    enableTestMode\n
    jsonExampleTestcases\n
    exampleTestcases\n
    metaData\n
    sampleTestCase\n
  }\n
}\n
"""

QUESTION_KEYWORDS_QUERY = """\n
query problemsetQuestionList($categorySlug: String, $limit: Int, $skip: Int, $filters: QuestionListFilterInput) {\n
  problemsetQuestionList(\n
    categorySlug: $categorySlug\n
    limit: $limit\n
    skip: $skip\n
    filters: $filters\n
  ) {\n
    hasMore\n
    total\n
    questions {\n
      acRate\n
      difficulty\n
      freqBar\n
      frontendQuestionId\n
      isFavor\n
      paidOnly\n
      solutionNum\n
      status\n
      title\n
      titleCn\n
      titleSlug\n
      topicTags {\n
        name\n
        nameTranslated\n
        id\n
        slug\n
      }\n
      extra {\n
        hasVideoSolution\n
        topCompanyTags {\n
          imgUrl\n
          slug\n
          numSubscribed\n
        }\n
      }\n
    }\n
  }\n
}\n
"""
