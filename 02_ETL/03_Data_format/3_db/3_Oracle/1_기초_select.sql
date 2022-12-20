-- �ּ� : ù��° SQL��
select * from employees;
select first_name from employees where first_name = 'John';
select * from employees where first_name like '%a%';
select * from employees where salary > 4000;

-- ���� ����Ŭ ���� ���� Ȯ��
select * from v$version;

-- ������ �������� ���̺� ��� ��ȸ
select * from tabs;

-- �÷� �� �⺻ ���� ��ȸ
-- ���̺� �̸��� '�빮��'�� �Է��� ��!
-- cols => ���̺��� ��ü ��
SELECT * from cols
where table_name = 'employees';

SELECT * from cols
where table_name = 'EMPLOYEES';

-- select (Projection => �� ����)
select first_name, last_name, salary from employees;

-- data Ÿ��
-- YY/MM/DD �������� ������ (Default�� DD/MM/YY)
select first_name, hire_date, salary from employees;

-- ������ �켱����
-- 0.1 => �޿� �λ����, salary*0.1 => �λ� �޿�
select first_name, last_name, salary, salary+salary*0.1
from employees;

-- ������ ��, Null ǥ�� => ���ǵ������� ���� null�� ǥ�õȴ�.
select first_name, department_id, commission_pct
from employees;

-- �� ��Ī(alias) ����
select first_name as �̸�, salary �޿�
from employees;

-- ���� ���α׷����� ���̸��� �ν��ϱ� ���� �뵵�ε� �ݵ�� ����ؾ���!
select first_name, last_name, salary, salary+salary*0.1 as �޿��λ��
from employees;
-- �����ϸ� ���� ��Ī�� ��� ����
select first_name, last_name, salary, salary+salary*0.1 as raised_income
from employees;

-- ���ͷ�(literal) ���� ��Ʈ���� ���� ������
-- || => ���ڿ���
-- ''s salary is $' => 's salary is $�� ���
select first_name || ' ' || last_name || '''s salary is $' || salary
    as "employees imformation"
from employees;

-- �ߺ� ��� DISTINCT
select department_id from employees;
select distinct department_id from employees;

-- ROWNUM, ROWID �ǻ翭(Pseudo column)
-- ����Ŭ���� ���� �ε����� 1���� �����Ѵ�.
-- rowid�� ���ϰ����� ����, ���� �����ϰ� ���� ������ Ű (pk�ε� Ȱ�밡��)
-- rownum �˻������ ���Ͽ� 1���� ���� �ο��Ѵ�
select employee_id, first_name from employees;
select rowid, rownum, employee_id, first_name from employees;

-- ���� ���� (Selection) : where �������� ����
select first_name, last_name, hire_date
from employees
where last_name = 'King';

-- �� ������
select first_name, salary, hire_date
from employees
where salary >= 15000;

-- ��¥��
select first_name, salary, hire_date
from employees
where hire_date = '04/01/30'; -- �Ϲ��� ����ȯ�� �Ͼ�⶧���� ����

-- between ������ (between �������� and ������) ��������, ������ ����.
select first_name, salary
from employees
where salary between 1000 and 12000;

-- IN ������
select manager_id from employees;
-- Q] �������̺��� manager_id�� 101, 102 �Ǵ� 103�� ����id, �̸�, �޿�, �Ŵ���id�� ����ϼ���
-- => IN ������ ����ؼ� ����Ұ�
select employee_id, first_name, salary, manager_id
from employees
where manager_id in (101, 102, 103);

-- LIKE ������
-- & ��ȣ Ȱ��
select job_id from employees;

select first_name, last_name, job_id, department_id
from employees
where job_id like '%IT%';

-- Q] 2003�� 1��1�Ϻ��� 2003�� 12��31�� ���̿� �Ի��� ��� ����� �̸��� �Ի����� ����ϼ���
select first_name, hire_date
from employees
where hire_date like '03%';

-- '_'��ȣ Ȱ�� : '_' ������ �� ���ڿ� ��Ī
-- �̸����� �� ��° ���ڰ� 'A'�� ��� ����� �̸��� �̸����� ���
select first_name, email
from employees
where email like '_A%';

-- IS NULL ������ : null�� ���� ã�� ��
select first_name, manager_id
from employees
where manager_id is null;

-- �� ������
-- 1) and ������
-- Q] ���� id�� IT_PROG�̰� �޿��� 5000 �̻��� ������ �̸�, ���� id, �޿��� ����ϼ���
select first_name, job_id, salary
from employees
where job_id = 'IT_PROG' and salary > 5000;

-- 2) or ������
-- Q] ���� id�� IT_PROG�̰ų� �޿��� 5000 �̻��� ������ �̸�, ���� id, �޿��� ����ϼ���
select first_name, job_id, salary
from employees
where job_id = 'IT_PROG' or salary > 5000;

-- Q] ���� id�� IT_PROG �Ǵ� 'FI_MGR'�̰� �޿��� 6000 �̻��� ������ �̸�, ���� id, �޿��� ����ϼ���

-- ����Ŭ���� and�������� �켱������ or���� ����.
-- ���� �ǹ̸� �и��ϰ� �ϱ����ؼ� ()�����ڸ� Ȱ���� ��

-- () ���� �� �ڿ� �ִ� and ������ ���� ���۵ȴ�
select first_name, job_id, salary
from employees
where (job_id = 'IT_PROG' or job_id = 'FI_MGR') and salary >= 6000;

select first_name, job_id, salary
from employees
where job_id = 'IT_PROG' or job_id = 'FI_MGR' and salary >= 6000;

-- ������ ����
-- order by (�⺻ �������� ����)
-- select
-- from
-- where
-- order by <- �� ��ġ�� ���

select first_name, hire_date
from employees
order by hire_date asc; -- ��������� ������������ ����

-- �������� ���� (desc)
select first_name, hire_date
from employees
order by hire_date desc;

-- �� ��Ī ����
select first_name, salary
from employees
order by salary;

-- <= salary*1.2 : �޿��� 20% �λ��� �ݿ��� �ݾ�
select first_name, salary*1.2
from employees
order by salary*1.2;

select first_name, salary*1.2 as "raise_salary"
from employees
order by raise_salary;

-- Q1]
select employee_id, first_name, hire_date, salary
from employees;

-- Q2]
select first_name || ' ' || last_name
    as "name"
from employees;

-- Q3]
select * from
employees
where department_id = 50;

-- Q4]
select first_name, department_id, job_id
from employees
where department_id = 50;

-- Q5]
select first_name, last_name, salary 
from employees;

-- Q6]
select first_name, salary
from employees
where salary > 10000;

-- Q7]
select first_name, job_id, commission_pct
from employees
where commission_pct IS NOT NULL;

-- Q8]
select first_name, hire_date, salary
from employees
where hire_date between '03/01/01' and '03/12/31';

-- Q9]
select first_name, hire_date, salary
from employees
where hire_date like '03%';

-- Q10]
select first_name, salary
from employees
order by salary desc;

-- Q11]
select first_name, salary, department_id
from employees
where department_id = 60
order by salary desc;

-- Q12]
select first_name, job_id
from employees
where job_id = 'IT_PROG' or job_id = 'SA_MAN';

-- Q13]
select first_name || ' ' || last_name || '����� �޿���' || salary || '�޷��Դϴ�'
    as "information"
from employees;

-- Q14]
select first_name, job_id
from employees
where job_id  like '%MAN%';

-- Q15]
select first_name, job_id
from employees
where job_id  like '%MAN%'
order by job_id;

-- select * from employees;