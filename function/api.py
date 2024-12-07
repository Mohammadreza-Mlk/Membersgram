
import subprocess, sys, os,time
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '.')))
sys.path.append("../Membersgram")
 
javascript_file = 'api.js'

# اجرای فایل جاوا اسکریپت
result = subprocess.run(['node', javascript_file], capture_output=True, text=True)

# نمایش خروجی
myCoins1 = result.stdout
print("Output:", myCoins1 )
 
time.sleep(10)


# اجرای فایل جاوا اسکریپت
result = subprocess.run(['node', javascript_file], capture_output=True, text=True)

# نمایش خروجی
myCoins2 = result.stdout
print("Output:", myCoins2 )
if myCoins2 > myCoins1:
    print("PASS")
 