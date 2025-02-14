import requests
from bs4 import BeautifulSoup
import re

topurl = ""

def getHeadings(url): 

    url = ""
    soup = BeautifulSoup(response.text, "html.parser")

    info = soup.find_all("a", class_=re.compile("px"))

    headings = []
    for i in range(len(info)): 
        tmpHeading = str(info[i])
        result = re.search("""href="/(.*)"><div""",tmpHeading)
        if result is None: 
            break
        headings.append(result.group(1))

    return headings

def getUnderHeadings(heading):
    
    url = topurl + heading

    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    info = soup.find_all("a", class_=re.compile("px"))

    underHeadings = []
    for i in range(len(info)): 
        tmpHeading = str(info[i])
        result = re.search("""href="/(.*)"><div""",tmpHeading)
        if result is None: 
            break
        underHeadings.append(result.group(1))

    return underHeadings

def getText(underHeading):

    url = topurl + underHeading
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")

    info = soup.find_all("div", class_=re.compile("accordion-item"))

    text = []
    for item in info: 
        text.append(item.text)

    return text

def getTextFiles(): 

    headings = getHeadings(topurl)
    for i in range(len(headings)): 
        print(f"Page {i} out of {len(headings)}")
        underHeadings = getUnderHeadings(headings[i])
        alltext = ""
        for j in range(len(underHeadings)):
            print(f"under heading {j} out of {len(underHeadings)}")
            text = getText(underHeadings[j])
            for item in text: 
                alltext += f"\n" + item

        with open(rf"INTERNETMEDICIN_TXT\test{i}.txt", 'w', encoding="utf-8") as textFile: 
            textFile.write(alltext)

#getTextFiles()