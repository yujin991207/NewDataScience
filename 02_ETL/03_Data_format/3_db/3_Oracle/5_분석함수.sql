----------------------------------------------------
-- 분석함수 : 데이터분석을 위한 다양한 기능 제공

-- RANK : 데이터의 우선순위를 결정 (중복순위 계산함) 
-- DENSE_RANK : 데이터의 우선순위를 결정 (중복순위를 계산하지않는다)
-- CUME_DIST : 최대값 1을 기준으로 분산된 값을 제공
-- PERCENT_RANK : 최대값 1을 기준으로 백분율(percent)값을 제공
--                => 첫번째 위치가 0부터 시작하고 두번째 row부터의 위치는
--                  (row의 rank-1 / 전체 row 개수 -1)
--                  rank를 기준으로 동일한 rank의 개수가 전체 대비 몇 % 인지로 해석
-- NTILE : ntile(n) 전체 데이터 분포를 앞에서부터 n개의 구간으로 나누어 표시

-- 문법
-- 분석함수 over([order by])
select * from employees;
select first_name, salary,
    rank() over (order by salary desc) as rank,
    dense_rank() over (order by salary desc) as dense_rank,
    round(cume_dist() over (order by salary desc),3) as cume_rank,
    round(percent_rank() over (order by salary desc),3) as percent_rank,
    ntile(3) over (order by salary desc) as ntile,
    rownum, -- 의사열(최초 테이블에 부여된 행번호)
    -- 검색결과에 따라 순차적으로 부여되는 행번호 (row_number)
    row_number() over (order by salary desc) as row_number 
    from employees;
    
-- ratio_to_report
-- 조회하는 값을 해당 컬럼 값의 백분율로 제공
-- 예) 매출
--     30 <- 0.3
--     50 <- 0.5
--     20 <- 0.2
select first_name, salary, 
round(ratio_to_report(salary) over (),4) as salary_ratio
from employees
where job_id = 'IT_PROG';

-- LAG / LEAD (이전/이후 값에 대한 검색)
-- LAG([열이름],[이전 이동수],[값이 없을 경우 반환값])
-- LEAD([열이름],[이후 이동수],[값이 없을 경우 반환값])
-- 직원아이디, 현재급여 다음으로 적은 급여, 현재 급여, 현재 급여보다 다음으로 높은 급여
select employee_id,
    lag(salary, 1,0) over (order by salary) as lower_sal,
    salary,
    lead(salary, 1,0) over (order by salary) as higher_sal
from employees
order by salary;
-- 결과 => 첫번째 열은 이전값이 없기때문에 0으로 반환해준다.

-- LISTAGG
-- LISTAGG([값, 구문], [구분자])
--      WITHIN GROUP(ORDER BY [열이름])
-- 기능 : 수집되는값을 구분자 join(연결)
select department_id, 
    listagg(first_name,', ') within group (order by hire_date) as names
from employees
group by department_id;

select * from employees;

-- PIVOT, UNPIVOT
-- table 생성
CREATE TABLE   sales_log(
  employee_id  NUMBER(6),
  week_id      NUMBER(2),
  week_day     VARCHAR2(10),
  quantity     NUMBER(8,2)
); 

INSERT INTO sales_log values(1101, 4, 'SALES_MON', 100);
INSERT INTO sales_log values(1101, 4, 'SALES_TUE', 150);
INSERT INTO sales_log values(1101, 4, 'SALES_WED', 80);
INSERT INTO sales_log values(1101, 4, 'SALES_THU', 60);
INSERT INTO sales_log values(1101, 4, 'SALES_FRI', 120);
INSERT INTO sales_log values(1102, 5, 'SALES_MON', 300);
INSERT INTO sales_log values(1102, 5, 'SALES_TUE', 300);
INSERT INTO sales_log values(1102, 5, 'SALES_WED', 230);
INSERT INTO sales_log values(1102, 5, 'SALES_THU', 120);
INSERT INTO sales_log values(1102, 5, 'SALES_FRI', 150);
COMMIT;

SELECT * FROM sales_log;

-- PIVOT : 행으로 나열된 여러개의 데이터를 공통의 속성으로 묶어 집계(평균, 합계 등)하고 열로 나타낸다.
-- 로그성 데이터(Long 포맷)을 분석용 데이터(Wide 포맷)로 전환하는 과정
-- 문법
-- select
-- from
-- pivot(
--     그룹함수(집계대상컬럼)
--     for [피벗기준컬럼]
--     in (피벗컬럼 나열)
-- )
-- where
-- order by
select *
from sales_log
pivot
(
    sum(quantity)
    for week_day in('SALES_MON' as sales_mon,
                    'SALES_TUE' as sales_tue,
                    'SALES_WED' as sales_wed,
                    'SALES_THU' as sales_thu,
                    'SALES_FRI' as sales_fri)
)
order by employee_id, week_id;
-- select * from sales_log;

-- table 생성
CREATE TABLE sales(
  employee_id  NUMBER(6),
  week_id      NUMBER(2),
  sales_mon    NUMBER(8,2),
  sales_tue    NUMBER(8,2),
  sales_wed    NUMBER(8,2),
  sales_thu    NUMBER(8,2),
  sales_fri    NUMBER(8,2)
);

INSERT INTO sales VALUES(1101, 4, 100, 150, 80,  60,  120);
INSERT INTO sales VALUES(1102, 5, 300, 300, 230, 120, 150);
COMMIT;

SELECT * FROM sales;

-- UNPIVOT :  여러개의 열으로 나열된 여러개의 데이터를 공통의 열로 묶어 (stack) 나열
-- 복합속성을 단일 속성으로 전환하는 과정
-- 문법
-- select
-- from
-- unpivot
-- (
--   [통합할 열의 이름 : 기준 데이터의 값을 나타내는 이름]
--   for [통합할 열의 이름 : 기준 데이터에서 나열된 열의 공통 특성을 나타내는 이름]
--   in ([기준데이터의 통합대상열1], [기준데이터의 통합대상열2] .... )
-- )
-- where
-- order by
select employee_id, week_id, week_day, quantity
from sales
unpivot
(
    quantity
    for week_day
    in(SALES_MON, SALES_TUE, SALES_WED, SALES_THU, SALES_FRI)
);

