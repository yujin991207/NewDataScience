create table covid_hospital(
        ����� varchar2(128),
        �����ڵ� varchar2(8),
        �õ��� varchar2(8),
        �ñ����� varchar2(32),
        ��ȭ��ȣ varchar2(32),
        ��������� date    
);

delete from covid_hospital;

select count(*)
from covid_hospital;

select * from covid_hospital;