## extensions.bzl
load("@bazel_tools//tools/build_defs/repo:local.bzl", "new_local_repository")

def _format_path(folder, problem):
    """Format the path for a problem."""
    return "%s/%s_%s/" % (folder, folder, problem)

def _non_module_dependencies_impl(ctx):
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
    plans = splits[2].split(",") if splits[2] else []
    new_local_repository(
        name = "problems",
        build_file = "//cpp:solution.BUILD",
        path = _format_path(folder, daily_problem),
    )

    # i = 0
    # for plan in plans:
    #     new_local_repository(
    #         name = "problem%d" % i,
    #         path = _format_path(folder, plan),
    #         build_file = "//cpp:solution.BUILD",
    #     )
    #     i += 1

non_module_dependencies = module_extension(
    implementation = _non_module_dependencies_impl,
)