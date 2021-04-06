import time
from selenium import webdriver

url = 'https://bmstu.health/schedule'
options = webdriver.ChromeOptions()
options.add_argument('--headless')
browser = webdriver.Chrome(chrome_options=options)
browser.get(url)
time.sleep(5)

dates_obj = browser.find_element_by_class_name('dates-row')
dates_obj_arr = dates_obj.find_elements_by_xpath('//*[@id="app-schedule-full"]/div/div[4]/div[1]/div')
dates_def = []
for date_obj in dates_obj_arr:
    date = dates_obj.text
    dates_def.append(date)

dates_def = dates_def[0].split('\n')
xpath_def = '//*[@id="app-schedule-full"]/div/*'
objects = browser.find_elements_by_xpath(xpath_def)
count_obj = len(objects)
current_act = ''
doctors = []
for i in range(count_obj):
    class_obj = objects[i].get_attribute('class')
    if class_obj == 'schedule-row':
        doctor = dict.fromkeys(['name', 'spec', 'office', 'dates'], 'None')
        doctor['name'] = objects[i].find_element_by_class_name('doctorname').text
        doctor['spec'] = current_act

        dates_obj = browser.find_elements_by_xpath(xpath_def[:-1] + 'div[' + str(i + 1) + ']/*')
        dates = dict.fromkeys(dates_def)
        for j in range(1, len(dates_obj)):
            date_class = dates_obj[j].get_attribute('class')
            if date_class == 'item true':
                doctor['office'] = dates_obj[j].text.split('\n')[0]
                data_part = ''.join(dates_obj[j].text.split('\n')[1:])
                if data_part == None or data_part == '':
                    data_part = 'По записи'
                dates[dates_def[j - 1]] = data_part
        doctor['dates'] = dates
        doctors.append(doctor)

    elif class_obj == 'activity-name':
        current_act = objects[i].text

with open('doctors.csv', 'w', encoding = 'utf-8') as file:
    i = 1
    for doctor in doctors:
        file.write(str(i) + ';')
        file.write(doctor['name'] + ';')
        file.write(doctor['spec'] + ';')
        file.write(doctor['office'] + '\n')
        i += 1
    file.close()

with open('dates.csv', 'w', encoding = 'utf-8') as file:
    i = 1
    count = 1
    for doctor in doctors:
        if doctor['dates'] != 'None':
            for date, status in doctor['dates'].items():
                if status != None:
                    file.write(str(count) + ';' + str(i) + ';' + date + ';' + status + '\n')
                    count += 1
        i += 1
    file.close()
