# phishing_website_detection_tool
# Phishing Website Detection Tool

## 📌 Project Overview

The **Phishing Website Detection Tool** is a simple web application developed to identify whether a given website URL is safe or potentially a phishing site. Phishing attacks are commonly used by attackers to steal sensitive information such as login credentials, banking details, and personal data by creating fake websites that look legitimate.

This project analyzes different characteristics of a URL and determines if the website might be suspicious.

## 🎯 Objective

The main objective of this project is to:

* Detect suspicious or phishing websites.
* Help users verify the safety of a URL before visiting it.
* Understand basic cybersecurity concepts related to phishing attacks.

## 🛠 Technologies Used

* **Python** – Backend logic
* **Flask** – Web framework
* **HTML** – Webpage structure
* **CSS** – Styling and user interface

## ⚙️ How the System Works

The tool checks several features of a URL, such as:

* Length of the URL
* Presence of **@ symbol**
* Use of **IP address instead of domain**
* Whether the website uses **HTTPS**
* Presence of **hyphens (-) in domain name**

Based on these features, the system calculates a score and determines whether the URL is **safe or potentially a phishing website**.

## 📂 Project Structure

```
phishing_detection_tool
│
├── app.py
├── requirements.txt
├── README.md
│
├── templates
│   └── index.html
│
└── static
    └── style.css
```

## 🚀 How to Run the Project

1. Clone the repository
2. Install required dependencies
3. Run the application
4. Open the application in your browser

Example:

```
pip install flask
python app.py
```

Then open:

```
http://127.0.0.1:5000
```

## 🔍 Usage

1. Enter a website URL in the input field.
2. Click the **Check Website** button.
3. The system will display whether the website is **safe or suspicious**.

## 📚 Learning Outcome

This project helps in understanding:

* Basic **cybersecurity concepts**
* URL-based **phishing detection techniques**
* Building a **web application using Flask**
* Integrating frontend and backend development

## ⭐ Conclusion

Phishing attacks are one of the most common cybersecurity threats. This tool demonstrates a basic approach to detecting suspicious URLs and helps users become more aware of potential online threats.

---
Thank you for taking the time to explore this project. Your feedback and support are greatly appreciated.
---
This project was developed as part of learning cybersecurity and web development concepts
--------
⭐ If you find this project useful, feel free to give this repository a star.
      
