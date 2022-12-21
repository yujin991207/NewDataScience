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
