from data_functions import get_data
from csv_functions import file

# Scraping data from index.hr
data = get_data()

# Triggering function to create/update CSV file with scraped data
file(data)
