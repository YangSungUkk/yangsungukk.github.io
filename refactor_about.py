
file_path = r"c:\git\my_portfolio\index.html"

new_content = """                <div class="about-info">
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

with open(file_path, 'r', encoding='utf-8') as f:
    lines = f.readlines()

# We want to replace lines 97 to 145 (1-based) -> indices 96 to 145 (exclusive of 145? no, inclusive of 144)
# Line 97 is index 96.
# Line 145 is index 144.
# So we replace lines[96:145] with the new content.

start_idx = 96
end_idx = 145

# Verify we are replacing the right thing
print("Replacing:")
print("".join(lines[start_idx:start_idx+5])) 
print("...")
print("".join(lines[end_idx-5:end_idx]))

# Construct new lines
# We need to make sure new_content has newlines
new_lines_list = [line + '\n' for line in new_content.split('\n')]

final_lines = lines[:start_idx] + new_lines_list + lines[end_idx:]

with open(file_path, 'w', encoding='utf-8') as f:
    f.writelines(final_lines)

print("Successfully refactored About section.")
