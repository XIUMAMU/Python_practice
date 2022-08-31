# str의 /로 구분된 각각의 옵션 추출 및 PZ 옵션의 값을 x, y, w, h 로 구분하여 표기

# PS = 121
# PZ.x = 2
# PZ.y = 3
# PZ.w = 100
# PZ.h = 100
# FILE = test.py

# 입력된 문자열
str = "/PS:121 /PZ:2,3,100,100 /FILE=test.py"

str_sp = str.split("/")            # 옵션별로 구분

ps = str_sp[1].split(":")         # PS의 값 추출
pz = str_sp[2]                  # PZ의 값 추출
file = str_sp[3].split("=")       # FILE의 값 추출

pz_sp = pz[3: ].split(",")       # PZ의 값을 x, y, w, h 구분하여 추출

print(f"{file[0]} = {file[1]}\n{ps[0]} = {ps[1]}\n{pz[ :2]}.X = {pz_sp[0]}\n{pz[ :2]}.Y = {pz_sp[1]}\n{pz[ :2]}.W = {pz_sp[2]}\n{pz[ :2]}.H = {pz_sp[3]}")
