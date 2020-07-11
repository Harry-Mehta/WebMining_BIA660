#A: A Google search for the term "Tim Berners-Lee".
import requests
r = requests.get('https://www.google.com/search?q=tim+berners-lee&rlz=1C1SQJL_enUS879US879&oq=Tim+Berners-Lee&aqs=chrome.0.0l8.1831j0j7&sourceid=chrome&ie=UTF-8')
print(r.text)
print("\n")
print(r.status_code)
print("\n")
print(r.headers)

#B: A POST request to a website that does not accept POST requests.
import requests
r = requests.post('http://www.google.com')
print(r.text)
print("\n")
print(r.status_code)
print("\n")
print(r.headers)

#C: A request to a URL that does not exist.
import requests
r = requests.get('http://www.fakerequesttt.com')
print(r.text)
print("\n")
print(r.status_code)
print("\n")
print(r.headers)