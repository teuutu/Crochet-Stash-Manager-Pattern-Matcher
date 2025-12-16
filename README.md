# Crochet-Stash-Manager-Pattern-Matcher
1. Overview
   
Crochet-Stash-Manager-Pattern-Matcher is a full-stack Python application designed to help crafters efficiently manage their yarn inventory and instantly find viable projects based on the materials they currently own.
This project demonstrates core skills in Data Structuring, Database Persistence, Basic NLP (Natural Language Processing), and Web Deployment, showcasing the ability to apply technical skills to a specific domain problem.

2. Features
   
Inventory Management: Stores and retrieves yarn stash details (weight, yardage, hook size, quantity) using SQLite.
Pattern Matching Logic: Analyzes inventory against pattern requirements to suggest viable projects.
Pattern Text Analysis (Basic NLP): Parses pattern instructions to estimate project complexity or stitch count (demonstrated in the get_total_stitches method).
Interactive Web Interface: Provides a user-friendly dashboard for viewing the stash, the pattern library, and the analysis results, built with Streamlit.
Zero-Configuration Deployment: Configured for seamless deployment on Streamlit Community Cloud.

3. Live Demo
🔗 View the Live Application: 

4. Technology Stack

5. Setup and Installation
 
Prerequisites
Python 3.8+

Git

Installation Steps

1. Clone the Repository:
   git clone https://github.com/teuutu/Crochet-Stash-Manager-Pattern-Matcher.git
cd Crochet-Stash-Manager-Pattern-Matcher

2. Create and Activate Virtual Environment:
   # For Windows (CMD):
python -m venv venv
venv\Scripts\activate.bat
# For macOS/Linux:
python3 -m venv venv
source venv/bin/activate

3. Install Dependencies:
   
pip install -r requirements.txt

4.Run the Application: 

The application will automatically initialize the SQLite database (crochet_inventory.db) with sample data upon launch.
streamlit run streamlit_app.py

6. Project Structure
   
   crochet-pattern-utility/
├── crochet_data.py          # Data models (Yarn, Pattern classes) and basic OOP structure.
├── db_manager.py            # SQLite setup, initialization, and CRUD operations.
├── crochet_analyzer.py      # Core business logic: pattern matching and analysis.
├── streamlit_app.py         # Main file: Streamlit UI and connection to the backend logic.
├── requirements.txt         # List of Python dependencies for deployment.
└── README.md                # This document.
