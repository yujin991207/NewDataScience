-- 서브쿼리 : 쿼리의 각 절에 의존관계를 활용하여 
--          중첩된 쿼리를 작성해 하나의 검색결과를 자동으로 완성

-- Nancy의 급여보다 많은 급여를 받는 사원의 이름과 급여를 출력
select salary
from employees
where first_name = 'Nancy';

select first_name, salary 
from employees
where salary > 12008;

-- 서브쿼리의 유형 : 단일행 서브쿼리, 다중행 서브쿼리
-- 서브쿼리활용 (단일행 서브쿼리 이용)
select first_name, salary 
from employees
where salary > (select salary
                from employees
                where first_name = 'Nancy');

-- where 조건에 단일 리터럴값을 사용해야 하나 복수개(다중행)의 값이 매칭이 되므로 에러 발생      
select salary from employees where first_name = 'David'; -- 3개의 값                
select first_name, salary 
from employees
where salary > (select salary
                from employees
                where first_name = 'David');
                
-- 다중행 서브쿼리
-- ANY/ALL
-- ANY : 하나라도 만족하는 조건 / ALL : 모든 것을 만족하는 조건
-- > any : 가장 작은 값보다 큰 조건 (min조건)
-- < any : 가장 큰 값보다 작은 조건 (max조건)

-- > all : 가장 큰 값보다 큰 조건 (max조건)
-- < all : 가장 큰 값보다 작은 조건 (min조건)
select first_name, salary 
from employees
where salary > any(select salary
                from employees
                where first_name = 'David'); -- 4800, 9500, 6800
                
-- IN을 서브쿼리에 활용 : 목록의 어떤 값과 같은지 확인
-- step1 : 검색 조건을 확인
select department_id from employees where first_name = 'David'; -- 60, 80, 80
-- step2
select first_name, department_id, job_id
from employees
where department_id in (
                        select department_id
                        from employees 
                        where first_name = 'David'
                        );
                        
-- Q] 20번 부서에 근무하는 사원의 평균보다 많은 급여를 버는 사원의 이름과 급여를 출력하세요
select first_name, salary
from employees
where salary > (
                select avg(salary)
                from employees
                where department_id = 20);

-- 상호연관쿼리 : 메인쿼리의 테이블이 서브쿼리에도 사용되는 형식
-- 자신이 속한 부서의 평균보다 많은 급여를 받는 사원의 이름과 급여를 출력한것임.
select first_name, salary
from employees a
where salary > (
                select avg(salary)
                from employees b
                where b.department_id = a.department_id);
                
-- select 절에서 서브쿼리 사용 -> Scalar Sub Query
-- Select 절에서 Join의 조건을 명시하여 Join할 대상 범위를 줄임
-- 상황에 따라서 Join보다 좋은 성능을 보이기 때문에 사용 (단, 항상 성능이 좋은 것은 아님)
select first_name, department_name
from employees e join departments d on (e.department_id = d.department_id)
order by first_name;

-- Scalar Sub Query 이용
select first_name,(select department_name
                   from departments d
                   where d.department_id = e.department_id) department_name
from employees e
order by first_name;

-- 인라인 뷰
-- from 절에 적용하는 서브쿼리. from 절에는 테이블 또는 뷰가 올 수 있음
-- 서브쿼리도 독립적인 뷰라고 볼 수 있기때문에 인라인 뷰라 칭함

-- Q] 급여를 가장 많이 받는 상위 10위 사원의 이름과 급여를 출력
select first_name, salary
from(
    select first_name, salary
    from employees
    order by salary desc
)
where rownum between 1 and 10;