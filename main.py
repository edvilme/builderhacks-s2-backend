from urllib import request
from flask import Flask, request
import comparisons
from flask_cors import CORS, cross_origin

app = Flask(__name__)

CORS(app)
cors = CORS(app, resource={
    r"/*":{
        "origins":"*"
    }
})

@app.route("/")
@cross_origin()
def hello_world():
    return "Hello world from edvilme!!"

@app.route("/test", methods=["POST"])
@cross_origin()
def test():
    submission = request.get_json(force=True)
    submission_type = submission['type']
    submission_submission = submission['submission']
    submission_answer = submission['answer']
    try:
        if(submission_type == "comparison_text_strict"):
            return {
                "correct": comparisons.comparison_text_strict(submission_submission, submission_answer)
            }
        if(submission_type == "comparison_text_medium"):
            return {
                "correct": comparisons.comparison_text_medium(submission_submission, submission_answer)
            }
        if(submission_type == "comparison_text_similarity"):
            return {
                "correct": comparisons.comparion_text_similarity(submission_submission, submission_answer)
            }
        if(submission_type == "comparison_num_strict"):
            return {
                "correct": comparisons.comparison_num_strict(submission_submission, submission_answer)
            }
        if(submission_type == "comparison_math_equality"):
            return {
                "correct": comparisons.comparison_math_equality(submission_submission, submission_answer)
            }
    except:
        return {
            "correct": False
        }

if __name__ == "__main__":
    app.run(port=8080, host='0.0.0.0')