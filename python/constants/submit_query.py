RECENT_SUBMISSIONS_QUERY = """
query recentSubmissions($userSlug: String!) {
  recentSubmitted(userSlug: $userSlug) {
    status
    lang
    source {
      sourceType
      ... on SubmissionSrcLeetbookNode {
        slug
        title
        pageId
        __typename
      }
      __typename
    }
    question {
      questionFrontendId
      title
      translatedTitle
      titleSlug
      __typename
    }
    submitTime
    __typename
  }
}
"""

RECENT_AC_SUBMISSIONS_QUERY = """
query recentAcSubmissions($userSlug: String!) {
  recentACSubmissions(userSlug: $userSlug) {
    submissionId
    submitTime
    question {
      title
      translatedTitle
      titleSlug
      questionFrontendId
    }
  }
}
"""

USER_PROFILE_QUESTIONS_QUERY = """
query userProfileQuestions($status: StatusFilterEnum!, $skip: Int!, $first: Int!, $sortField: SortFieldEnum!, $sortOrder: SortingOrderEnum!, $keyword: String, $difficulty: [DifficultyEnum!]) {
  userProfileQuestions(status: $status, skip: $skip, first: $first, sortField: $sortField, sortOrder: $sortOrder, keyword: $keyword, difficulty: $difficulty) {
    totalNum
    questions {
      translatedTitle
      frontendId
      titleSlug
      title
      difficulty
      lastSubmittedAt
      numSubmitted
      lastSubmissionSrc {
        sourceType
        ... on SubmissionSrcLeetbookNode {
          slug
          title
          pageId
          __typename
        }
        __typename
      }
      __typename
    }
    __typename
  }
}
"""

PROGRESS_SUBMISSIONS_QUERY = """
query progressSubmissions($offset: Int, $limit: Int, $lastKey: String, $questionSlug: String) {
  submissionList(offset: $offset, limit: $limit, lastKey: $lastKey, questionSlug: $questionSlug) {
    lastKey
    hasNext
    submissions {
      id
      timestamp
      url
      lang
      runtime
      __typename
    }
    __typename
  }
}
"""

MY_SUBMISSION_DETAIL_QUERY = """
query mySubmissionDetail($id: ID!) {
  submissionDetail(submissionId: $id) {
    id
    code
    runtime
    memory
    rawMemory
    statusDisplay
    timestamp
    lang
    isMine
    passedTestCaseCnt
    totalTestCaseCnt
    sourceUrl
    question {
      titleSlug
      title
      translatedTitle
      questionId
      __typename
    }
    ... on GeneralSubmissionNode {
      outputDetail {
        codeOutput
        expectedOutput
        input
        compileError
        runtimeError
        lastTestcase
        __typename
      }
      __typename
    }
    submissionComment {
      comment
      flagType
      __typename
    }
    __typename
  }
}
"""
