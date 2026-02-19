# Python Job Scraper & Django Viewer

A simple project combining web scraping in pure Python utilizing BeautifulSoup and requests. This project also includes a presentation layer built in the Django framework.

## Features

1. **Scraper (Python + BeautifulSoup):**
   - Extracts current job listings from the target website.
   - **Audit Logging:** Utilizes the built-in `logging` module to track script execution, record data extraction events, and log potential connection errors (which it outputs to `scraper.log`).
   - **Error Resilience:** Implements `try-except` blocks to handle unexpected issues or changes without crashing.
   - Exports clean, structured data to a `jobs.json` file.

2. **Web Viewer (Django):**
   - A lightweight Django application acting purely as a presentation layer (View + Template).
   - Automatically reads and formats data from the scraped JSON file.
   - Features UI built with simple HTML/CSS.

##  How to Run Locally

**1. Clone the repository and install dependencies:**

```bash
git clone https://github.com/MSZM0/Job-Scraper.git
cd Job-Scraper
pip install django requests beautifulsoup4
```

**2. Run the scraper (Optional):**

You can run the scraper to download the latest data, but a `jobs.json` file is also provided for demonstration purposes.

```bash
python scraper.py
```

**3. Start the Django server:**
To view the data in your browser, start the local development server:

```bash
python manage.py runserver
```

Finally, open your web browser and navigate to `http://127.0.0.1:8000/`.
