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
