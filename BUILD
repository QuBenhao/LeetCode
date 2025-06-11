load("//:solutions.bzl", "generate_cc_tests")

generate_cc_tests(enabled = False)

load("@plans//:plans.bzl", "PLANS")
load("@plans//:plans.bzl", "FOLDER")
load("//:solutions.bzl", "gen_plans")

gen_plans(folder= FOLDER, plans = PLANS)
