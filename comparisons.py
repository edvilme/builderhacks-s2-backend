import string
import spacy
from quantulum3 import parser
from latex2sympy import latex2sympy
nlp = spacy.load("en_core_web_sm")


def comparison_text_strict(submission: str, answer: str) -> bool:
    return submission == answer

def comparison_text_medium(submission: str, answer: str) -> bool:
    def __medium_transform(s: str) -> str:
        return s.lower().translate( str.maketrans(dict.fromkeys(string.punctuation)) )
    return __medium_transform(submission) == __medium_transform(answer)

def comparion_text_similarity(submission: str, answer: str) -> bool:
    return nlp(answer).similarity(nlp(submission)) >= 0.8

def comparison_num_strict(submission: str, answer: str) -> bool:
    submission_expr = parser.parse(submission)
    answer_expr = parser.parse(answer)
    # Check if scalars are equal
    if(submission_expr[0].value != answer_expr[0].value):
        return False
    # Check if units are equal
    if(submission_expr[0].unit.name != answer_expr[0].unit.name):
        return False
    return True

def comparison_math_equality(submission: str, answer: str) -> bool:
    submission_expr = latex2sympy(submission)
    answer_expr = latex2sympy(answer)
    return submission_expr.equals(answer_expr)