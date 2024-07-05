def format_question_id(question_id: str) -> str:
    if not question_id:
        return question_id
    if any('\u4e00' <= char <= '\u9fff' for char in question_id):
        if "剑指Offer" in question_id:
            question_id = question_id.replace("剑指Offer", "JZ_Offer")
        elif "面试题" in question_id:
            question_id = question_id.replace("面试题", "Interview")
        else:
            raise ValueError(f"Unknown Chinese question_id: {question_id}, contact the author to add it.")
    if "." in question_id:
        question_id = question_id.replace(".", "__")
    if " " in question_id:
        question_id = question_id.replace(" ", "_")
    return question_id


def back_question_id(question_id: str) -> str:
    if not question_id:
        return question_id
    if "__" in question_id:
        question_id = question_id.replace("__", ".")
    if "_" in question_id:
        question_id = question_id.replace("_", " ")
    if "JZ_Offer" in question_id:
        question_id = question_id.replace("JZ_Offer", "剑指Offer")
    if "Interview" in question_id:
        question_id = question_id.replace("Interview", "面试题")
    return question_id
