# re.sub(pattern,replace,string)
import re
print(re.sub(r"India","Australia","My favorite country is India "))
# My favorite country is Australia (India is replaced by Australia)

# If the pattern is not found, the string is returned unchanged
print(re.sub(r"Modi","XiJiping","The Chineese President is XiJiping"))
# The Chineese President is XiJiping