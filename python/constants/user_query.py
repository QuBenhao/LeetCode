USER_PROFILE_PUBLIC_QUERY = """
query userProfilePublicProfile($userSlug: String!) {
  userProfilePublicProfile(userSlug: $userSlug) {
    haveFollowed
    siteRanking
    profile {
      userSlug
      realName
      aboutMe
      asciiCode
      userAvatar
      gender
      websites
      skillTags
      ipRegion
      birthday
      location
      useDefaultAvatar
      github
      school: schoolV2 {
        schoolId
        logo
        name
      }
      company: companyV2 {
        id
        logo
        name
      }
      job
      globalLocation {
        country
        province
        city
        overseasCity
      }
      socialAccounts {
        provider
        profileUrl
      }
      skillSet {
        langLevels {
          langName
          langVerboseName
          level
        }
        topics {
          slug
          name
          translatedName
        }
        topicAreaScores {
          score
          topicArea {
            name
            slug
          }
        }
      }
    }
    educationRecordList {
      unverifiedOrganizationName
    }
    occupationRecordList {
      unverifiedOrganizationName
      jobTitle
    }
  }
}
"""