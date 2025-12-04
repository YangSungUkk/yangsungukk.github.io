lines_to_remove = range(570, 681) # 570 to 680 inclusive
file_path = r"c:\git\my_portfolio\index.html"

with open(file_path, 'r', encoding='utf-8') as f:
    lines = f.readlines()

# lines are 0-indexed in python list, but my range is 1-indexed
# so line 570 is index 569
start_index = 570 - 1
end_index = 680 - 1

# Keep lines before start_index and after end_index
new_lines = lines[:start_index] + lines[end_index+1:]

with open(file_path, 'w', encoding='utf-8') as f:
    f.writelines(new_lines)

print(f"Removed lines {570} to {680}")
