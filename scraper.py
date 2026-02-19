import requests
from bs4 import BeautifulSoup
import json
import logging
    
# Configuring Logging
logging.basicConfig(
    filename='scraper.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

def scrape_jobs():
    logging.info("Beginning the scraping process...")
    url = 'https://pythonjobs.github.io/' 
    jobs_data = []

    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status() 
        logging.info(f"Successfully connected to the website: {url}")
        soup = BeautifulSoup(response.text, 'html.parser')
        job_boxes = soup.find_all('div', class_='job')

        for job in job_boxes:
            title = job.find('h1').text.strip() if job.find('h1') else 'No Title'
            company_icon = job.find('i', class_='i-company')
            company = company_icon.parent.text.strip() if company_icon else 'No Company'
            location_icon = job.find('i', class_='i-globe')
            location = location_icon.parent.text.strip() if location_icon else 'No Location'
            link_tag = job.find('a', class_='go_button')

            if link_tag and 'href' in link_tag.attrs:
                job_url = 'https://pythonjobs.github.io' + link_tag['href']
            else:
                job_url = '#'
            
            jobs_data.append({
                'title': title,
                'company': company,
                'location': location,
                'url': job_url
            })
        
        logging.info(f"Scraped {len(jobs_data)} job offers.")

    except requests.exceptions.RequestException as e:
        logging.error(f"Error while fetching the page: {e}")

    except Exception as e:
        logging.error(f"Unexpected error: {e}")

    # Save to a JSON file
    try:
        with open('jobs.json', 'w', encoding='utf-8') as f:
            json.dump(jobs_data, f, ensure_ascii=False, indent=4)
        logging.info("Data successfully saved to jobs.json.")
        
    except IOError as e:
        logging.error(f"Error writing to file: {e}")

if __name__ == '__main__':
    scrape_jobs()
    print("Scraping completed! Check the scraper.log and jobs.json files.")