describe ii1;

select count(*) from ii1;
select count(*) from ii3;

select count(*) from ii6;

select * from ii6;

alter table ii6 rename to museum;
describe museum;

drop table ii1;
drop table ii2;
drop table ii3;
drop table ii4;
drop table ii5;

alter table i2 rename to drug_store;
desc drug_store;

select count(*) from drug_store;

select count(*)
from drug_store
where '��ǥ����X' is null;

SELECT count(*)
from drug_store
where '��ǥ����X' is null and '��ǥ����Y' is null;


SELECT *
from drug_store;


SELECT count(*)
from drug_store
where ��ǥ����X is null and ��ǥ����Y is null;

select count(*)
from drug_store
where ��������ü�ּ� is null or ���θ���ü�ּ� is null;

select ���θ���ü�ּ�
from drug_store
where ���θ���ü�ּ� like '����%';

select ������ȣ, �󼼿������¸�, nvl(�������,'-') as �������, 
��������ü�ּ�, ���θ���ü�ּ�, ������, ��ǥ����X, ��ǥ����Y
from drug_store;

select * from drug_store;

select * 
from drug_store
where ���θ���ü�ּ� like '��⵵%';

select ������ȣ, �󼼿������¸�, �������, 
    case when ���θ���ü�ּ� like '����%' then '����Ư����'
         when ���θ���ü�ּ� like '��⵵%' then '��⵵'
         when ���θ���ü�ּ� like '������%' then '������'
         when ���θ���ü�ּ� like '��󳲵�%' then '��󳲵�'
         when ���θ���ü�ּ� like '���ϵ�%' then '���ϵ�'
         when ���θ���ü�ּ� like '��û����%' then '��û����'
         when ���θ���ü�ּ� like '��û�ϵ�%' then '��û�ϵ�'
         when ���θ���ü�ּ� like '���󳲵�%' then '���󳲵�'
         when ���θ���ü�ּ� like '����ϵ�%' then '����ϵ�'
         when ���θ���ü�ּ� like '���ֱ�����%' then '���ֱ�����'
         when ���θ���ü�ּ� like '�λ걤����%' then '�λ걤����'
         when ���θ���ü�ּ� like '�뱸������%' then '�뱸������'
         when ���θ���ü�ּ� like '����������%' then '����������'
         when ���θ���ü�ּ� like '��걤����%' then '��걤����'
         when ���θ���ü�ּ� like '��õ������%' then '��õ������'
         when ���θ���ü�ּ� like '����%' then '����Ư����ġ��'
         when ���θ���ü�ּ� like '����%' then '����Ư����'
    else ���θ���ü�ּ�
    end as �õ���, ��������ü�ּ�, ���θ���ü�ּ�, ������, ��ǥ����X, ��ǥ����Y
from drug_store;

select ������ȣ, �󼼿������¸�, �������, 
    case when ��������ü�ּ� like '����%' then '����Ư����'
         when ��������ü�ּ� like '��⵵%' then '��⵵'
         when ��������ü�ּ� like '������%' then '������'
         when ��������ü�ּ� like '��󳲵�%' then '��󳲵�'
         when ��������ü�ּ� like '���ϵ�%' then '���ϵ�'
         when ��������ü�ּ� like '��û����%' then '��û����'
         when ��������ü�ּ� like '��û�ϵ�%' then '��û�ϵ�'
         when ��������ü�ּ� like '���󳲵�%' then '���󳲵�'
         when ��������ü�ּ� like '����ϵ�%' then '����ϵ�'
         when ��������ü�ּ� like '���ֱ�����%' then '���ֱ�����'
         when ��������ü�ּ� like '�λ걤����%' then '�λ걤����'
         when ��������ü�ּ� like '�뱸������%' then '�뱸������'
         when ��������ü�ּ� like '����������%' then '����������'
         when ��������ü�ּ� like '��걤����%' then '��걤����'
         when ��������ü�ּ� like '��õ������%' then '��õ������'
         when ��������ü�ּ� like '����%' then '����Ư����ġ��'
         when ��������ü�ּ� like '����%' then '����Ư����'
    else ���θ���ü�ּ�
    end as �õ���, ��������ü�ּ�, ���θ���ü�ּ�, ������, ��ǥ����X, ��ǥ����Y
from drug_store
where ���θ���ü�ּ� is null;

select ������ȣ, �󼼿������¸�, �������, 
    case when ���θ���ü�ּ� like '����%' then '����Ư����'
         when ���θ���ü�ּ� like '��⵵%' then '��⵵'
         when ���θ���ü�ּ� like '������%' then '������'
         when ���θ���ü�ּ� like '��󳲵�%' then '��󳲵�'
         when ���θ���ü�ּ� like '���ϵ�%' then '���ϵ�'
         when ���θ���ü�ּ� like '��û����%' then '��û����'
         when ���θ���ü�ּ� like '��û�ϵ�%' then '��û�ϵ�'
         when ���θ���ü�ּ� like '���󳲵�%' then '���󳲵�'
         when ���θ���ü�ּ� like '����ϵ�%' then '����ϵ�'
         when ���θ���ü�ּ� like '���ֱ�����%' then '���ֱ�����'
         when ���θ���ü�ּ� like '�λ걤����%' then '�λ걤����'
         when ���θ���ü�ּ� like '�뱸������%' then '�뱸������'
         when ���θ���ü�ּ� like '����������%' then '����������'
         when ���θ���ü�ּ� like '��걤����%' then '��걤����'
         when ���θ���ü�ּ� like '��õ������%' then '��õ������'
         when ���θ���ü�ּ� like '����%' then '����Ư����ġ��'
         when ���θ���ü�ּ� like '����%' then '����Ư����'
         when ��������ü�ּ� like '����%' then '����Ư����'
         when ��������ü�ּ� like '��⵵%' then '��⵵'
         when ��������ü�ּ� like '������%' then '������'
         when ��������ü�ּ� like '��󳲵�%' then '��󳲵�'
         when ��������ü�ּ� like '���ϵ�%' then '���ϵ�'
         when ��������ü�ּ� like '��û����%' then '��û����'
         when ��������ü�ּ� like '��û�ϵ�%' then '��û�ϵ�'
         when ��������ü�ּ� like '���󳲵�%' then '���󳲵�'
         when ��������ü�ּ� like '����ϵ�%' then '����ϵ�'
         when ��������ü�ּ� like '���ֱ�����%' then '���ֱ�����'
         when ��������ü�ּ� like '�λ걤����%' then '�λ걤����'
         when ��������ü�ּ� like '�뱸������%' then '�뱸������'
         when ��������ü�ּ� like '����������%' then '����������'
         when ��������ü�ּ� like '��걤����%' then '��걤����'
         when ��������ü�ּ� like '��õ������%' then '��õ������'
         when ��������ü�ּ� like '����%' then '����Ư����ġ��'
         when ��������ü�ּ� like '����%' then '����Ư����'
    else ���θ���ü�ּ�
    end as �õ���, ��������ü�ּ�, ���θ���ü�ּ�, ������, ��ǥ����X, ��ǥ����Y
from drug_store;


UPDATE drug_store
    set �󼼿������¸� = '���' 
WHERE �󼼿������¸� = '�������';

select * from 
drug_store
where ��������ü�ּ� like 'Ȳ�ص�%' and �󼼿������¼��� = '������';