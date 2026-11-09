# Aadhaar OCR Extractor

A web-based Aadhaar Card OCR (Optical Character Recognition) application built using **Python, Flask, and OpenBharatOCR**. It extracts important details from uploaded Aadhaar card images and displays the results through a simple web interface.

## 🚀 Features

- Upload Aadhaar card images in JPG, JPEG, and PNG formats.
- Extract Aadhaar details using OpenBharatOCR.
- Retrieve information such as:
  - Full Name
  - Date/Year of Birth
  - Gender
  - Aadhaar Number
- Mask Aadhaar numbers to improve privacy.
- Simple and user-friendly web interface.
- Temporary file handling with automatic cleanup.

## 🛠️ Technologies Used

- Python
- Flask
- OpenBharatOCR
- HTML
- CSS
- OpenCV

## 📁 Project Structure

```text
Aadhaar-OCR-Extractor/
│
├── app.py              # Flask application
├── extractor.py        # Aadhaar OCR extraction logic
├── templates/
│   └── index.html      # Web interface
├── requirements.txt    # Project dependencies
└── README.md           # Project documentation
```

## ⚙️ Installation and Setup

### 1. Clone the Repository

```bash
git clone https://github.com/anubhab-panda/AadhaText.git
```

### 2. Navigate to the Project Directory

```bash
cd AadhaText
```

### 3. Create a Virtual Environment

```bash
python -m venv venv
```

### 4. Activate the Virtual Environment

**Windows PowerShell:**

```powershell
.\venv\Scripts\Activate.ps1
```

### 5. Install Dependencies

```bash
pip install -r requirements.txt
```

### 6. Run the Application

```bash
python app.py
```

### 7. Open the Application

Open your browser and visit:

```text
http://127.0.0.1:5000
```

Upload an Aadhaar card image to extract the details.

## 📸 How It Works

1. The user uploads an Aadhaar card image through the web interface.
2. Flask receives the uploaded file.
3. The image is temporarily saved on the server.
4. OpenBharatOCR processes the image and extracts the relevant information.
5. The Aadhaar number is masked before displaying the result.
6. The temporary file is deleted after processing.

## 🔐 Privacy and Security

This project is intended for educational and demonstration purposes.

- Aadhaar information is sensitive personal data.
- Use only documents you are authorized to process.
- Avoid storing Aadhaar numbers or personal information unnecessarily.
- Do not upload real Aadhaar card images to public repositories.
- Ensure appropriate security measures before deploying this application publicly.

## ⚠️ Disclaimer

This application is an OCR-based tool and may not always extract information accurately. OCR results should be verified manually.

This project is not affiliated with or endorsed by UIDAI.

## 👨‍💻 Author

GitHub: [Anubhab Panda](https://github.com/anubhab-panda)

---

If you find this project useful, consider giving it a ⭐ on GitHub.
