from datetime import datetime

now = datetime.now()

output = f"""
Run Test is Done

Date: {now.strftime('%Y-%m-%d')}
Time: {now.strftime('%H:%M:%S')}
"""

print(output)

with open("output.txt", "w") as f:
    f.write(output)
