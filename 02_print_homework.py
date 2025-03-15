part1 = "QYTANG"
part2 = "'day"
part3 = "2014-9-28"

print(f"{part1}{part2} {part3}")

##################################################################


word = " scallywag"

sub_word = word[3:7]

print(sub_word)

##################################################################

word = "Python"
new_word1 = word[1:]
new_word2 = word[0]
new_word_last = new_word1 + '-' + new_word2 + 'y'
print(new_word_last)

##################################################################

department1 = 'Security'
department2 = 'Python'
depart1_m = 'cq_bomb'
depart2_m = 'qinke'
COURSE_FEES_SEC = 456789.123456
COURSE_FEES_Python = 1234.3456

line1 = "Department1 name:%-15sManager:%-15sCOURSE_FEES:%-15sThe End!" % (department1, depart1_m, COURSE_FEES_SEC)
line2 = "Department2 name:%-15sManager:%-15sCOURSE_FEES:%-15sThe End!" % (department2, depart2_m, COURSE_FEES_Python)

line1 = f'Department1 name:{department1:<15}Manager:{depart1_m:<15}COURSE_FEES:{COURSE_FEES_SEC:<15}The End!'
line2 = f'Department2 name:{department1:<15}Manager:{depart1_m:<15}COURSE_FEES:{COURSE_FEES_SEC:<15}The End!'

line1 = "Department1 name:{dep:<15}Manager:{depart1_m:<15}COURSE_FEES:{COURSE_FEES_SEC:<15.2f}The End!".format(
    dep=department1, depart1_m=depart1_m, COURSE_FEES_SEC=COURSE_FEES_SEC
)
day = '星期三'
line3 = '今天是星期几{day3}'.format(day3=day)
line2 = "Department2 name:{department2:<15}Manager:{depart2_m:<15}COURSE_FEES:{COURSE_FEES_Python:<15.2f}The End!".format(
    department2=department2, depart2_m=depart2_m, COURSE_FEES_Python=COURSE_FEES_Python
)

length = len(line1)
print('=' * length)
print(line1)
print(line2)
print(line3)
print('=' * length)

##################################################################


import re

str1 = 'Port-channel1.189 192.168.189.254 YES CONFIG up'

ip_pattern = r'\b(?:[0-9]{1,3}\.){3}[0-9]{1,3}\b'
match = re.search(ip_pattern, str1)

ip_address = match.group()
print(f"{'接口':<8}:Port-channel1.189")
print(f"{'IP地址':<8}:{ip_address}")
print(f"{'状态':<8}:up")
