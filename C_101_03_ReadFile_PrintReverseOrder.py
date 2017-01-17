# ������� �������������� ��� ��������� ��������������� �����������
# �' ����
# ������ ������������
# worked with Python 2.7.10
# @ Tasos Chatzipapadopoulos

'''

�������� 6� ���������� �������
������������� 3 / ������ 101
�� ������� ��������� ��� ������ Python, �� ����� �� ������� �� 
������ �� ����� ���� �������, �� ��������� �� ����������� ��� 
���� ������ ��� ��� �������� �� ������ �� ��� ���� ������, 
��� ������� ��� ������� ���� ���������� �����.  
      
'''

# ���������� �������� �� ������
f = open ('testFile.txt', 'r')

# pythonic way
for line in reversed(open("testFile.txt").readlines()):
    print line

# ����������� ����������
lines = []
for line in f :
    lines.append(line)

# ����� ������ ����������
for i in range(len(lines)-1,-1,-1):
    print lines[i]
    

# �� ����� ������� ����������    
lines.reverse()
for line in lines :
    print line
    
f.close()

# ������� �� ������
lines.reverse()
o = open('outputFile.txt', 'w')
for i in range(len(lines)-1,-1,-1):
    o.write(lines[i])
o.close()
