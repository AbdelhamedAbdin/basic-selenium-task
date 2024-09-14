from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd

# Initialize the Chrome WebDriver
driver = webdriver.Chrome()

# Open the webpage
url = 'https://www.scrapethissite.com/pages/forms'
driver.get(url)

# Locate the table element
table = driver.find_element(By.TAG_NAME, "table")

# Find the table body (tbody) and rows (tr)
tbody = table.find_element(By.TAG_NAME, "tbody")
list_of_tr = tbody.find_elements(By.TAG_NAME, "tr")

# Extract the headings from the first row (tr)
heading = list_of_tr[0]
table_headings = heading.find_elements(By.TAG_NAME, "th")

# Extract column names
columns = [th.text for th in table_headings]

# Create an empty DataFrame with column names
new_data = pd.DataFrame(columns=columns)

# Extract row data (skip the first row which is header)
row_results = list_of_tr[1:]

# Iterate over each row and append to the DataFrame
for row_result in row_results:
    # Extract cell data for this row
    row_data = [td.text for td in row_result.find_elements(By.TAG_NAME, "td")]

    # Append the row data as a new row in the DataFrame
    new_data.loc[len(new_data)] = row_data

# Save the DataFrame to a CSV file
new_data.to_csv("team.csv", index=False)

# Close the browser when done
driver.quit()
