load("@daily//:daily.bzl", "FOLDER", "DAILY_PROBLEM", "PLANS", "LINK_MAPPINGS")
load("//:solutions.bzl", "generate_cc_tests", "gen_daily")

gen_daily(folder = FOLDER, problem = DAILY_PROBLEM, plans = PLANS, link_mappings = LINK_MAPPINGS)
generate_cc_tests(link_mappings = LINK_MAPPINGS)
