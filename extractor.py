from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import requests
import os


def download_all_papers(base_url, save_dir, driver_path):
    driver = webdriver.Chrome(driver_path)
    driver.get(base_url)

    if not os.path.exists(save_dir):
        os.makedirs(save_dir)

    # wait for the select element to become visible
    wait = WebDriverWait(driver, 30)
    res = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".note_content_title")))
    print("Successful load the website!")
    # parse the results
    divs = driver.find_elements_by_class_name('title_pdf_row')
    num_papers = len(divs)
    print(num_papers)
    for index, paper in enumerate(divs):
        name = paper.find_element_by_class_name('note_content_title').text
        name.replace("/","-")
        link = paper.find_element_by_class_name('note_content_pdf').get_attribute('href')
        print('Downloading paper {}/{}: {}'.format(index+1, num_papers, name))
        download_pdf(link, os.path.join(save_dir, name))
    driver.close()



def download_all_papers_iclr(base_url, save_dir, driver_path):
    driver = webdriver.Chrome(driver_path)
    driver.get(base_url)

    if not os.path.exists(save_dir):
        os.makedirs(save_dir)

    # wait for the select element to become visible
    print("Successful load the website!")
    # parse the results
    divs = driver.find_elements_by_css_selector('.maincard.narrower.Poster')
    num_papers = len(divs)
    print(num_papers)
    for index, paper in enumerate(divs):
        name = paper.find_element_by_class_name('maincardBody').text
        print(len(name))
        link = paper.find_elements_by_css_selector('.btn.btn-default.btn-xs.href_PDF')[0].get_attribute('href')
        print(link.replace("forum","pdf"))
        print('Downloading paper {}/{}: {}'.format(index+1, num_papers, name))
        download_pdf(link.replace("forum","pdf"), os.path.join(save_dir, name))
    driver.close()


def download_all_papers_nips(base_url, save_dir, driver_path):
    driver = webdriver.Chrome(driver_path)
    driver.get(base_url)

    if not os.path.exists(save_dir):
        os.makedirs(save_dir)

    # wait for the select element to become visible
    print("Successful load the website!")
    # parse the results
    divs = driver.find_elements_by_css_selector('.maincard.narrower.Poster')
    num_papers = len(divs)
    print(num_papers)
    driver2 = webdriver.Chrome(driver_path)
    for index, paper in enumerate(divs):
        name = paper.find_element_by_class_name('maincardBody').text
        name = name.replace("/","-")
        name = name.replace("(","")
        name = name.replace(")","")
        print(len(name))
        link = paper.find_elements_by_css_selector('.btn.btn-default.btn-xs.href_PDF')[0].get_attribute('href')
        driver2.get(link)
        link = driver2.current_url+'.pdf'
        print('Downloading paper {}/{}: {}'.format(index+1, num_papers, name))
        download_pdf(link, os.path.join(save_dir, name))
    driver.close()
    driver2.close()


def download_all_papers_icml(base_url, save_dir, driver_path):
    driver = webdriver.Chrome(driver_path)
    driver.get(base_url)

    if not os.path.exists(save_dir):
        os.makedirs(save_dir)

    # wait for the select element to become visible
    print("Successful load the website!")
    # parse the results
    divs = driver.find_elements_by_css_selector('.maincard.narrower.Poster')
    num_papers = len(divs)
    print(num_papers)
    for index, paper in enumerate(divs):
        name = paper.find_element_by_class_name('maincardBody').text
        name = name.replace("/","-")
        name = name.replace("(","")
        name = name.replace(")","")
        print(len(name))
        link = paper.find_elements_by_css_selector('.btn.btn-default.btn-xs.href_PDF')[0].get_attribute('href')
        # print(link.replace("forum","pdf"))
        linklist = link.split("/")
        link.replace(".html",linklist[-1].replace("html","pdf"))
        print('Downloading paper {}/{}: {}'.format(index+1, num_papers, name))
        download_pdf(link.replace("forum","pdf"), os.path.join(save_dir, name))
    driver.close()




def download_pdf(url, name):
    r = requests.get(url, stream=True)

    with open('%s.pdf' % name, 'wb') as f:
        for chunck in r.iter_content(1024):
            f.write(chunck)
    r.close()


if __name__ == '__main__':
    NIPS16 = 'https://openreview.net/group?id=NIPS.cc/2016/Deep_Learning_Symposium'
    ICLR17 = 'https://openreview.net/group?id=ICLR.cc/2017/conference'
    ICLR18 = 'https://iclr.cc/Conferences/2018/Schedule?type=Poster'
    NIPS17 = 'https://nips.cc/Conferences/2017/Schedule?type=Poster'
    ICML17 = 'https://icml.cc/Conferences/2017/Schedule?type=Poster'
    driver_path = '/usr/lib/chromium-browser/chromedriver'
    save_dir_nips = '/home/surya/Desktop/Papers/NIPS-2017'
    save_dir_iclr = '/home/surya/Desktop/Papers/ICLR-2018'
    save_dir_nips16 = '/home/surya/Desktop/Papers/NIPS-2016'
    save_dir_iclr17 = '/home/surya/Desktop/Papers/ICLR-2017'
    save_dir_icml17 = '/home/surya/Desktop/Papers/ICML-2017'
    # download_all_papers(NIPS, save_dir_nips, driver_path)
    # download_all_papers_iclr(ICLR18, save_dir_iclr, driver_path)
    # download_all_papers(ICLR17,save_dir_iclr17,driver_path)
    # download_all_papers_nips(NIPS17,save_dir_nips,driver_path)
    # download_all_papers(NIPS16,save_dir_nips16,driver_path)
    download_all_papers_icml(ICML17,save_dir_icml17,driver_path)