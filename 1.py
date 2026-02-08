import os

password="2341sldfosaf@l2308234"
github_token="ghp_87654321abcdefghijklmnopqrstuvwxyz"
# 触发 GitHub Secret Scanning 告警
github_token = "ghp_87654321abcdefghijklmnopqrstuvwxyz1234567890"
# 旧版格式（gho_/ghu_/ghs_ 开头也会触发）
github_old_token = "gho_1234567890abcdefghijklmnopqrstuvwxyz1234"

# 精准匹配 GitHub PAT 规则：ghp_ + 40位字符（共43位）
github_token = "ghp_87654321abcdefghijklmnopqrstuvwxyz1234"

# 精准匹配 AWS Access Key 规则：AKIA + 16位字符
aws_access_key_id = "AKIA1234567890ABCD"

# 精准匹配 Google API Key 规则：AIzaSy + 33位字符
google_api_key = "AIzaSyB9N9HxXj67890abcdefghijklmnopqrstuvwx"

token="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"
