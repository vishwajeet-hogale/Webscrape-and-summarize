# Webscrape-and-summarize
## Project Overview
This Git repository hosts an application designed to scrape articles from the "livemint" website and provide concise summaries using the state-of-the-art T5 model. The application is inspired by the InShorts app concept, aiming to deliver condensed yet informative insights from lengthy articles.
## Components
### Text Summarization Script (t5_textsumm.py):
* The script utilizes the newspaper3k module to extract articles from the "livemint" website.
* It employs the T5 model (specifically, the t5-small variant) for summarizing the extracted articles.
* The summarization process involves preprocessing the text, tokenizing it, and generating a concise summary using the T5 model.
* The summarized articles are then stored in a Pandas DataFrame.

### Web Scraping Script (livemint.py):
* This script defines a function (webscrape()) to extract articles from the "livemint" website and store them in a CSV file (livemint.csv).
* It is triggered by a button in the Flask web application to update the dataset with the latest articles.

### Flask Web Application (app.py):
* The Flask app defines a simple web interface with two main functionalities: web scraping and article summarization.
* Users can trigger the web scraping process to update the dataset with the latest articles from "livemint."
* Users can generate article summaries using the T5 model on the existing dataset.
* The application displays the original title, text, and the generated summary for each article.

### HTML Templates (templates/index.html):
* The HTML templates define the structure of the web interface.
* There are sections for displaying the original articles, triggering web scraping, and generating summaries.

## Usage
### Environment Setup:
* Ensure that the required Python packages are installed. You can install them using pip install -r requirements.txt.

### Run the Flask App:
* Execute the Flask application by running python app.py in the terminal.
* Access the application in a web browser at http://localhost:5000.

### Web Scraping:
* Click the "Web Scrape" button to update the dataset with the latest articles from "livemint."

### Text Summarization:
* Click the "Generate Summary" button to initiate the text summarization process using the T5 model.
* The application will display the original title, text, and the generated summary for each article.

## Dependencies
* torch
* transformers
* pandas
* flask

## Note
* Ensure that the livemint.csv file is present in the project directory before running the application.
* The T5 model used in this project is t5-small. For larger datasets, consider using a larger T5 variant for better performance.

License
This project is licensed under the MIT License.
