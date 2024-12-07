javascript_file = 'test.js'

# اجرای فایل جاوا اسکریپت
result = subprocess.run(['node', javascript_file], capture_output=True, text=True)

# نمایش خروجی
print("Output:", result.stdout)
print("Error:", result.stderr)