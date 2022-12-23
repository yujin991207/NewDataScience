select * from employees;

-- 각 부서별 인원 수를 출력하라(부서 번호가 없는 직원은 제외)
select department_id, count(*)
from employees
where department_id is not null
group by department_id;

-- 부서별 평균 급여가 가장 큰 부서의 번호와 평균 급여를 출력하라.
select department_id, avg(salary)
from employees
group by department_id
order by department_id;

-- 각 부서의 직무별 인원수, 각 부서의 인원수, 전체 인원수를 출력하라.
select department_id, job_id, count(*)
from employees
group by rollup(department_id, job_id);

-- 부서의 인원이 10명 이상인 부서의 번호와 인원수를 출력하라.
select department_id ,count(*)
from employees
group by department_id
having count(*) >= 10;

-- 부서별 가장 높은 급여를 출력하라
select department_id, max(salary)
from employees
group by department_id;

-- 100번 부서의 직무별 평균급여와 100번 부서 전체의 평균급여를 출력하라(union all이용)
select department_id, job_id, avg(salary)
from employees
where department_id = 100
group by department_id, job_id
union all
select department_id, null, avg(salary)
from employees
where department_id = 100
group by department_id;

-- grouping sets이용
select department_id, job_id, avg(salary)
from employees
where department_id = 100
group by grouping sets(department_id, job_id);

-- 50, 80, 100 번 각각 부서별 직원 5명의 이름, 급여를 출력한뒤 5명 중 가장 높은 급여를 출력하라
select rownum,department_id, first_name, salary
from employees
where department_id in(50,80,100) and rownum <= 5;

--임금이 높은 순으로 랭크를 매겨 랭크순으로 출력하시오. 이때, 중복순위를 계산하시오.
--select first_name, salary,
--    rank() over (order by salary desc) as rank,
select first_name, salary,
    rank() over (order by salary desc) as rank
from employees;

--부서별 임금이 높은 순 top 5만 출력 ()
select department_id, round(avg(salary),1) avg_sal, rank() over (order by round(avg(salary),1) desc) as rank_
from employees
group by department_id;

 --급여가 높은 순으로 랭크를 매겨 이름, 급여, 입사일,랭크를 출력하라.
-- 이때 같은 급여를 받는 경우 입사일이 빠른 이를 더 높은 랭크에 배치하라
select first_name, salary, hire_date,
    rank() over (order by salary desc) as rank,
    row_number() over (order by salary desc) as real_rank
from employees
order by salary desc, hire_date;

-- 직무별 사원을 , 출력하는데 ...(풀네임으로) 이름 순서는 급여가 높은순으로
--select department_id,
--    listagg(first_name,', ') within group (order by hire_date) as names
--from employees
--group by department_id;

select job_id,
    listagg(first_name||' '||last_name,', ') within group (order by salary desc) as names
from employees
group by job_id
having lower(job_id) like '%mk%';
--ratio_to_report를 이용해서
--Hazel의 salary는 전체 salary의 2.28% 입니다
--형태로 출력하시오
--select first_name, salary,
--round(ratio_to_report(salary) over (),4) as salary_ratio
--from employees
--where job_id = 'IT_PROG';

select first_name || '의 salary는 전체 salary의' || to_char(round(ratio_to_report(salary) over(),4)*100,'0.99')||'%입니다'
from employees;

select * from employees;


--보너스를 받지 않은 사원은 10% 인상
--보너스를 받은 사원은 5%인상을 해주세요 그리고 'tot_sal' 이름으로 출력해주세요
--순서를 내림차순으로 매겨주세요

select first_name, NVL2(COMMISSION_PCT,salary*(COMMISSION_PCT+0.05),salary*1.1) tot_sal
from employees;
--select job_id, salary,
--    case job_id when'IT_PROG' then salary+(salary*0.1)
--                when'FI_MGR' then salary+(salary*0.15)
--                when'FI_ACCOUNT' then salary+(salary*0.2)
--                else salary
--    end as revised_salary // case when job_id = 'IT_PROG' then salary+(salary*0.1)
--from employees;
select first_name,
    case when COMMISSION_PCT is null then salary*1.1
         else salary*(COMMISSION_PCT+0.05)
    end as tot_sal
from employees;

-- to_char(2000000,'L9,999,999') salary from dual
select first_name,
    case when COMMISSION_PCT is null then to_char(salary*1.1*1273.69,'L9,999,999,999')
         else to_char(salary*(COMMISSION_PCT+0.05)*1273.69,'L9,999,999,999')
    end as tot_sal
from employees
order by tot_sal;

select * from job_history;
select * from employees;

select * from regions;
select * from countries;
select * from locations;

select *
from regions r
join countries c
on r.region_id = c.region_id;

-- Q5]  manager_id가 없는 직원은 사장님이므로 manager_id를 0으로 고치세요.
-- 업무 부담이 높은 매니져 순으로 manager_id와 담당직원수를 출력하세요.
-- 업무 부담이 높은 매니져 순은 담당하고 있는 직원이 가장 많은 직원순입니다.
-- (nvl,count,group by, order by 사용)
select first_name,
    case when commission_pct*salary is null then nvl(commission_pct*salary,'gift_card')
         --when commission_pct*salary < 2000 then coalesce(commission_pct,'gift_card')
    else commission_pct
    end as bonus
from employees;

select first_name, nvl(commission_pct,'gift_card')
from employees;

select * from employees;

select first_name, commission_pct*salary as bonus,
       decode(commission_pct*salary,null,'gift_card')
from employees;

-----------------------------------------------------
-- Q1]
select department_id
from
(select department_id, stddev(salary) as stdd
from employees
group by department_id
order by stdd)
where rownum = 1;


-- Q2]
select a.first_name, a.manager_id, b.first_name as manager_name
from employees a ,employees b
where a.manager_id = b.employee_id and a.employee_id = 103;

-- Q3]
select distinct l.postal_code as 우편번호
from employees e
join departments d
on e.department_id = d.department_id and e.department_id = 60
join locations l
on d.location_id = l.location_id and d.location_id = 1400;

-- Q4]
select first_name, salary
from employees
where rownum = 1
order by salary desc;

--select * from employees;
--select * from departments;
--select * from locations;
