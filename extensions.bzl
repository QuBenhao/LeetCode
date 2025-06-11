## extensions.bzl
load("@bazel_tools//tools/build_defs/repo:local.bzl", "new_local_repository")

def _format_path(folder, problem):
    """Format the path for a problem."""
    return "%s/%s_%s/" % (folder, folder, problem)

def _load_daily_question_impl(ctx):
    script = ctx.path(Label("//:get_daily_path.py"))
    root = ctx.path(Label("//:MODULE.bazel")).dirname
    result = ctx.execute([ctx.which("python3"), script, root])
    if result.return_code != 0:
        fail("Failed to get daily problem path: %s" % result.stderr)
    # result in three lines
    s = result.stdout.strip()
    splits = s.splitlines()
    if len(splits) != 3:
        fail("Expected three lines in output, got: %s" % s)
    folder = splits[0]
    daily_problem = splits[1]
    new_local_repository(
        name = "problems",
        build_file = "//cpp:solution.BUILD",
        path = _format_path(folder, daily_problem),
    )

load_daily_question = module_extension(
    implementation = _load_daily_question_impl,
)

def _impl(rctx):
    script = rctx.path(Label("//:get_daily_path.py"))
    root = rctx.path(Label("//:MODULE.bazel")).dirname
    result = rctx.execute([rctx.which("python3"), script, root])
    if result.return_code != 0:
        fail("Failed to get daily problem path: %s" % result.stderr)
    s = result.stdout.strip()
    splits = s.splitlines()
    if len(splits) != 3:
        fail("Expected three lines in output, got: %s" % s)
    plans = splits[2]
    rctx.file("BUILD", "exports_files([\"plans.bzl\"])\nvisibility = [\"//visibility:public\"]\n")
    rctx.file("plans.bzl", """\
PLANS = %s
""" % ("[" + ",".join(['"%s"' % p for p in plans.split(",")]) + "]"))


daily_plans = repository_rule(
    implementation = _impl,
)