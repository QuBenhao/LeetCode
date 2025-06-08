ADD_QUESTION_TO_FAVORITE_QUERY = """
    mutation batchAddQuestionsToFavorite($favoriteSlug: String!, $questionSlugs: [String]!) {
  batchAddQuestionsToFavorite(
    favoriteSlug: $favoriteSlug
    questionSlugs: $questionSlugs
  ) {
    ok
    error
  }
}"""

MY_FAVORITE_QUERY = """
    query myFavoriteList {
  myCreatedFavoriteList {
    favorites {
      coverUrl
      coverEmoji
      coverBackgroundColor
      hasCurrentQuestion
      isPublicFavorite
      lastQuestionAddedAt
      name
      slug
      favoriteType
    }
    hasMore
    totalLength
  }
  myCollectedFavoriteList {
    hasMore
    totalLength
    favorites {
      coverUrl
      coverEmoji
      coverBackgroundColor
      hasCurrentQuestion
      isPublicFavorite
      name
      slug
      lastQuestionAddedAt
      favoriteType
    }
  }
}"""

FAVORITE_QUESTION_QUERY = """
    query favoriteQuestionList($favoriteSlug: String!, $filter: FavoriteQuestionFilterInput, $searchKeyword: String, $filtersV2: QuestionFilterInput, $sortBy: QuestionSortByInput, $limit: Int, $skip: Int, $version: String = "v2") {
  favoriteQuestionList(
    favoriteSlug: $favoriteSlug
    filter: $filter
    filtersV2: $filtersV2
    searchKeyword: $searchKeyword
    sortBy: $sortBy
    limit: $limit
    skip: $skip
    version: $version
  ) {
    questions {
      difficulty
      id
      paidOnly
      questionFrontendId
      status
      title
      titleSlug
      translatedTitle
      isInMyFavorites
      frequency
      acRate
      topicTags {
        name
        nameTranslated
        slug
      }
    }
    totalLength
    hasMore
  }
}
"""