from bs4 import BeautifulSoup
import urllib.request

html = urllib.request.urlopen('https://movie.naver.com/movie/sdb/rank/rmovie.nhn')
soup = BeautifulSoup(html, 'html.parser')

# width = "14" => 1번째 열, 영화 순서
ranks = soup.findAll('img', attrs={'width':'14'})
# class = "tit3" => 2번째 열, 영화 이름부분 순서대로 조회
tags = soup.findAll('div', attrs={'class':'tit3'})
# class = "arrow" => 3번째 열, 영화 평점부분(등락) 순서대로 조회
up_downs = soup.findAll('img', attrs={'class':'arrow'})
# class = "range ac" => 4번째 열, 등락폭을 영화 순위대로 조회
ranges = soup.findAll('td', attrs={'class':'range ac'})

f = open('movie_rank_test.csv', 'w', encoding='utf-8')
f.write('rank, movie_title, range, up_downs\n')
i = 0

# ['alt'] => 순위, ['title'] => 영화이름, ranges[i] => 영화 등락폭부분, ['alt'] => 영화 등락부분
while i < len(ranks)-1:
    print('{0}, {1}, {2}, {3}'.format(int(ranks[i]['alt']), tags[i].a['title'], ranges[i].string, up_downs[i]['alt']))
    f.write('{0}, {1}, {2}, {3}\n'.format(int(ranks[i]['alt']), tags[i].a['title'], ranges[i].string, up_downs[i]['alt']))
    i += 1
f.close()

