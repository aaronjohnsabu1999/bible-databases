# Parse XML Bible databases to CSV (for import to SQLite DB Browser)

import csv
import requests
import xml.etree.ElementTree as ET

def parseXML(xmlfile):
    tree     = ET.parse(xmlfile)
    bible    = tree.getroot()
    verses   = []
    bookIter = 0

    for book in bible.findall('./b'):
        chapterIter = 1
        for chapter in book:
            verseIter = 1
            for verse in chapter:
                verses.append({'Book': bookIter, 'Chapter': chapterIter, 'Versecount': verseIter, 'verse': verse.text})
                verseIter += 1
            chapterIter += 1
        bookIter += 1

    return verses

def savetoCSV(newsitems, filename):
    fields = ['Book', 'Chapter', 'Versecount', 'verse']
    with open(filename, 'w') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames = fields)
        # writer.writeheader()
        writer.writerows(newsitems)

def main():
    xmlFiles = ["AMPBible_Database", "AKJVBible_Database", "CEVBible_Database", "ESVBible_Database", "GENBible_Database", "MSGBible_Database", "NASBBible_Database", "UKJVBible_Database"]
    for xmlFile in xmlFiles:
        verses = parseXML('./XML/' + xmlFile + ".xml")
        savetoCSV(verses, './CSV/' + xmlFile + '.csv')

if __name__ == "__main__":
    main()