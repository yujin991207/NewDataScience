--# RENTALNAME, HOLDER_COUNT, BIKE_COUNT, WEEDO, GYUNGDO, RENTALID, UPDATE_DATE

create table BIKE_REAL_TIME(
    STATIONNAME varchar2(180),
    RACKTOCNT number(10),
    BIKETOCNT number(10),
    SHARED_RATE number(14,9),
    LATITUDE number(14,9),
    LONGITUDE number(14,9),
    STATIONID  varchar2(80),
    UPDATETIME date
);

drop table bike_real_time;
COMMIT;

select * from bike_real_time;
select * from bike_real_time where updatetime = (select max(updatetime) from bike_real_time);

drop table bike_real_time;
COMMIT;

delete from bike_real_time;