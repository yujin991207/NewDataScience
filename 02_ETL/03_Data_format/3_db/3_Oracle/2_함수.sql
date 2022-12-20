-- * �Լ�
-- 1) ������ �Լ� : ���� �࿡���� ���� �����ϰ� �ະ�� �ϳ��� ����� ����
-- 2) ������ �Լ� : ������ ���� �����Ͽ� ���� �׷�� �ϳ��� ����� ���� (��: count())

-- => ������ �Լ� : �����Լ�, �����Լ�, ��¥�Լ�, ��ȯ�Լ�, �Ϲ��Լ�
-----------------------------------------------------
-- �����Լ�

-- dual ���̺� : ����Ŭ ��ü���� ���� Ȯ���ϱ����� �뵵�� �����ϴ� ���̺�
select * from dual;

-- initcap : �ܾ �������� ù ���ڸ� �빮�ڷ� �������� �ҹ��ڷ� ��ȯ�ϴ� �Լ�
select initcap('python specialist') from dual;
select initcap('pythonspecialist') from dual;

-- lower : ��ü�� �ҹ��ڷ� ����� �Լ�
select lower('PYTHON SPECIALIST') from dual;
-- upper : ��ü�� �빮�ڷ� ����� �Լ�
select upper('python specialist') from dual;

-- length : ���ڿ� ���̼��� ��ȯ�ϴ� �Լ�
select length('python specialist') from dual;
select length('���̽�������') from dual;

-- concat : �� ���ڿ��� �����Ͽ� ��ȯ
select concat('���̽�','������') from dual;

-- substr : substr([���ڿ�],[�����ε���],[����ұ��ڼ�]) 
-- => ���ڿ��� �������� �����ε������� ���ε����� ���ڿ� ��ȯ (���ڿ��� �����ε����� 1����)
select substr('���̽�������',1,3) from dual;
select substr('���̽�������',2,4) from dual;
-- instr : instr([���ڿ�],[ã�����ϴ¹��ڿ�])
-- => ���ڿ��� �������� ã�����ϴ� ���ڿ��� �ε��� ��ȯ
select instr('���̽�������','��') from dual;
select instr('���̽�������','��') from dual; -- ��ġ���Ǵ� ���ڿ��� ������ 0�� ��ȯ�Ѵ�.

-- rpad/lpad : �־��� �ڸ�����ŭ ������(rpad)/������ ������ ���ڿ��� ä���.
-- rpad/lpad([���ڿ�],[ä���ڸ���],[ä�﹮��])

select rpad('ȫ�浿',10,'*') from dual; -- �ѱ��� 2���� �ڸ������Ѵ�.
select lpad('ȫ�浿',10,'*') from dual;

-- Q] �������̺��� �̸� 10�ڸ� �� ������ �������� '-'�� ä��� 
--    �޿� 10�ڸ� �� ������ ������ '*'�� ä���� ����Ͻÿ�.
select rpad(first_name,10,'-') as name, lpad(salary,10,'*') as salary
from employees;

-- ltrim/rtrim/trim : ���ڿ��� �������� ������ ���ڸ� ���� ����, ������, �������� ����
-- ltrim/rtrim/trim([���ڿ�],[�����ҹ��ڿ�]) => ������ ���ڿ� �⺻���� ���鹮��
select ltrim('    ���̽� ������    ') as name from dual;
-- ��Ī�� ������ �� as�� ������ �� �ִ�.
select rtrim('    ���̽� ������    ') name from dual;
select trim('    ���̽� ������    ') name from dual;

select ltrim('���̽����������̽�','���̽�') name from dual;
select rtrim('���̽����������̽�','���̽�') name from dual;
-- trim �Լ��� ���� ���鹮�ڸ� ���� �� �� �ִ�. 
-- ���ڰ� 1���̱⶧���� �Ʒ��ڵ�� ������ �߻��Ѵ�.
-- select trim('���̽����������̽�','���̽�') name from dual;

-- replace
select replace('PythonSpecialist','Python','BigData') from dual;
select replace('Python Specialist',' ','') from dual; -- ���鹮�� ����

-- translate([�������ڿ�],[��Ī���ڿ�],[��ȯ���ڿ�])
select translate('1234abcd','abcd','ABC') from dual;

select translate('hello world!!!','hw','HW') from dual;
select translate('hello world!!!','!','?') from dual;

select translate('$100','$','') from dual; -- ��ȯ�� ���ڰ� ���ٸ� null�� ��ȯ
select translate('$100','$',' ') money_num from dual;
select translate('$1,000,000','$,',' ') money from dual;

-- Q] �������̺��� �̸��� �̸� �״��, �ҹ��ڷ�, ù���ڸ� �빮�ڷ�, ��� �빮�ڷ� ����غ�����
select first_name, lower(first_name), initcap(first_name), upper(first_name)
from employees;

select first_name from employees;
select lower(first_name) from employees;
select initcap(first_name) from employees;
select upper(first_name) from employees;

-- Q] �������̺��� �̸��� 'austin'�� ������
--    �̸��� �̸� �״��, �ҹ��ڷ�, ù���ڸ� �빮�ڷ�, ��� �빮�ڷ� ����غ�����
--    �˻��� �ҹ��ڷ� �Ұ�
select last_name, lower(last_name), initcap(last_name), upper(last_name)
from employees
where lower(last_name) = 'austin';

-- ltrim ��ȭ
select ltrim('JavaSpecialist','Java') name from dual;
-- ������ ���ڿ��� ������ ������ ��������ʴ´�.
select ltrim('JavaSpecialist','Jav') name from dual;
-- ���Ŵ� �����������ϴ� ���ڸ� ���� �߰��� ������ �����Ѵ�.
select ltrim('JavaSpecialist','avJ') name from dual;
select ltrim('JavaSpecialist','vJa') name from dual;

-- Q] ���� ���̵� it_prog�� (�ݵ�� �ҹ��ڷ� �˻��ؾ���!) �����
--    �̸��� �տ� 3�ڸ��� ����ϰ� �������ڸ��� * ����ϸ�
--    salary�� ��ü 10�ڸ��� ������ ����ϰ� �������� * ����Ѵ�.
select
rpad (substr(first_name, 1,3), length(first_name),'*') as name, 
lpad (salary,10,'*') as salary
from employees
where lower(job_id) = 'it_prog';

----------------------------------------------------------------
-- �����Լ�

-- �ݿø� : round
select round(45.923,2), round(45.923,0), round(45.923,-1)
from dual;

-- �ø� : ceil
select ceil(7.3) from dual;
select ceil(8.12357) from dual;

-- ���� : floor
select floor(7.845984) from dual;
select floor(5.9) from dual;

-- ���� : trunc([������],[�ڸ���]), �ڸ�����ŭ �������� ���� ����
select trunc(45.923,2), trunc(45.923), trunc(45.923,-1)
from dual;

-- to_date([��¥��Ʈ��],[����])
select to_date('2022-12-20','YYYY-MM-DD') as dt from dual;
-- 'MM' => ���� �������� �����Ѵ�
-- trunc�Լ��� �����Ͽ� �ſ� ù°���� ���Ѵ�
select trunc(to_date('2022-12-20','YYYY-MM-DD'),'MM') as dt from dual;

-- Q] trunc�Լ��� �����Ͽ� 2022�� ù°���� ���Ѵ�.
select trunc(to_date('2022-12-20','YYYY-MM-DD'),'YYYY') as dt from dual;

-- DD�� �����ϸ� �ϴ����� ������ ��¥�� �����Ƿ� ���ϰ��� ��ȯ�Ѵ�.
select trunc(to_date('2022-12-20','YYYY-MM-DD'),'DD') as dt from dual;
-- DAY�� �����ϸ� �� ���� ù��° �Ͽ����� ��ȯ�Ѵ�.
select trunc(to_date('2022-12-23','YYYY-MM-DD'),'DAY') as dt from dual;
select trunc(to_date('2022-12-31','YYYY-MM-DD'),'DAY') as dt from dual;

-- ���밪
select abs(-1000) abs_num from dual;
-- ������
select power(2,3) power_num from dual;
-- ������
select sqrt(100) sqrt_num from dual;
-- ������
select mod(10,3) mod_num from dual;

---------------------------------------------------------------
-- ��¥�Լ�

-- SYSDATE : ������ ��¥�� ��ȯ(YY/MM/DD)
select sysdate today from dual;

-- SYSTIMESTAMP : ������ ��¥�� �ð��� ��ȯ
select systimestamp from dual;

-- Q] �μ���ȣ�� 60�� ����� �̸��� ������� �ٹ��� �ָ� 'Weeks' �� �̸����� ���
select first_name, (sysdate-hire_date)/7 as Weeks
from employees
where department_id = 60;

-- MONTHS_BETWEEN : �� ��¥ ������ �� ���� ��ȯ
-- ���� ��������� ��ȯ
select first_name, sysdate, hire_date, 
months_between(sysdate,hire_date) as workmonth
from employees
where first_name = 'Diana';

-- ADD_MONTHS : �����Ͽ� ���� ����
select first_name, hire_date, ADD_MONTHS(hire_date,1)
from employees
where first_name = 'Diana';

-- Q] �� ������ Ȱ���Ͽ� Diana�� �Ի� �� 200������ ���� ��¥�� ���ϼ���.
select first_name, hire_date, ADD_MONTHS(hire_date,200)
from employees
where first_name = 'Diana';

-- NEXT_DAY : ���ƿ��� ���� �ֱ� ���� ��¥
select sysdate, next_day(sysdate,'��') from dual;
select sysdate, next_day(sysdate,'��') from dual;

-- LAST_DAY : �ش� ���� ���Ե� ���� ������ ��¥
select sysdate, last_day(sysdate) from dual;

-- Q] 1������ 12������ ���������� ����ϼ���.
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
-- �������̺��� ....... email (��ü �ҹ���, ��ü �빮��, ù���ڸ� �빮��)
select lower(email), upper(email), initcap(email)
from employees;
-- manager_id�� 114���̰� �޿��� 2700�̻��� ����� �޿��� 10% �λ��ؼ� ���
select salary, salary+(salary * 0.1)
from employees
where manager_id = 114 and salary >= 2700;
-- �μ���ȣ�� 80�� ����� �̸��� ������� �ٹ��� �ָ� ���ο�� ����ϼ���
select first_name, (sysdate-hire_date)/7 as Weeks
from employees
where department_id = 80;

select hire_date
from employees
where hire_date like '05/10%';

-- job_id FI_ACCOUNT �̰� �Ի���� �������� 1���� ���� �⵵/��/�ϰ� , 
-- �Ի��, �̸��� ����ϼ���
-- �׸��� �Ի縦 ������ ������ ����ϼ���

-- job_id 'clerk'�� �� ������ �ش��ϴ� ����� �̸�, ����id��
-- �̸������ ���
select first_name, job_id
from employees
where job_id like '%CLERK%'
order by first_name;

-- ���ʽ��� �������� ������� �޿��� 300�޷� �߰������ϰ�
-- �̸�, �߰����޵ȱ޿��� ���
select first_name,commission_pct,salary+300 as total_salary
from employees
where commission_pct is null
order by total_salary desc;

-- ù���ڿ� ���������ڻ��� * ��� (A����)
-- ����������� 10�� ���� ����̸��� hire_date, �������̵� ����ϼ���
select first_name, hire_date, job_id, round((sysdate-hire_date)/365,0) as works_month
from employees
where (sysdate-hire_date)/365 > 10;

-- �ڵ�����ȣ���� . �� - ���� ��� ���ڸ��� *�� ���
select replace(rpad(substr(phone_number,1,4), length(phone_number),'*'),'.','-')
from employees;
