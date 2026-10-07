import os

from addition import add
from subtraction import subtract
from multiplication import multiply

commit = os.environ.get("GITHUB_SHA", "local")[:7]

html = f"""<!doctype html>
<html>
<head>
  <meta charset="utf-8">
  <title>Calculator App</title>
  <style>
    body {{ font-family: Arial, sans-serif; max-width: 450px; margin: 40px auto; }}
    p {{ font-size: 20px; border-bottom: 1px solid #ddd; padding: 10px; }}
  </style>
</head>
<body>
  <h1>Calculator App</h1>
  <p>10 + 20 = {add(10, 20)}</p>
  <p>20 - 10 = {subtract(20, 10)}</p>
  <p>10 x 20 = {multiply(10, 20)}</p>
  <small>Deployed by GitHub Actions | Commit: {commit}</small>
</body>
</html>
"""

os.makedirs("site", exist_ok=True)
with open("site/index.html", "w") as f:
    f.write(html)
print("Built site/index.html")