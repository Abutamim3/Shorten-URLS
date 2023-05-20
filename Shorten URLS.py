


# Developed by Abdulrahman Alharbi


import urllib.request

def tiny_url(url):
    apiurl = 'http://tinyurl.com/api-create.php?url='
    tinyurl = urllib.request.urlopen(apiurl + url).read()
    return tinyurl.decode("utf-8")

full_url = 'https://www.youtube.com/watch?v=CrqQAPA2gGU'
short_url = tiny_url(full_url)

print('original url:\n', full_url)
print()
print('Shortened url:\n', short_url)

print ("Developed by Abdulrahman Alharbi")