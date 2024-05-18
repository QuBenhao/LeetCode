PLAN_QUERY = """
query GetMyStudyPlan($progressType: PlanUserProgressTypeEnum!, $offset: Int!, $limit: Int!) {
  studyPlanV2UserProgresses(
    progressType: $progressType
    offset: $offset
    limit: $limit
  ) {
    hasMore
    total
    planUserProgresses {
      nextQuestionInfo {
        inPremiumSubgroup
        nextQuestion {
          id
          questionFrontendId
          title
          titleSlug
          translatedTitle
        }
      }
      nextQuestionInfo {
        inPremiumSubgroup
        nextQuestion {
          id
          questionFrontendId
          title
          titleSlug
          translatedTitle
        }
      }
      quittedAt
      startedAt
      plan {
        questionNum
        slug
        premiumOnly
        name
        onGoing
        highlight
        cover
      }
      latestSubmissionAt
      id
      allCompletedAt
      finishedQuestionNum
    }
  }
}
"""

PLAN_PROGRESS_QUERY = """
query studyPlanProgress($slug: String!, $historyId: ID) {
  studyPlanV2ProgressDetail(planSlug: $slug, id: $historyId) {
    id
    status
    weeklyTaskScheduleResettable
    finishedQuestionNum
    studyPlanDetail {
      questionNum
      planSubGroups {
        slug
        questions {
          titleSlug
          status
        }
      }
    }
  }
}
"""