# Internship-Day---3
Web scrapper for news headlines


The first thing to do is import 'requests' and 'beautifulsoup'. I didn't have them installed so i did it by opening the console and typing "pip install request" and "pip install bs4"
imoprt allows us to bring external modules and use them. "requests" is used to male HTTP request and "beautifulsoup" is used to parse HTML amd XML.
Then we "url" to store the URl or news site we ant to scrape.
request.get() allows to send HTTP GET request to the url, in "r" we store the response we get from the server.
If and else are used to figure out if the required conditions are met for execution.
Then we create a variable that holds the HTML structure(soup), r.text contains the raw content of the page.
We use the title=[] to create an empty list. soup.find('title') allows us to find the first tag in the page.
.get_text() allows us to extract only the text in the page.
append() add the text extracted to the list.
We then create a loop to go through all one by one, Then we extract and clean up the text inside.
Then we use titles.append() to add text to list, "open" creates the file.txt and we use "w" to use write mode or overwrite files.
then we use the print() to let the user know that the headlines are saved to text file.
