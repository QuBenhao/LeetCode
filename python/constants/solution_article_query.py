QUESTION_MY_SOLUTION_LIST_QUERY = """
query questionMySolutionList($questionSlug: String!, $skip: Int, $first: Int) {
  questionSolutionMyArticles(
    questionSlug: $questionSlug
    skip: $skip
    first: $first
  ) {
    totalNum
    edges {
      node {
        uuid
        title
        slug
        status
        createdAt
        author {
          username
          profile {
            userSlug
            realName
          }
        }
        tags {
          name
          slug
        }
        upvoteCount
      }
    }
  }
}
"""

SOLUTION_ARTICLE_QUERY = """
query solutionArticleQuery($slug: String!) {
  solutionArticle(slug: $slug) {
    content
    title
    slug
    uuid
    author {
      username
      profile {
        userSlug
        realName
      }
    }
    createdAt
    updatedAt
    upvoteCount
    favoriteCount
    tags {
      name
      slug
    }
  }
}
"""
