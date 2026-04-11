## extensions.bzl

def _impl(rctx):
    script = rctx.path(Label("//:get_daily_path.py"))
    root = rctx.path(Label("//:MODULE.bazel")).dirname
    result = rctx.execute([rctx.which("python3"), script, root])
    if result.return_code != 0:
        fail("Failed to get daily problem path: %s" % result.stderr)
    s = result.stdout.strip()
    splits = s.splitlines()
    if len(splits) < 2:
        fail("Expected at least two lines in output, got: %s" % s)
    folder = splits[0]
    rctx.path(Label("//:daily-" + folder + ".json"))
    daily_problem = splits[1]
    plans = splits[2] if len(splits) > 2 else ""

    # Read link_mappings.bzl if it exists
    link_mappings_content = "LINK_MAPPINGS = {}"
    link_mappings_path = root.get_child("link_mappings.bzl")
    if link_mappings_path.exists:
        link_mappings_content = rctx.read(link_mappings_path)

    rctx.file("BUILD", "exports_files([\"daily.bzl\"])\nvisibility = [\"//visibility:public\"]\n")
    rctx.file("daily.bzl", """
FOLDER = "%s"
DAILY_PROBLEM = "%s"
PLANS = %s

%s
""" % (folder, daily_problem, "[" + ",".join(['"%s"' % p for p in plans.split(",")]) + "]", link_mappings_content))

daily = repository_rule(
    implementation = _impl,
)
