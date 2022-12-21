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
