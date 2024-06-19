def get_default_folder(problem_category: str = None, paid_only: bool = False):
    if problem_category == "database":
        return "mysql"
    return "problems" if not paid_only else "premiums"
