# 목적: 분산데이터(여러 csv파일) 읽기
# 여러 파일을 읽고 쓸 수 있는 ...
# glob => 특정 경로에 있는 다수의 파일에 접근하려고 할 때 필요한 모듈이다.
import csv
import glob
import os
import sys

# 현재 경로의 '.' 표시
input_path = '.'

file_counter = 0

# glob.glob()인자에 지정한 패턴의 모든 파일을 반환
# os.path.join([디렉토리 경로],[문자열]) => 디렉토리 경로의 문자열을 연결 해준다.
# sales_* => sales_로 시작 하고 sales_ 문자 이후에 어떠한 문자도 매칭이 가능
for input_file in glob.glob(os.path.join(input_path,'sales_*')):
	row_counter = 1

	with open(input_file, 'r', newline='') as csv_in_file:
		filereader = csv.reader(csv_in_file)
		header = next(filereader)

		for row in filereader:
			row_counter += 1
	# print('{0!s}: \t{1:d} rows \t{2:d} columns'.format(\
	print('{0}: \t{1} rows \t{2} columns'.format(\
		os.path.basename(input_file), row_counter, len(header)))
	file_counter += 1
print('Number of files: {0:d}'.format(file_counter))