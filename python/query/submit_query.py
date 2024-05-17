RECENT_SUBMISSIONS_QUERY = """\n
query recentSubmissions($userSlug: String!) {\n
  recentSubmitted(userSlug: $userSlug) {\n
    status\n
    lang\n
    source {\n
      sourceType\n
      ... on SubmissionSrcLeetbookNode {\n
        slug\n
        title\n
        pageId\n
        __typename\n
      }\n
      __typename\n
    }\n
    question {\n
      questionFrontendId\n
      title\n
      translatedTitle\n
      titleSlug\n
      __typename\n
    }\n
    submitTime\n
    __typename\n
  }\n
}\n
"""

RECENT_AC_SUBMISSIONS_QUERY = """\n
query recentAcSubmissions($userSlug: String!) {\n
  recentACSubmissions(userSlug: $userSlug) {\n
    submissionId\n
    submitTime\n
    question {\n
      title\n
      translatedTitle\n
      titleSlug\n
      questionFrontendId\n
    }\n
  }\n
}\n
"""

USER_PROFILE_QUESTIONS_QUERY = """\n
query userProfileQuestions($status: StatusFilterEnum!, $skip: Int!, $first: Int!, $sortField: SortFieldEnum!, $sortOrder: SortingOrderEnum!, $keyword: String, $difficulty: [DifficultyEnum!]) {\n
  userProfileQuestions(status: $status, skip: $skip, first: $first, sortField: $sortField, sortOrder: $sortOrder, keyword: $keyword, difficulty: $difficulty) {\n
    totalNum\n
    questions {\n
      translatedTitle\n
      frontendId\n
      titleSlug\n
      title\n
      difficulty\n
      lastSubmittedAt\n
      numSubmitted\n
      lastSubmissionSrc {\n
        sourceType\n
        ... on SubmissionSrcLeetbookNode {\n
          slug\n
          title\n
          pageId\n
          __typename\n
        }\n
        __typename\n
      }\n
      __typename\n
    }\n
    __typename\n
  }\n
}\n
"""

PROGRESS_SUBMISSIONS_QUERY = """\n
query progressSubmissions($offset: Int, $limit: Int, $lastKey: String, $questionSlug: String) {\n
  submissionList(offset: $offset, limit: $limit, lastKey: $lastKey, questionSlug: $questionSlug) {\n
    lastKey\n
    hasNext\n
    submissions {\n
      id\n
      timestamp\n
      url\n
      lang\n
      runtime\n
      __typename\n
    }\n
    __typename\n
  }\n
}\n
"""

MY_SUBMISSION_DETAIL_QUERY = """\n
query mySubmissionDetail($id: ID!) {\n
  submissionDetail(submissionId: $id) {\n
    id\n
    code\n
    runtime\n
    memory\n
    rawMemory\n
    statusDisplay\n
    timestamp\n
    lang\n
    isMine\n
    passedTestCaseCnt\n
    totalTestCaseCnt\n
    sourceUrl\n
    question {\n
      titleSlug\n
      title\n
      translatedTitle\n
      questionId\n
      __typename\n
    }\n
    ... on GeneralSubmissionNode {\n
      outputDetail {\n
        codeOutput\n
        expectedOutput\n
        input\n
        compileError\n
        runtimeError\n
        lastTestcase\n
        __typename\n
      }\n
      __typename\n
    }\n
    submissionComment {\n
      comment\n
      flagType\n
      __typename\n
    }\n
    __typename\n
  }\n
}\n
"""
