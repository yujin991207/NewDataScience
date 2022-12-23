select * from employees;

-- �� �μ��� �ο� ���� ����϶�(�μ� ��ȣ�� ���� ������ ����)
select department_id, count(*)
from employees
where department_id is not null
group by department_id;

-- �μ��� ��� �޿��� ���� ū �μ��� ��ȣ�� ��� �޿��� ����϶�.
select department_id, avg(salary)
from employees
group by department_id
order by department_id;

-- �� �μ��� ������ �ο���, �� �μ��� �ο���, ��ü �ο����� ����϶�.
select department_id, job_id, count(*)
from employees
group by rollup(department_id, job_id);

-- �μ��� �ο��� 10�� �̻��� �μ��� ��ȣ�� �ο����� ����϶�.
select department_id ,count(*)
from employees
group by department_id
having count(*) >= 10;

-- �μ��� ���� ���� �޿��� ����϶�
select department_id, max(salary)
from employees
group by department_id;

-- 100�� �μ��� ������ ��ձ޿��� 100�� �μ� ��ü�� ��ձ޿��� ����϶�(union all�̿�)
select department_id, job_id, avg(salary)
from employees
where department_id = 100
group by department_id, job_id
union all
select department_id, null, avg(salary)
from employees
where department_id = 100
group by department_id;

-- grouping sets�̿�
select department_id, job_id, avg(salary)
from employees
where department_id = 100
group by grouping sets(department_id, job_id);

-- 50, 80, 100 �� ���� �μ��� ���� 5���� �̸�, �޿��� ����ѵ� 5�� �� ���� ���� �޿��� ����϶�
select rownum,department_id, first_name, salary
from employees
where department_id in(50,80,100) and rownum <= 5;

--�ӱ��� ���� ������ ��ũ�� �Ű� ��ũ������ ����Ͻÿ�. �̶�, �ߺ������� ����Ͻÿ�.
--select first_name, salary,
--    rank() over (order by salary desc) as rank,
select first_name, salary,
    rank() over (order by salary desc) as rank
from employees;

--�μ��� �ӱ��� ���� �� top 5�� ��� ()
select department_id, round(avg(salary),1) avg_sal, rank() over (order by round(avg(salary),1) desc) as rank_
from employees
group by department_id;

 --�޿��� ���� ������ ��ũ�� �Ű� �̸�, �޿�, �Ի���,��ũ�� ����϶�.
-- �̶� ���� �޿��� �޴� ��� �Ի����� ���� �̸� �� ���� ��ũ�� ��ġ�϶�
select first_name, salary, hire_date,
    rank() over (order by salary desc) as rank,
    row_number() over (order by salary desc) as real_rank
from employees
order by salary desc, hire_date;

-- ������ ����� , ����ϴµ� ...(Ǯ��������) �̸� ������ �޿��� ����������
--select department_id,
--    listagg(first_name,', ') within group (order by hire_date) as names
--from employees
--group by department_id;

select job_id,
    listagg(first_name||' '||last_name,', ') within group (order by salary desc) as names
from employees
group by job_id
having lower(job_id) like '%mk%';
--ratio_to_report�� �̿��ؼ�
--Hazel�� salary�� ��ü salary�� 2.28% �Դϴ�
--���·� ����Ͻÿ�
--select first_name, salary,
--round(ratio_to_report(salary) over (),4) as salary_ratio
--from employees
--where job_id = 'IT_PROG';

select first_name || '�� salary�� ��ü salary��' || to_char(round(ratio_to_report(salary) over(),4)*100,'0.99')||'%�Դϴ�'
from employees;

select * from employees;


--���ʽ��� ���� ���� ����� 10% �λ�
--���ʽ��� ���� ����� 5%�λ��� ���ּ��� �׸��� 'tot_sal' �̸����� ������ּ���
--������ ������������ �Ű��ּ���

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

-- Q5]  manager_id�� ���� ������ ������̹Ƿ� manager_id�� 0���� ��ġ����.
-- ���� �δ��� ���� �Ŵ��� ������ manager_id�� ����������� ����ϼ���.
-- ���� �δ��� ���� �Ŵ��� ���� ����ϰ� �ִ� ������ ���� ���� �������Դϴ�.
-- (nvl,count,group by, order by ���)
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
select distinct l.postal_code as �����ȣ
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
