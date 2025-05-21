CONTEST_HISTORY_QUERY = """query contestHistory($pageNum: Int!, $pageSize: Int) {
  contestHistory(pageNum: $pageNum, pageSize: $pageSize) {
    totalNum
    contests {
      containsPremium
      title
      cardImg
      titleSlug
      description
      startTime
      duration
      originStartTime
      isVirtual
      company {
        watermark
        __typename
      }
      isEeExamContest
      __typename
    }
    __typename
  }
}
"""