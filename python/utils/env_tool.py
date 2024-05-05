def get_default_folder(problem_category=None):
    if problem_category == "database":
        return "mysql"
    return "problems"
