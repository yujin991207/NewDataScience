create table air_temp(
    �������ڵ�   varchar2(32),
    �����Ҹ�     varchar2(16),
    �����ð�    timestamp,
    ���       number(8,3)
);
select * from air_temp;
select * from air_temp order by �����ð� desc;
commit;

delete from air_temp;

commit;


insert into air_temp values ('DT_0001','��õ','22/12/29 10:00:00', '-2.5');