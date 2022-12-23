-- �׽�Ʈ�� ���̺� ����
create table test_table(
    deptno number(2),
    dname varchar2(14),
    loc varchar2(13)
);

-- ���̺� ��Ű�� ��ȸ
describe test_table;

-- ���� ������ �Է��׽�Ʈ
insert into test_table values(1,'IT����','����');

select * from test_table;

-- ���̺��� �� �߰�
alter table test_table
add (job varchar2(10));

describe test_table;

-- ���̸� ����
alter table test_table
rename column deptno to department_no;

select * from test_table;

alter table test_table
rename column dname to department_name;

select * from test_table;
describe test_table;

-- ���Ӽ� ����
-- ������� : ����� ũ�� �����ϴ� ���� ������ ������ �۰Դ� ����� �ȵ�.
alter table test_table
modify (department_name varchar2(20));

describe test_table;

-- �� ����
alter table test_table
drop column job;

describe test_table;

-- ���̺� ����
drop table test_table;
-- ��������� ���ΰ�ħ �Ǵ� Ctrl+R
describe test_table;
