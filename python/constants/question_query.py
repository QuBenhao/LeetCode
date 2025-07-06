QUESTION_INFO_QUERY = """
query questionTitle($titleSlug: String!) {
  question(titleSlug: $titleSlug) {
    questionId
    questionFrontendId
    title
    titleSlug
    isPaidOnly
    difficulty
    likes
    dislikes
    categoryTitle
  }
}
"""

QUESTION_DESC_QUERY = """
query questionContent($titleSlug: String!) {
  question(titleSlug: $titleSlug) {
    content
    editorType
    mysqlSchemas
    dataSchemas
  }
}
"""

QUESTION_DESC_CN_QUERY = """
query questionTranslations($titleSlug: String!) {
  question(titleSlug: $titleSlug) {
    translatedTitle
    translatedContent
  }
}
"""

QUESTION_CODE_QUERY = """
query questionEditorData($titleSlug: String!) {
  question(titleSlug: $titleSlug) {
    questionId
    questionFrontendId
    codeSnippets {
      lang
      langSlug
      code
    }
    envInfo
    enableRunCode
    hasFrontendPreview
    frontendPreviews
  }
}
"""

QUESTION_TESTCASE_QUERY = """
query consolePanelConfig($titleSlug: String!) {
  question(titleSlug: $titleSlug) {
    questionId
    questionFrontendId
    questionTitle
    enableRunCode
    enableSubmit
    enableTestMode
    jsonExampleTestcases
    exampleTestcases
    metaData
    sampleTestCase
  }
}
"""

QUESTION_KEYWORDS_QUERY = """
query problemsetQuestionListV2($filters: QuestionFilterInput, $limit: Int, $searchKeyword: String, $skip: Int, $sortBy: QuestionSortByInput, $categorySlug: String) {
  problemsetQuestionListV2(
    filters: $filters
    limit: $limit
    searchKeyword: $searchKeyword
    skip: $skip
    sortBy: $sortBy
    categorySlug: $categorySlug
  ) {
    questions {
      id
      titleSlug
      title
      translatedTitle
      questionFrontendId
      paidOnly
      difficulty
      topicTags {
        name
        slug
        nameTranslated
      }
      status
      isInMyFavorites
      frequency
      acRate
      contestPoint
    }
    totalLength
    finishedLength
    hasMore
  }
}
"""
