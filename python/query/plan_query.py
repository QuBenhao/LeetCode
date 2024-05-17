PLAN_QUERY = """\n
query GetMyStudyPlan($progressType: PlanUserProgressTypeEnum!, $offset: Int!, $limit: Int!) {\n
  studyPlanV2UserProgresses(\n
    progressType: $progressType\n
    offset: $offset\n
    limit: $limit\n
  ) {\n
    hasMore\n
    total\n
    planUserProgresses {\n
      nextQuestionInfo {\n
        inPremiumSubgroup\n
        nextQuestion {\n
          id\n
          questionFrontendId\n
          title\n
          titleSlug\n
          translatedTitle\n
        }\n
      }\n
      nextQuestionInfo {\n
        inPremiumSubgroup\n
        nextQuestion {\n
          id\n
          questionFrontendId\n
          title\n
          titleSlug\n
          translatedTitle\n
        }\n
      }\n
      quittedAt\n
      startedAt\n
      plan {\n
        questionNum\n
        slug\n
        premiumOnly\n
        name\n
        onGoing\n
        highlight\n
        cover\n
      }\n
      latestSubmissionAt\n
      id\n
      allCompletedAt\n
      finishedQuestionNum\n
    }\n
  }\n
}\n
"""

PLAN_PROGRESS_QUERY = """\n
query studyPlanProgress($slug: String!, $historyId: ID) {\n
  studyPlanV2ProgressDetail(planSlug: $slug, id: $historyId) {\n
    id\n
    status\n
    weeklyTaskScheduleResettable\n
    finishedQuestionNum\n
    studyPlanDetail {\n
      questionNum\n
      planSubGroups {\n
        slug\n
        questions {\n
          titleSlug\n
          status\n
        }\n
      }\n
    }\n
  }\n
}\n
"""