from google import google
num_page = 100
search_results = google.search("site:gov.co filetype:pdf listado cedula telefono", num_page)

for result in search_results:
    print result.link
