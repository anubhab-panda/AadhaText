from flask import Flask, render_template, request
from extractor import extract_aadhaar
from werkzeug.utils import secure_filename
import os
import tempfile

app = Flask(__name__)

app.config["MAX_CONTENT_LENGTH"] = 5 * 1024 * 1024

ALLOWED_EXTENSIONS = {"png", "jpg", "jpeg"}


def mask_aadhaar(number):
    if not number:
        return None

    digits = "".join(
        ch for ch in str(number) if ch.isdigit()
    )

    # if len(digits) == 12:
    return "XXXX XXXX " + digits[-4:]

    return "Could not extract Aadhaar number"


@app.route("/", methods=["GET", "POST"])
def index():

    data = None
    error = None

    if request.method == "POST":

        file = request.files.get("file")

        if not file or not file.filename:
            error = "Please upload an Aadhaar image."

        else:
            extension = file.filename.rsplit(
                ".", 1
            )[-1].lower()

            if extension not in ALLOWED_EXTENSIONS:
                error = "Only JPG, JPEG and PNG files are allowed."

            else:
                temp_path = None

                try:
                    with tempfile.NamedTemporaryFile(
                        suffix="." + extension,
                        delete=False
                    ) as temp:

                        temp_path = temp.name
                        file.save(temp_path)
                    print("path temp ",temp_path)
                    # data = extract_aadhaar(temp_path)

                    # data["aadhaar_number"] = mask_aadhaar(
                    #     data.get("aadhaar_number")
                    # )
                    result = extract_aadhaar(temp_path)

                    data = {
                        "name": result.get("Full Name"),
                        "dob": result.get("Date/Year of Birth"),
                        "gender": result.get("Gender"),
                        "aadhaar_number": mask_aadhaar(
                            result.get("Aadhaar Number")
                        )
                    }
                    data["aadhaar_number"] = mask_aadhaar(
                         data.get("aadhaar_number"))

                except Exception:
                    error = "Unable to extract details. Please try again."

                finally:
                    if temp_path and os.path.exists(temp_path):
                        os.remove(temp_path)

    return render_template(
        "index.html",
        data=data,
        error=error
    )


if __name__ == "__main__":
    app.run(debug=True)