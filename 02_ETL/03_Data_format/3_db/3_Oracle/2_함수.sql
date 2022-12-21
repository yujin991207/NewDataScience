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
-- ��ȯ�Լ�
-- �Ͻ��� �� ��ȯ
-- number <-> character <-> date

select first_name from employees
where department_id = 40; -- <= ����Ÿ��

select first_name from employees
where department_id = '40'; -- <= ����Ÿ�������� �Ͻ��� ����ȯ�� �Ͼ��

select first_name from employees
where hire_date = '03/06/17'; -- <= ����Ÿ�������� �Ͻ��� ����ȯ�� �Ͼ��

select '5500.00' - 4000 from dual;
-- ������! ������ �� �����ʹ� �Ϲ��� �� ��ȯ�� �����ʴ´�.
select '$5500.00' - 4000 from dual; -- ����

--select ltrim('$5500.00','$') - 4000 
--from dual;
select first_name from employees
where hire_date = '03�� 6�� 17��'; -- ����

select first_name from employees
where hire_date = '03/06/17';

-- ����� �� ��ȯ
-- TO_CHAR : ����(��¥)���� ��¥������ �����Ͽ� ���ڷ� ��ȯ, TO_CHAR([��¥],[��¥����])
select first_name, to_char(hire_date,'MM/YY') as HiredMonth
from employees
where first_name = 'Steven';

select first_name, to_char(hire_date,'YYYY"��" MM"��" DD"��"') as HiredMonth
from employees
where first_name = 'Steven';

select first_name, to_char(hire_date,'YYYY-MM-DD') as HiredMonth
from employees
where first_name = 'Steven';

-- TO_CHAR : ����(����)���� ��¥������ �����Ͽ� ���ڷ� ��ȯ, TO_CHAR([����],[��������])
-- ex) $999,999 <- ���ڴ� 9�� ǥ��
-- ���˺��� ��ȯ������ ���̰� ū ��쿡�� '#'���� ǥ��ȴ�.
select to_char(2000000,'$999,999') salary from dual; -- '#' ���
select to_char(2000000,'$9999,999') salary from dual;

-- �տ� 0���� padding�ϰ������� 
-- ��ǥ �ݾ��� �ڸ����� ����Ͽ� ǥ���ϰ� ���� ���
select to_char(2000000,'$009,999,999') salary from dual;

-- �Ҽ������� �ڸ��� ���� ������ ���ٸ� �� ���� �����ȴ�.
select to_char(2000000.45,'$009,999,999') salary from dual;
-- �Ҽ��� ó��
select to_char(2000000.45,'$009,999,999.99') salary from dual;

-- ��������ȭ���ȣ ��� ('L' ��ȣ ���)
select to_char(2000000,'L9,999,999') salary from dual;

-- Q] �������̺� �̸��� David�� �̸�, ��, �޿� 
--    salary1���� 15.23% �λ����� 15% �λ�� �ݾ���
--   ������ ���� ����($1,466,85)�� ����� �λ�ݾ��� salary2���� ����ϼ���
select first_name, last_name, salary, salary*0.15 salary1, 
to_char(salary*0.1523,'$9,999.99') salary2
from employees
where first_name = 'David';

-- ���ϴ� ��¥ �������� �˻��ϱ�
select first_name, hire_date
from employees
where hire_date = TO_DATE('2003/06/17','YYYY/MM/DD');

-- TO_DATE : ���ڸ� ��¥ Ÿ������ ����
-- Q] 2003��6��17�Ͽ� �Ի��� �����̸�, �Ի����� ����ϼ��� ('2003��6��17��'�� �˻�����)
select first_name, hire_date
from employees
where hire_date = TO_DATE('2003��06��17��','YYYY"��"MM"��"DD"��"');

-- Q] ��¥Ÿ���� �Ʒ��� ���� ��µǵ��� �����̸�, �Ի����� ����ϼ���.
--   '2003-06-17'
select first_name, TO_CHAR(hire_date,'YYYY-MM-DD') as hire_date
from employees;

-- NULL ��ȯ .. ����ġó��
-- NVL
-- NVL([������],[null�̸� ��ȯ�Ǵ� ��]) <= �������� null�� �ƴϸ� �������� ��ȯ
select nvl(1000,100) from dual;
select nvl(null,100) from dual;

select commission_pct from employees;
select nvl(commission_pct,0) from employees;

select first_name, salary, nvl(commission_pct,0) commission_pct,
salary+(salary*(nvl(commission_pct,0))) as total_salary
from employees;

-- NVL2
-- NVL2([������],[null�� �ƴϸ� ��ȯ�Ǵ� ��],[null�̸� ��ȯ�Ǵ� ��]) 
select nvl2(1.2, 1000*0.2, 0) from dual;

select first_name, salary, nvl(commission_pct,0) commission_pct,
nvl2(commission_pct, salary+(salary*commission_pct), salary) as total_salary
from employees;

-- COALESCE([���Ǵ±���1],[���Ǵ±���2] ...) : null�� �ƴ� ù��° ������ ���� ����
-- ��) �������ͺ��̽����� ���������� ��ȣ�� �����ϰ��� �� ��
-- ���ð����� �� �� (�޴���, ����ȭ, ȸ���ȣ) �켱������ ���Ͽ� 
-- ���� �ƴ� ���� �����ϰ��� �� �� ����
select coalesce('010-123-4567',null,null) from dual;
select coalesce(null,'070-123-4567',null) from dual;
select coalesce(null,null,'02-123-4567') from dual;

-- Q] �� ������ coalesce�Լ��� ����ؼ� Ǯ�����.
select first_name, salary, nvl(commission_pct,0) commission_pct,
coalesce(salary+(salary*commission_pct), salary) as total_salary
from employees;

-- Q] ���ʽ��� 650�޷����� �۰ų� ���ʽ��� ���� ����鿡�� ��ǰ���� �����Ϸ����Ѵ�.
--    �ش� ������� �̸��� ���ʽ��� ����ϼ���. (coalesce �Լ� ����� ��)
--   (76�� ���� ��µ�)
select first_name,
coalesce(salary*commission_pct,0) as bonus
from employees
where coalesce(salary*commission_pct,0) < 650;

-- LNNVL : LNNNVL(����) ������ ����� false �Ǵ� unknown�̸� true�� ��ȯ
-- ������ �ݴ��� ��쿡���� �˻��ϰ� ���� �� Ȱ��
select first_name,
coalesce(salary*commission_pct,0) as bonus
from employees
where LNNVL(salary*commission_pct >= 650);

-- DECODE : DECODE(Column or expression, search1, result
--                                       [search2, result2, ...]

-- ù��°���� �ι�°���� ���ٸ� ����°���� ��ȯ���ش�
select decode('java','java','�鿣�� ���') as language from dual;

select decode('java','java','�鿣�� ���'
                    ,'html','����Ʈ���� ���'
                    ,'python','�����ͻ��̾� ���'
                    ) as language_j from dual;
                    
select decode('html','java','�鿣�� ���'
                    ,'html','����Ʈ���� ���'
                    ,'python','�����ͻ��̾� ���'
                    ) as language_h from dual;
                    
select decode('python','java','�鿣�� ���'
                    ,'html','����Ʈ���� ���'
                    ,'python','�����ͻ��̾� ���'
                    ) as language_p from dual;

-- ��ġ�Ǵ� �˻����ڿ��� ���ٸ� null�� ��ȯ�Ѵ�
select decode('css','java','�鿣�� ���'
                    ,'html','����Ʈ���� ���'
                    ,'python','�����ͻ��̾� ���'
                    ) as language_c from dual;
                    
-- default���� ���� �������� �����Ѵ� (search ���ڿ�����)
select decode('css','java','�鿣�� ���'
                    ,'html','����Ʈ���� ���'
                    ,'python','�����ͻ��̾� ���'
                    ,'��Ÿ���'
                    ) as language from dual;
                    
-- Q] �������̺��� ���� ID, �޿�, �׸��� �޿� �λ����� ����Ѵ�.
--    �޿��λ����� ���� id�� IT FROG, FI MGR, FI ACCOUNT�� ���� 
--    ���� 10, 15, 20% �λ����� �����Ѵ�.
select job_id, salary,
    decode(job_id,'IT_PROG',salary+(salary*0.1)
                ,'FI_MGR',salary+(salary*0.15)
                ,'FI_ACCOUNT',salary+(salary*0.2)
                ,salary)
                as revised_salary
from employees;

-- CASE ~ WHEN ~ THEN
select job_id, salary,
    case job_id when'IT_PROG' then salary+(salary*0.1)
                when'FI_MGR' then salary+(salary*0.15)
                when'FI_ACCOUNT' then salary+(salary*0.2)
                else salary
    end as revised_salary
from employees;

-- �������� �����
select job_id, salary,
    case when job_id = 'IT_PROG' then salary+(salary*0.1)
         when job_id ='FI_MGR' then salary+(salary*0.15)
         when job_id ='FI_ACCOUNT' then salary+(salary*0.2)
         else salary
    end as revised_salary
from employees;

-- ��ø�Լ� ����ϱ�
-- �Լ�1(�Լ�2(�Լ�3))
-- step1
select add_months(hire_date,6)-- �Ի� �� 6����
from employees
order by hire_date;
-- step2
-- �Ի� �� 6���� �� �� �ݿ��� ���
select next_day(add_months(hire_date,6),'��') as cal_day
from employees
order by hire_date;
-- step3
-- �Ի� �� 6���� �� �� �ݿ����� ���� 'YYYY-MM-DD' �������� ���
select to_char(next_day(add_months(hire_date,6),'��'),'YYYY-MM-DD') as cal_day
from employees
order by hire_date;

-- Q] ���� �̸��� �޿�, �Ի�⵵, �Ի��� ���� ����, �޿� �λ���� ����Ͻÿ�.
--    �����������
--    �޿� �λ���� ������ ����
--    > �ټӳ⵵�� 10�� �̻��̸� 10%�λ�
--    > �ټӳ⵵�� 5�� �̻��̸� 5%�λ�
--    > 5�� �̸��� �λ�� ����
select first_name, salary, 
       to_char(hire_date,'YYYY"��" "�Ի�"') as year,
       to_char(hire_date,'DAY') as day,
    case when ((sysdate-hire_date)/365) >= 10 then to_char(salary+(salary*0.1),'$999,999')
         when ((sysdate-hire_date)/365) >= 5 then to_char(salary+(salary*0.15),'$999,999')
         when ((sysdate-hire_date)/365) < 5 then to_char(salary+(salary*0.2),'$999,999')
         else to_char(salary,'$999,999')
    end as revised_salary
from employees;

-- ���տ�����
-- UNION : �ΰ� �̻��� ���ǰ���� ��ġ�� ���� (�ߺ��Ǵ°���� ����)
select employee_id, first_name
from employees
where hire_date like '04%'
union
select employee_id, first_name
from employees
where department_id = 20;

-- UNION ALL (������, �ߺ��� ���� ����)
select employee_id, first_name
from employees
where hire_date like '04%'
union all
select employee_id, first_name
from employees
where department_id = 20;

-- INTERSECT (������)
select employee_id, first_name
from employees
where hire_date like '04%'
intersect
select employee_id, first_name
from employees
where department_id = 20;

-- MINUS (������)
select employee_id, first_name
from employees
where hire_date like '04%'
minus
select employee_id, first_name
from employees
where department_id = 20;

select employee_id, first_name
from employees
where department_id = 20
minus
select employee_id, first_name
from employees
where hire_date like '04%';

