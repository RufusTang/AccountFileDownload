#-*- coding: UTF-8 -*-

import urllib2
import os

def DownloadFile(code):

    url = r'http://quotes.money.163.com/service/zcfzb_%s.html'%(code)
    FileSavePath = 'zcfzb%s.csv'%(code)
    f = urllib2.urlopen(url)
    data = f.read()
    with open(FileSavePath, "wb") as TempFile:
        TempFile.write(data)

    url = r'http://quotes.money.163.com/service/lrb_%s.html'%(code)
    FileSavePath = 'lrb%s.csv'%(code)
    f = urllib2.urlopen(url)
    data = f.read()
    with open(FileSavePath, "wb") as TempFile:
        TempFile.write(data)

    url = r'http://quotes.money.163.com/service/xjllb_%s.html'%(code)
    FileSavePath = 'xjllb%s.csv'%(code)
    f = urllib2.urlopen(url)
    data = f.read()
    with open(FileSavePath, "wb") as TempFile:
        TempFile.write(data)


def main():
    f = open("StockCode.txt", "r")
    lines = f.readlines()
    for line in lines:
        print line.strip('\n')
        DownloadFile(line.strip('\n'))

if __name__ == '__main__':
    main()
