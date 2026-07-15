strs = ["flower", "flow", "flight"]

longest_common_prefix = ""
strs.sort()
first_string = strs[0]
last_string = strs[-1]

for i in range(min(len(first_string), len(last_string))):
    if first_string[i] != last_string[i]:
        break
    longest_common_prefix += first_string[i]

print(longest_common_prefix)
