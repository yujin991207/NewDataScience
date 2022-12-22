----------------------------------------------------
-- �м��Լ� : �����ͺм��� ���� �پ��� ��� ����

-- RANK : �������� �켱������ ���� (�ߺ����� �����) 
-- DENSE_RANK : �������� �켱������ ���� (�ߺ������� ��������ʴ´�)
-- CUME_DIST : �ִ밪 1�� �������� �л�� ���� ����
-- PERCENT_RANK : �ִ밪 1�� �������� �����(percent)���� ����
--                => ù��° ��ġ�� 0���� �����ϰ� �ι�° row������ ��ġ��
--                  (row�� rank-1 / ��ü row ���� -1)
--                  rank�� �������� ������ rank�� ������ ��ü ��� �� % ������ �ؼ�
-- NTILE : ntile(n) ��ü ������ ������ �տ������� n���� �������� ������ ǥ��

-- ����
-- �м��Լ� over([order by])
select * from employees;
select first_name, salary,
    rank() over (order by salary desc) as rank,
    dense_rank() over (order by salary desc) as dense_rank,
    round(cume_dist() over (order by salary desc),3) as cume_rank,
    round(percent_rank() over (order by salary desc),3) as percent_rank,
    ntile(3) over (order by salary desc) as ntile,
    rownum, -- �ǻ翭(���� ���̺� �ο��� ���ȣ)
    -- �˻������ ���� ���������� �ο��Ǵ� ���ȣ (row_number)
    row_number() over (order by salary desc) as row_number 
    from employees;
    
-- ratio_to_report
-- ��ȸ�ϴ� ���� �ش� �÷� ���� ������� ����
-- ��) ����
--     30 <- 0.3
--     50 <- 0.5
--     20 <- 0.2
select first_name, salary, 
round(ratio_to_report(salary) over (),4) as salary_ratio
from employees
where job_id = 'IT_PROG';

-- LAG / LEAD (����/���� ���� ���� �˻�)
-- LAG([���̸�],[���� �̵���],[���� ���� ��� ��ȯ��])
-- LEAD([���̸�],[���� �̵���],[���� ���� ��� ��ȯ��])
-- �������̵�, ����޿� �������� ���� �޿�, ���� �޿�, ���� �޿����� �������� ���� �޿�
select employee_id,
    lag(salary, 1,0) over (order by salary) as lower_sal,
    salary,
    lead(salary, 1,0) over (order by salary) as higher_sal
from employees
order by salary;
-- ��� => ù��° ���� �������� ���⶧���� 0���� ��ȯ���ش�.

-- LISTAGG
-- LISTAGG([��, ����], [������])
--      WITHIN GROUP(ORDER BY [���̸�])
-- ��� : �����Ǵ°��� ������ join(����)
select department_id, 
    listagg(first_name,', ') within group (order by hire_date) as names
from employees
group by department_id;

select * from employees;

-- PIVOT, UNPIVOT
-- table ����
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

-- PIVOT : ������ ������ �������� �����͸� ������ �Ӽ����� ���� ����(���, �հ� ��)�ϰ� ���� ��Ÿ����.
-- �α׼� ������(Long ����)�� �м��� ������(Wide ����)�� ��ȯ�ϴ� ����
-- ����
-- select
-- from
-- pivot(
--     �׷��Լ�(�������÷�)
--     for [�ǹ������÷�]
--     in (�ǹ��÷� ����)
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

-- table ����
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

-- UNPIVOT :  �������� ������ ������ �������� �����͸� ������ ���� ���� (stack) ����
-- ���ռӼ��� ���� �Ӽ����� ��ȯ�ϴ� ����
-- ����
-- select
-- from
-- unpivot
-- (
--   [������ ���� �̸� : ���� �������� ���� ��Ÿ���� �̸�]
--   for [������ ���� �̸� : ���� �����Ϳ��� ������ ���� ���� Ư���� ��Ÿ���� �̸�]
--   in ([���ص������� ���մ��1], [���ص������� ���մ��2] .... )
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

