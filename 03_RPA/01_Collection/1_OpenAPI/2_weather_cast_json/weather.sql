create table weather(
    date_time timestamp,
    nx number(8,3),
    ny number(8,3),
    �ð�1_������ number(8,3),
    �������� number(8,3),
    ��� number(8,3),
    ���� number(8,3),
    ǳ�� number(8,3),
    ǳ�� number(8,3),
    �����ٶ����� number(8,3),
    ���Ϲٶ����� number(8,3)
);

describe weather;

select * from weather;

delete from weather;
-- �ڵ� ���� sql
INSERT INTO WEATHER (DATE_TIME, NX, NY, "���", "�ð�1_������", "��������", "����", "ǳ��", "ǳ��", "�����ٶ�����", "���Ϲٶ�����") VALUES (to_timestamp('202212271500'),58,125,3.4,0.0,0.0,46.0,1.4,225.0,1.0,1.0);
INSERT INTO WEATHER (DATE_TIME, NX, NY, "���", "�ð�1_������", "��������", "����", "ǳ��", "ǳ��", "�����ٶ�����", "���Ϲٶ�����") VALUES ('20221227 1500',58,125,3.4,0.0,0.0,46.0,1.4,225.0,1.0,1.0);

commit;

insert into weather values (
'202212281100',
58,125,0,0,-2.8,60,250,3,2.8,-0.8
);

insert into weather values (
'202212281000',
58,125,0,0,-2.1,60,248,3,2.8,-0.7
);

insert into weather values (
'202212281200',
58,125,0,0,-1.3,62,245,2,2.5,-0.6
);

insert into weather values (
'202212281300',
58,125,0,0,0.2,62,232,2,2.5,-0.6
);

insert into weather values (
'202212281400',
58,125,0,0,0.2,62,232,2,2.5,-0.6
);

delete from weather
where date_time = '202212281200';

commit;

select * from weather;

commit;

drop table weather;
