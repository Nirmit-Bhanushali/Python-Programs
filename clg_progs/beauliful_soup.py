# .  Write a Python program using BeautifulSoup to read a simple HTML file (provide the HTML string in the code) and extract the text content of all <a> (anchor) tags present in the file.

from bs4 import BeautifulSoup
html_content = """
<!DOCTYPE html>
<html>
<head>
    <title>Sample HTML Page</title>
</head>
<body>
    <h1>Welcome to My Website</h1>
    <p>Here are some useful links:</p>
    
    <a href="https://www.google.com">Google Search</a>
    <a href="https://www.github.com">GitHub Repository</a>
    <a href="https://www.stackoverflow.com">Stack Overflow</a>
    
    <div class="footer">
        <a href="/about">About Us</a>
        <a href="/contact">Contact Page</a>
    </div>
</body>
</html>
"""

soup = BeautifulSoup(html_content, 'html.parser')

# Find all anchor tags
anchor_tags = soup.find_all('a')

# Extract and print text from each anchor tag
print("Text content of all anchor tags:\n")
for tag in anchor_tags:
    print(tag.text)
