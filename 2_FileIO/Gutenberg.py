# A tiny downloader for files in the Project Gutenberg

import urllib2
import sys

def download(url, bookname):
    '''
    Takes a valid URL and downloads the content.
    Then creates a new file in the same folder using the
    provided bookname.
    '''

    print("Downloading %s" %url)
    book = urllib2.urlopen(url).read()
    with open(bookname, "wb") as outfile:
        outfile.write(book)
    print("Writting file %s" %bookname)
    print("Done!")

def main():
    print('All command line arguments: ',sys.argv)
    if len(sys.argv) == 3:
        url = sys.argv[1]
        bookname = sys.argv[2]
        download(url,bookname)
    else:
        print('Supply url and bookname')

if __name__ == "__main__":
    main()