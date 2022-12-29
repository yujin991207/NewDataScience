create table air_temp(
    관측소코드   varchar2(32),
    관측소명     varchar2(16),
    관측시간    timestamp,
    기온       number(8,3)
);
select * from air_temp;
select * from air_temp order by 관측시간 desc;
commit;

delete from air_temp;

commit;


insert into air_temp values ('DT_0001','인천','22/12/29 10:00:00', '-2.5');