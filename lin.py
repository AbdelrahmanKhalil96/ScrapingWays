# import web driver
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import parameters
from parsel import Selector
import time
import csv
# specifies the path to the chromedriver.exe
driver = webdriver.Chrome('E:\Sel\chromedriver.exe')


def validate_field(field):  # if field is present pass if field:pass
    # if field is not present print text else:
    if field:
        return str(field)
    else:
        field = 'No results'
        return str(field)


# driver.get method() will navigate to a page given by the URL address
driver.get('https://www.linkedin.com')
try:
    driver.find_element_by_id('reload-button').click
    time.sleep(1)
except:
    print('loaded normally')
# locate email form by_class_name
username = driver.find_element_by_id('session_key')

driver.implicitly_wait(3)
# send_keys() to simulate key strokes
username.send_keys(parameters.linkedin_username)
driver.implicitly_wait(8)
# locate password form by_class_name
password = driver.find_element_by_id('session_password')

# send_keys() to simulate key strokes
password.send_keys(parameters.linkedin_password)
driver.implicitly_wait(5)
# locate submit button by_xpath
log_in_button = driver.find_element_by_xpath('//*[@type="submit"]')
time.sleep(2)
# .click() to mimic button click
log_in_button.click()

driver.implicitly_wait(5)
# iUh30 gBIQub qLRx3b tjvcx
time.sleep(3)
driver.get('https://www.google.com')
driver.find_element_by_link_text('English').click()
# foot = driver.find_element_by_id('foot')
# t = [foot.find_element_by_xpath(
#     '//tr[@jsname="TeSSVd"]').text.replace("\n", ",").strip()]
# page = driver.find_element_by_xpath("//div[@aria-label='Page 2']/div[@class='SJajHc NVbCr' and text()='Any time']")
search = driver.find_element_by_name('q')
search.send_keys(parameters.search_query)
search.send_keys(Keys.RETURN)
driver.implicitly_wait(1)
parent = driver.find_elements_by_class_name('yuRUbf')
linkedin_urls = []
for cl in parent:
    parentwithLink = cl.find_element_by_tag_name('a').get_attribute("href")
    linkedin_urls.append(parentwithLink)
    print(parentwithLink)
# driver.find_elements_by_class_name('iUh30.gBIQub.qLRx3b.tjvcx')
# linkedin_urls = [str(url.text).replace(
#     ' › ', '/in/').replace('\'\',', " ")for url in linkedin_urls]
# print("Page 1 : ")
driver.find_element_by_link_text("Next").click()
driver.implicitly_wait(1)
# linkedin_urls2 = driver.find_elements_by_class_name(
#     'iUh30.gBIQub.qLRx3b.tjvcx')
# linkedin_urls2 = [str(url.text).replace(' › ', '/in/').replace('\'\',', " ")
#                   for url in linkedin_urls2]
parent = driver.find_elements_by_class_name('yuRUbf')
i = 0
for cl in parent:
    parentwithLink = cl.find_element_by_tag_name('a').get_attribute("href")
    linkedin_urls.append(parentwithLink)
    print(parentwithLink)
# print("Page 2 : ")

# print(linkedin_urls2)

#linkedin_urls = linkedin_urls+linkedin_urls2

# For loop to iterate over each URL in the list
userData = {}
# defining new variable passing two parameters
writer = csv.writer(open(parameters.file_name, 'w'))

# writerow() method to the write to the file object
writer.writerow(['Name', 'Brief', 'Countery', 'University', 'URL'])

for linkedin_url in linkedin_urls:
    # get the profile URL
    driver.get(linkedin_url)

    # add a 5 second pause loading each URL
    driver.implicitly_wait(5)
# //*[starts-with(@class, "pv-top-card-section__name")]/text()
    # assigning the source code for the webpage to variable sel
    sel = Selector(text=driver.page_source)

    try:

        name = sel.xpath(
            '//*[starts-with(@class, "inline t-24 t-black t-normal break-words")]/text()').extract_first()
        if name:
            name = name.strip()
        brief = sel.xpath(
            '//*[starts-with(@class, "mt1 t-18 t-black t-normal break-words")]/text()').extract_first()
        if brief:
            brief = brief.strip()
        countery = sel.xpath(
            '//*[starts-with(@class, "t-16 t-black t-normal inline-block")]/text()').extract_first()
        if countery:
            countery = countery.strip()
        university = sel.xpath(
            '//*[starts-with(@class, "text-align-left ml2 t-14 t-black t-bold full-width lt-line-clamp lt-line-clamp--multi-line ember-view")]/text()').extract_first()
        if university:
            university = university.strip()
        userData[i] = {
            'Name': name,
            'Brief': brief,
            'Countery': countery,
            'University': university,
            'LinkedIn_URL': driver.current_url
        }
        i += 1
        time.sleep(0.5)
        # validating if the fields exist on the profile
        name = validate_field(name)
        job_title = validate_field(brief)
        company = validate_field(countery)
        college = validate_field(university)
        location = validate_field(driver.current_url)
        # writing the corresponding values to the header
        try:

            writer.writerow([name,
                             job_title,
                             company,
                             college,
                             linkedin_url])
        except UnicodeEncodeError:
            print([name, job_title, company, college, linkedin_url])
            writer.writerow([name.encode('utf-8'),
                             job_title.encode('utf-8'),
                             company.encode('utf-8'),
                             college.encode('utf-8'),
                             linkedin_url.encode('utf-8')])
    except AttributeError:
        print('error')
# terminates the application
driver.quit()
print(userData)
# function to ensure all key data fields have a value
