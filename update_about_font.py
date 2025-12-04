
file_path = r"c:\git\my_portfolio\index.html"

# The content currently in the file (without lead class)
old_content_snippet = """                <div class="about-info">
                  <p>
                    <span class="title-s">이름: </span> <span>양성욱</span>
                  </p>
                  <p>
                    <span class="title-s">직무: </span> <span>안전관리자 / AI &amp; 데이터 분석가</span>
                  </p>
                  <p>
                    <span class="title-s">이메일: </span> <span>didtjddnr1@gmail.com</span>
                  </p>
                  <p>
                    <span class="title-s">GitHub: </span> <span>https://yangsungukk.github.io/</span>
                  </p>
                  <p>
                    <span class="title-s">자격증: </span> <span>산업안전기사, 정보통신기사, ISO45001 심사원</span>
                  </p>
                </div>"""

# The new content (with lead class)
new_content_snippet = """                <div class="about-info">
                  <p class="lead">
                    <span class="title-s">이름: </span> <span>양성욱</span>
                  </p>
                  <p class="lead">
                    <span class="title-s">직무: </span> <span>안전관리자 / AI &amp; 데이터 분석가</span>
                  </p>
                  <p class="lead">
                    <span class="title-s">이메일: </span> <span>didtjddnr1@gmail.com</span>
                  </p>
                  <p class="lead">
                    <span class="title-s">GitHub: </span> <span>https://yangsungukk.github.io/</span>
                  </p>
                  <p class="lead">
                    <span class="title-s">자격증: </span> <span>산업안전기사, 정보통신기사, ISO45001 심사원</span>
                  </p>
                </div>"""

with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# Normalize line endings to be sure
content = content.replace('\r\n', '\n')
old_content_snippet = old_content_snippet.replace('\r\n', '\n')
new_content_snippet = new_content_snippet.replace('\r\n', '\n')

if old_content_snippet in content:
    new_content = content.replace(old_content_snippet, new_content_snippet)
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(new_content)
    print("Successfully updated About section font size.")
else:
    print("Could not find the target content to replace.")
    # Debugging: print a part of the file to see what's wrong
    start_marker = '<div class="about-info">'
    idx = content.find(start_marker)
    if idx != -1:
        print("Found start marker at index", idx)
        print("Next 500 chars:")
        print(content[idx:idx+500])
    else:
        print("Could not find start marker.")
