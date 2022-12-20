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
select * from employees;
-- 직원테이블에서 ....... email (전체 소문자, 전체 대문자, 첫글자만 대문자)
select lower(email), upper(email), initcap(email)
from employees;
-- manager_id가 114번이고 급여가 2700이상인 사원의 급여를 10% 인상해서 출력
select salary, salary+(salary * 0.1)
from employees
where manager_id = 114 and salary >= 2700;
-- 부서번호가 80인 사원의 이름과 현재까지 근무한 주를 새로운열에 출력하세요
select first_name, (sysdate-hire_date)/7 as Weeks
from employees
where department_id = 80;

select hire_date
from employees
where hire_date like '05/10%';

-- job_id FI_ACCOUNT 이고 입사월을 기준으로 1년이 지난 년도/월/일과 , 
-- 입사월, 이름을 출력하세요
-- 그리고 입사를 먼저한 순으로 출력하세요

-- job_id 'clerk'가 들어간 직무에 해당하는 사원의 이름, 직무id를
-- 이름순대로 출력
select first_name, job_id
from employees
where job_id like '%CLERK%'
order by first_name;

-- 보너스를 받지않은 사람들의 급여를 300달러 추가지급하고
-- 이름, 추가지급된급여를 출력
select first_name,commission_pct,salary+300 as total_salary
from employees
where commission_pct is null
order by total_salary desc;

-- 첫글자와 마지막글자빼고 * 출력 (A포함)
-- 현재기준으로 10년 일한 사원이름과 hire_date, 직무아이디를 출력하세요
select first_name, hire_date, job_id, round((sysdate-hire_date)/365,0) as works_month
from employees
where (sysdate-hire_date)/365 > 10;

-- 핸드폰번호에서 . 을 - 변경 가운데 세자리를 *로 출력
select replace(rpad(substr(phone_number,1,4), length(phone_number),'*'),'.','-')
from employees;
