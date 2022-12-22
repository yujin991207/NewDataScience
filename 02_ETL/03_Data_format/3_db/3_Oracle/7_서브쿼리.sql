-- �������� : ������ �� ���� �������踦 Ȱ���Ͽ� 
--          ��ø�� ������ �ۼ��� �ϳ��� �˻������ �ڵ����� �ϼ�

-- Nancy�� �޿����� ���� �޿��� �޴� ����� �̸��� �޿��� ���
select salary
from employees
where first_name = 'Nancy';

select first_name, salary 
from employees
where salary > 12008;

-- ���������� ���� : ������ ��������, ������ ��������
-- ��������Ȱ�� (������ �������� �̿�)
select first_name, salary 
from employees
where salary > (select salary
                from employees
                where first_name = 'Nancy');

-- where ���ǿ� ���� ���ͷ����� ����ؾ� �ϳ� ������(������)�� ���� ��Ī�� �ǹǷ� ���� �߻�      
select salary from employees where first_name = 'David'; -- 3���� ��                
select first_name, salary 
from employees
where salary > (select salary
                from employees
                where first_name = 'David');
                
-- ������ ��������
-- ANY/ALL
-- ANY : �ϳ��� �����ϴ� ���� / ALL : ��� ���� �����ϴ� ����
-- > any : ���� ���� ������ ū ���� (min����)
-- < any : ���� ū ������ ���� ���� (max����)

-- > all : ���� ū ������ ū ���� (max����)
-- < all : ���� ū ������ ���� ���� (min����)
select first_name, salary 
from employees
where salary > any(select salary
                from employees
                where first_name = 'David'); -- 4800, 9500, 6800
                
-- IN�� ���������� Ȱ�� : ����� � ���� ������ Ȯ��
-- step1 : �˻� ������ Ȯ��
select department_id from employees where first_name = 'David'; -- 60, 80, 80
-- step2
select first_name, department_id, job_id
from employees
where department_id in (
                        select department_id
                        from employees 
                        where first_name = 'David'
                        );
                        
-- Q] 20�� �μ��� �ٹ��ϴ� ����� ��պ��� ���� �޿��� ���� ����� �̸��� �޿��� ����ϼ���
select first_name, salary
from employees
where salary > (
                select avg(salary)
                from employees
                where department_id = 20);

-- ��ȣ�������� : ���������� ���̺��� ������������ ���Ǵ� ����
-- �ڽ��� ���� �μ��� ��պ��� ���� �޿��� �޴� ����� �̸��� �޿��� ����Ѱ���.
select first_name, salary
from employees a
where salary > (
                select avg(salary)
                from employees b
                where b.department_id = a.department_id);
                
-- select ������ �������� ��� -> Scalar Sub Query
-- Select ������ Join�� ������ ����Ͽ� Join�� ��� ������ ����
-- ��Ȳ�� ���� Join���� ���� ������ ���̱� ������ ��� (��, �׻� ������ ���� ���� �ƴ�)
select first_name, department_name
from employees e join departments d on (e.department_id = d.department_id)
order by first_name;

-- Scalar Sub Query �̿�
select first_name,(select department_name
                   from departments d
                   where d.department_id = e.department_id) department_name
from employees e
order by first_name;

-- �ζ��� ��
-- from ���� �����ϴ� ��������. from ������ ���̺� �Ǵ� �䰡 �� �� ����
-- ���������� �������� ���� �� �� �ֱ⶧���� �ζ��� ��� Ī��

-- Q] �޿��� ���� ���� �޴� ���� 10�� ����� �̸��� �޿��� ���
select first_name, salary
from(
    select first_name, salary
    from employees
    order by salary desc
)
where rownum between 1 and 10;