# html_to_pdf
A set of scripts to facilitate converting HTML files to PDF.

## html_cleaner.py
When converting html to pdf, line breaks such as <hr> do not convert well. Image line breaks also do not convert. This script walks through a directory tree and looks for .html files. When it finds one it scans it for a given piece of html and removes lines containing that html.

Specifically, the script re-writes the file line by line except for the lines containing the specified html tags. It is important to ensure you have the right text encoding as a result to avoid losing special characters. Currently the script is set to use UTF-8 which works well.

One small issue with this is html files that contain data in the same line as the line break tags. Since the whole line is "removed" the html formatting can be broken by this script. It is important to check the html format before running this script to avoid unwanted formatting changes or data loss.

## html_to_pdf.py
This script walks through a specified directory and looks for .html files. When it finds one it uses the pdfkit module to convert the file to a .pdf.

## url_scraper.py
This script scrapes a given url for all lines that contain .html and writes them to a file. This is used to generate a list of URLs from an index page that can then be used to download all .html files.