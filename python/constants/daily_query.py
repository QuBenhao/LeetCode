DAILY_QUERY = """
    query questionOfTodayV2 {
  todayRecord {
    date
    userStatus
    question {
      id: questionId
      titleSlug
      title
      translatedTitle
      questionFrontendId
      paidOnly: isPaidOnly
      difficulty
      topicTags {
        name
        slug
        nameTranslated: translatedName
      }
      status
      isInMyFavorites: isFavor
      acRate
      frequency: freqBar
    }
  }
}
"""
