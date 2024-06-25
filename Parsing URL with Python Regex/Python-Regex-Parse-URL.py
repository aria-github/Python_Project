
import re



url_regex = re.compile(r'(https?)://(www\.[A-za-z-]{2,256}\.[a-z]{2,6})([-a-zA-Z0-9@:%_\+.~#?&//=]*)')

match = url_regex.search("https://www.my-website.com/bio?data=blah&dog=yes")



print(f"Protocol: {match.group(1)}")
# Protocol: https

print(f"Domain: {match.group(2)}")
# Domain: www.my-website.com

print(f"Everything Else: {match.group(3)}")
# Everything Else: /bio?data=blah&dog=yes



print(match.groups())
# ('https', 'www.my-website.com', '/bio?data=blah&dog=yes')

print(match.group())
# https://www.my-website.com/bio?data=blah&dog=yes