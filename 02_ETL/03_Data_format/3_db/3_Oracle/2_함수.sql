-- * 함수
-- 1) 단일행 함수 : 단일 행에서만 적용 가능하고 행별로 하나의 결과를 리턴
-- 2) 다중행 함수 : 복수의 행을 조작하여 행의 그룹당 하나의 결과를 리턴 (예: count())

-- => 단일행 함수 : 문자함수, 숫자함수, 날짜함수, 변환함수, 일반함수
-----------------------------------------------------
-- 문자함수

-- dual 테이블 : 오라클 자체에서 값을 확인하기위한 용도로 제공하는 테이블
select * from dual;

-- initcap : 단어를 기준으로 첫 문자만 대문자로 나머지는 소문자로 변환하는 함수
select initcap('python specialist') from dual;
select initcap('pythonspecialist') from dual;

-- lower : 전체를 소문자로 만드는 함수
select lower('PYTHON SPECIALIST') from dual;
-- upper : 전체를 대문자로 만드는 함수
select upper('python specialist') from dual;

-- length : 문자열 길이수를 반환하는 함수
select length('python specialist') from dual;
select length('파이썬전문가') from dual;

-- concat : 두 문자열을 연결하여 반환
select concat('파이썬','전문가') from dual;

-- substr : substr([문자열],[시작인덱스],[출력할글자수]) 
-- => 문자열을 기준으로 시작인덱스에서 끝인덱스의 문자열 반환 (문자열의 시작인덱스는 1부터)
select substr('파이썬전문가',1,3) from dual;
select substr('파이썬전문가',2,4) from dual;
-- instr : instr([문자열],[찾고자하는문자열])
-- => 문자열을 기준으로 찾고자하는 문자열의 인덱스 반환
select instr('파이썬전문가','전') from dual;
select instr('파이썬전문가','정') from dual; -- 매치가되는 문자열이 없으면 0을 반환한다.

-- rpad/lpad : 주어진 자릿수만큼 오른쪽(rpad)/왼쪽이 지정한 문자열을 채운다.
-- rpad/lpad([문자열],[채울자리수],[채울문자])

select rpad('홍길동',10,'*') from dual; -- 한글은 2개씩 자리차지한다.
select lpad('홍길동',10,'*') from dual;

-- Q] 직원테이블에서 이름 10자리 중 나머지 오른쪽은 '-'로 채우고 
--    급여 10자리 중 나머지 왼쪽은 '*'로 채워서 출력하시오.
select rpad(first_name,10,'-') as name, lpad(salary,10,'*') as salary
from employees;

-- ltrim/rtrim/trim : 문자열을 기준으로 제거할 문자를 각각 왼쪽, 오른쪽, 양쪽으로 제거
-- ltrim/rtrim/trim([문자열],[제거할문자열]) => 제거할 문자열 기본값은 공백문자
select ltrim('    파이썬 전문가    ') as name from dual;
-- 별칭을 지정할 때 as를 생략할 수 있다.
select rtrim('    파이썬 전문가    ') name from dual;
select trim('    파이썬 전문가    ') name from dual;

select ltrim('파이썬전문가파이썬','파이썬') name from dual;
select rtrim('파이썬전문가파이썬','파이썬') name from dual;
-- trim 함수는 양쪽 공백문자만 제거 할 수 있다. 
-- 인자가 1개이기때문에 아래코드는 에러가 발생한다.
-- select trim('파이썬전문가파이썬','파이썬') name from dual;

-- replace
select replace('PythonSpecialist','Python','BigData') from dual;
select replace('Python Specialist',' ','') from dual; -- 공백문자 제거

-- translate([원본문자열],[매칭문자열],[변환문자열])
select translate('1234abcd','abcd','ABC') from dual;

select translate('hello world!!!','hw','HW') from dual;
select translate('hello world!!!','!','?') from dual;

select translate('$100','$','') from dual; -- 변환할 문자가 없다면 null로 반환
select translate('$100','$',' ') money_num from dual;
select translate('$1,000,000','$,',' ') money from dual;

-- Q] 직원테이블에서 이름을 이름 그대로, 소문자로, 첫글자만 대문자로, 모두 대문자로 출력해보세요
select first_name, lower(first_name), initcap(first_name), upper(first_name)
from employees;

select first_name from employees;
select lower(first_name) from employees;
select initcap(first_name) from employees;
select upper(first_name) from employees;

-- Q] 직원테이블에서 이름이 'austin'인 직원의
--    이름을 이름 그대로, 소문자로, 첫글자만 대문자로, 모두 대문자로 출력해보세요
--    검색을 소문자로 할것
select last_name, lower(last_name), initcap(last_name), upper(last_name)
from employees
where lower(last_name) = 'austin';

-- ltrim 심화
select ltrim('JavaSpecialist','Java') name from dual;
-- 제거할 문자열의 문자의 순서는 고려하지않는다.
select ltrim('JavaSpecialist','Jav') name from dual;
-- 제거는 제거하지못하는 문자를 최초 발견할 때까지 제거한다.
select ltrim('JavaSpecialist','avJ') name from dual;
select ltrim('JavaSpecialist','vJa') name from dual;

-- Q] 직무 아이디가 it_prog인 (반드시 소문자로 검색해야함!) 사원의
--    이름의 앞에 3자리만 출력하고 나머지자리는 * 출력하며
--    salary는 전체 10자리중 오른쪽 출력하고 나머지는 * 출력한다.
select
rpad (substr(first_name, 1,3), length(first_name),'*') as name, 
lpad (salary,10,'*') as salary
from employees
where lower(job_id) = 'it_prog';

----------------------------------------------------------------
-- 숫자함수

-- 반올림 : round
select round(45.923,2), round(45.923,0), round(45.923,-1)
from dual;

-- 올림 : ceil
select ceil(7.3) from dual;
select ceil(8.12357) from dual;

-- 버림 : floor
select floor(7.845984) from dual;
select floor(5.9) from dual;

-- 절삭 : trunc([데이터],[자리수]), 자리수만큼 데이터의 값을 절삭
select trunc(45.923,2), trunc(45.923), trunc(45.923,-1)
from dual;

-- to_date([날짜스트링],[포맷])
select to_date('2022-12-20','YYYY-MM-DD') as dt from dual;
-- 'MM' => 월을 기준으로 절삭한다
-- trunc함수를 응용하여 매월 첫째날을 구한다
select trunc(to_date('2022-12-20','YYYY-MM-DD'),'MM') as dt from dual;

-- Q] trunc함수를 응용하여 2022년 첫째날을 구한다.
select trunc(to_date('2022-12-20','YYYY-MM-DD'),'YYYY') as dt from dual;

-- DD로 절삭하면 일단위로 절삭할 날짜가 없으므로 동일값을 반환한다.
select trunc(to_date('2022-12-20','YYYY-MM-DD'),'DD') as dt from dual;
-- DAY로 절삭하면 그 주의 첫번째 일요일을 반환한다.
select trunc(to_date('2022-12-23','YYYY-MM-DD'),'DAY') as dt from dual;
select trunc(to_date('2022-12-31','YYYY-MM-DD'),'DAY') as dt from dual;

-- 절대값
select abs(-1000) abs_num from dual;
-- 제곱값
select power(2,3) power_num from dual;
-- 제곱근
select sqrt(100) sqrt_num from dual;
-- 나머지
select mod(10,3) mod_num from dual;

---------------------------------------------------------------
-- 날짜함수

-- SYSDATE : 현재의 날짜를 반환(YY/MM/DD)
select sysdate today from dual;

-- SYSTIMESTAMP : 현재의 날짜와 시간을 반환
select systimestamp from dual;

-- Q] 부서번호가 60인 사원의 이름과 현재까지 근무한 주를 'Weeks' 열 이름으로 출력
select first_name, (sysdate-hire_date)/7 as Weeks
from employees
where department_id = 60;

-- MONTHS_BETWEEN : 두 날짜 사이의 월 수를 반환
-- 월로 나눈결과를 반환
select first_name, sysdate, hire_date, 
months_between(sysdate,hire_date) as workmonth
from employees
where first_name = 'Diana';

-- ADD_MONTHS : 기준일에 월을 더함
select first_name, hire_date, ADD_MONTHS(hire_date,1)
from employees
where first_name = 'Diana';

-- Q] 위 예제를 활용하여 Diana가 입사 후 200개월이 지난 날짜를 구하세요.
select first_name, hire_date, ADD_MONTHS(hire_date,200)
from employees
where first_name = 'Diana';

-- NEXT_DAY : 돌아오는 가장 최근 요일 날짜
select sysdate, next_day(sysdate,'월') from dual;
select sysdate, next_day(sysdate,'금') from dual;

-- LAST_DAY : 해당 날이 포함된 월의 마지막 날짜
select sysdate, last_day(sysdate) from dual;

-- Q] 1월부터 12월까지 마지막날을 출력하세요.
select 
to_char(last_day(to_date('01','MM')), 'dd') as "1",
to_char(last_day(to_date('02','MM')), 'dd') as "2",
to_char(last_day(to_date('03','MM')), 'dd') as "3",
to_char(last_day(to_date('05','MM')), 'dd') as "5",
to_char(last_day(to_date('06','MM')), 'dd') as "6",
to_char(last_day(to_date('07','MM')), 'dd') as "7",
to_char(last_day(to_date('08','MM')), 'dd') as "8",
to_char(last_day(to_date('09','MM')), 'dd') as "9",
to_char(last_day(to_date('10','MM')), 'dd') as "10",
to_char(last_day(to_date('11','MM')), 'dd') as "11",
to_char(last_day(to_date('12','MM')), 'dd') as "12"
from dual;

-------------------------------------------------------------------
-- 변환함수
-- 암시적 형 변환
-- number <-> character <-> date

select first_name from employees
where department_id = 40; -- <= 숫자타입

select first_name from employees
where department_id = '40'; -- <= 문자타입이지만 암시적 형변환이 일어난다

select first_name from employees
where hire_date = '03/06/17'; -- <= 문자타입이지만 암시적 형변환이 일어난다

select '5500.00' - 4000 from dual;
-- 하지만! 서식이 들어간 데이터는 암묵적 형 변환이 되지않는다.
select '$5500.00' - 4000 from dual; -- 에러

--select ltrim('$5500.00','$') - 4000 
--from dual;
select first_name from employees
where hire_date = '03년 6월 17일'; -- 에러

select first_name from employees
where hire_date = '03/06/17';

-- 명시적 형 변환
-- TO_CHAR : 문자(날짜)열에 날짜포맷을 적용하여 문자로 변환, TO_CHAR([날짜],[날짜포맷])
select first_name, to_char(hire_date,'MM/YY') as HiredMonth
from employees
where first_name = 'Steven';

select first_name, to_char(hire_date,'YYYY"년" MM"월" DD"일"') as HiredMonth
from employees
where first_name = 'Steven';

select first_name, to_char(hire_date,'YYYY-MM-DD') as HiredMonth
from employees
where first_name = 'Steven';

-- TO_CHAR : 문자(숫자)열에 날짜포맷을 적용하여 문자로 변환, TO_CHAR([숫자],[숫자포맷])
-- ex) $999,999 <- 숫자는 9로 표시
-- 포맷보다 변환숫자의 길이가 큰 경우에는 '#'으로 표기된다.
select to_char(2000000,'$999,999') salary from dual; -- '#' 출력
select to_char(2000000,'$9999,999') salary from dual;

-- 앞에 0으로 padding하고싶은경우 
-- 목표 금액의 자리수를 고려하여 표현하고 싶은 경우
select to_char(2000000,'$009,999,999') salary from dual;

-- 소수점이하 자리에 대한 포맷이 없다면 그 값은 삭제된다.
select to_char(2000000.45,'$009,999,999') salary from dual;
-- 소수점 처리
select to_char(2000000.45,'$009,999,999.99') salary from dual;

-- 지역국가화폐기호 사용 ('L' 기호 사용)
select to_char(2000000,'L9,999,999') salary from dual;

-- Q] 직원테이블에 이름이 David인 이름, 성, 급여 
--    salary1열에 15.23% 인상율은 15% 인상된 금액을
--   다음과 같은 형식($1,466,85)을 적용된 인상금액을 salary2열에 출력하세요
select first_name, last_name, salary, salary*0.15 salary1, 
to_char(salary*0.1523,'$9,999.99') salary2
from employees
where first_name = 'David';

-- 원하는 날짜 포맷으로 검색하기
select first_name, hire_date
from employees
where hire_date = TO_DATE('2003/06/17','YYYY/MM/DD');

-- TO_DATE : 문자를 날짜 타입으로 변경
-- Q] 2003년6월17일에 입사한 직원이름, 입사일을 출력하세요 ('2003년6월17일'이 검색조건)
select first_name, hire_date
from employees
where hire_date = TO_DATE('2003년06월17일','YYYY"년"MM"월"DD"일"');

-- Q] 날짜타입이 아래와 같이 출력되도록 직원이름, 입사일을 출력하세요.
--   '2003-06-17'
select first_name, TO_CHAR(hire_date,'YYYY-MM-DD') as hire_date
from employees;

-- NULL 변환 .. 결측치처리
-- NVL
-- NVL([원본값],[null이면 변환되는 값]) <= 원본값이 null이 아니면 원본값을 반환
select nvl(1000,100) from dual;
select nvl(null,100) from dual;

select commission_pct from employees;
select nvl(commission_pct,0) from employees;

select first_name, salary, nvl(commission_pct,0) commission_pct,
salary+(salary*(nvl(commission_pct,0))) as total_salary
from employees;

-- NVL2
-- NVL2([원본값],[null이 아니면 변환되는 값],[null이면 변환되는 값]) 
select nvl2(1.2, 1000*0.2, 0) from dual;

select first_name, salary, nvl(commission_pct,0) commission_pct,
nvl2(commission_pct, salary+(salary*commission_pct), salary) as total_salary
from employees;

-- COALESCE([값또는구문1],[값또는구문2] ...) : null이 아닌 첫번째 인자의 값을 선택
-- 예) 고객데이터베이스에서 연락가능한 번호를 추출하고자 할 때
-- 선택가능한 값 중 (휴대폰, 집전화, 회사번호) 우선순위를 정하여 
-- 널이 아닌 값을 추출하고자 할 때 유용
select coalesce('010-123-4567',null,null) from dual;
select coalesce(null,'070-123-4567',null) from dual;
select coalesce(null,null,'02-123-4567') from dual;

-- Q] 위 예제를 coalesce함수를 사용해서 풀어보세요.
select first_name, salary, nvl(commission_pct,0) commission_pct,
coalesce(salary+(salary*commission_pct), salary) as total_salary
from employees;

-- Q] 보너스가 650달러보다 작거나 보너스가 없는 사원들에게 상품권을 지급하려고한다.
--    해당 사원들의 이름과 보너스를 출력하세요. (coalesce 함수 사용할 것)
--   (76개 행이 출력됨)
select first_name,
coalesce(salary*commission_pct,0) as bonus
from employees
where coalesce(salary*commission_pct,0) < 650;

-- LNNVL : LNNNVL(구문) 구문의 결과가 false 또는 unknown이면 true를 반환
-- 조건의 반대의 경우에대해 검색하고 싶을 때 활용
select first_name,
coalesce(salary*commission_pct,0) as bonus
from employees
where LNNVL(salary*commission_pct >= 650);

-- DECODE : DECODE(Column or expression, search1, result
--                                       [search2, result2, ...]

-- 첫번째값과 두번째값이 같다면 세번째값을 반환해준다
select decode('java','java','백엔드 언어') as language from dual;

select decode('java','java','백엔드 언어'
                    ,'html','프론트엔드 언어'
                    ,'python','데이터사이언스 언어'
                    ) as language_j from dual;
                    
select decode('html','java','백엔드 언어'
                    ,'html','프론트엔드 언어'
                    ,'python','데이터사이언스 언어'
                    ) as language_h from dual;
                    
select decode('python','java','백엔드 언어'
                    ,'html','프론트엔드 언어'
                    ,'python','데이터사이언스 언어'
                    ) as language_p from dual;

-- 매치되는 검색문자열이 없다면 null을 반환한다
select decode('css','java','백엔드 언어'
                    ,'html','프론트엔드 언어'
                    ,'python','데이터사이언스 언어'
                    ) as language_c from dual;
                    
-- default값은 제일 마지막에 정의한다 (search 문자열없이)
select decode('css','java','백엔드 언어'
                    ,'html','프론트엔드 언어'
                    ,'python','데이터사이언스 언어'
                    ,'기타언어'
                    ) as language from dual;
                    
-- Q] 직원테이블에서 직무 ID, 급여, 그리고 급여 인상율을 출력한다.
--    급여인상율은 직무 id가 IT FROG, FI MGR, FI ACCOUNT에 따라 
--    각각 10, 15, 20% 인상율을 적용한다.
select job_id, salary,
    decode(job_id,'IT_PROG',salary+(salary*0.1)
                ,'FI_MGR',salary+(salary*0.15)
                ,'FI_ACCOUNT',salary+(salary*0.2)
                ,salary)
                as revised_salary
from employees;

-- CASE ~ WHEN ~ THEN
select job_id, salary,
    case job_id when'IT_PROG' then salary+(salary*0.1)
                when'FI_MGR' then salary+(salary*0.15)
                when'FI_ACCOUNT' then salary+(salary*0.2)
                else salary
    end as revised_salary
from employees;

-- 개별조건 적용시
select job_id, salary,
    case when job_id = 'IT_PROG' then salary+(salary*0.1)
         when job_id ='FI_MGR' then salary+(salary*0.15)
         when job_id ='FI_ACCOUNT' then salary+(salary*0.2)
         else salary
    end as revised_salary
from employees;

-- 중첩함수 사용하기
-- 함수1(함수2(함수3))
-- step1
select add_months(hire_date,6)-- 입사 후 6개월
from employees
order by hire_date;
-- step2
-- 입사 후 6개월 그 주 금요일 출력
select next_day(add_months(hire_date,6),'금') as cal_day
from employees
order by hire_date;
-- step3
-- 입사 후 6개월 그 주 금요일의 날을 'YYYY-MM-DD' 형식으로 출력
select to_char(next_day(add_months(hire_date,6),'금'),'YYYY-MM-DD') as cal_day
from employees
order by hire_date;

-- Q] 직원 이름별 급여, 입사년도, 입사한 날의 요일, 급여 인상액을 출력하시오.
--    출력포맷참고
--    급여 인상액은 다음과 같다
--    > 근속년도가 10년 이상이면 10%인상
--    > 근속년도가 5년 이상이면 5%인상
--    > 5년 미만은 인상액 없음
select first_name, salary, 
       to_char(hire_date,'YYYY"년" "입사"') as year,
       to_char(hire_date,'DAY') as day,
    case when ((sysdate-hire_date)/365) >= 10 then to_char(salary+(salary*0.1),'$999,999')
         when ((sysdate-hire_date)/365) >= 5 then to_char(salary+(salary*0.15),'$999,999')
         when ((sysdate-hire_date)/365) < 5 then to_char(salary+(salary*0.2),'$999,999')
         else to_char(salary,'$999,999')
    end as revised_salary
from employees;

-- 집합연산자
-- UNION : 두개 이상의 질의결과를 합치는 연산 (중복되는결과를 포함)
select employee_id, first_name
from employees
where hire_date like '04%'
union
select employee_id, first_name
from employees
where department_id = 20;

-- UNION ALL (합집합, 중복된 값도 포함)
select employee_id, first_name
from employees
where hire_date like '04%'
union all
select employee_id, first_name
from employees
where department_id = 20;

-- INTERSECT (교집합)
select employee_id, first_name
from employees
where hire_date like '04%'
intersect
select employee_id, first_name
from employees
where department_id = 20;

-- MINUS (차집합)
select employee_id, first_name
from employees
where hire_date like '04%'
minus
select employee_id, first_name
from employees
where department_id = 20;

select employee_id, first_name
from employees
where department_id = 20
minus
select employee_id, first_name
from employees
where hire_date like '04%';

