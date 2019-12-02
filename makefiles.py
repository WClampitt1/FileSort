import os

for i in range(1, 10):
    for ext in ['.jpg', '.png', '.ipt', '.docx', '.pdf']:
        os.system('>' + str(i) + ext)
