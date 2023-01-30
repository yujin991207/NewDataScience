create table bike_real_time(
    INDEX_NUMBER number(10),
    STATIONNAME varchar2(180),
    RACKTOCNT number(10),
    BIKETOCNT number(10),
    SHARED_RATE number(10),
    LAT number(14,9),
    LON number(14,9),
    STATIONID  varchar2(80),
    UPDATETIME timestamp
);


select * from weather_rain;
select * from weather_temp;

select * from matzip;

create table time(
    time_test timestamp,
    time_test_2 DATE
);

drop table bike_real_time;

drop table time;
delete from bike_real_time;
select * from bike_real_time;
insert into time values(sysdate,sysdate);
commit;

select * from riding;

MERGE INTO bike_real_time 
        USING dual
            ON (STATIONNAME = :STATIONNAME and RIDING_DT = :RIDING_DT)
        WHEN NOT MATCHED THEN
            INSERT (STATIONNAME,RACKTOCNT,BIKETOCNT,SHARED_RATE,LAT,LON,STATIONID,UPDATETIME)
            VALUES (:STATIONNAME,:RACKTOCNT,:BIKETOCNT,:SHARED_RATE,:LAT,:LON,:STATIONID,:UPDATETIME) 
        WHEN MATCHED THEN
            UPDATE SET
                RACKTOCNT=:RACKTOCNT,BIKETOCNT=BIKETOCNT;
                
                commit;

select * from riding;
select * from member;

SELECT A.*,TO_CHAR(A.RIDING_DT,'DY') DAY 
  FROM RIDING A
 WHERE A.ID = 1
ORDER BY RIDING_DT ;

-- 주행거리 dt별로 평균
select riding_dt,round(sum(distance)/(select count(distinct(id)) from riding),2) as avg_distance
                from riding group by 
                riding_dt order by riding_dt;
                
---------------------------------------
-- Kcal
select r.riding_dt as riding_dt,
                       round(sum(2.3*m.weight*(r.riding_time*0.0667))/ count(distinct(m.id)),2) as avg_Kcal
                       from riding r join member m on r.id=m.id
                       group by r.riding_dt
                       order by r.riding_dt;
                       
                       
select * from riding;
select * from weather_rain;

select * from bike_real_time;
delete from bike_real_time;

select b.riding_dt, nvl(a.avg,0) distance from (select riding_dt,round(sum(distance)/(select ceil(count(distinct(id))*0.1) from riding),2) as avg from riding where id in (select id from 
    (select sum(distance) sum, id from riding 
    group by id order by sum desc) 
    where rownum<= (select ceil(count(distinct(id))*0.1) from riding)) group by riding_dt order by riding_dt) a right join (SELECT TO_CHAR(SDT + LEVEL - 1, 'YYYY-MM-DD') riding_dt, 0 as distance
   FROM (SELECT TO_DATE('2023-01-15', 'YYYY-MM-DD') SDT  -- 시작 일자
              , (TO_DATE('2023-01-21', 'YYYY-MM-DD')+6) EDT -- 종료일자
           FROM DUAL)
 CONNECT BY LEVEL <= EDT - SDT + 1) b on a.riding_dt = b.riding_dt;
 
 select b.riding_dt, round(nvl(a.cal, 0),2) cal from(select  r.riding_dt riding_dt,2.3 * m.weight*(r.riding_time*0.0667) as cal from member m join riding r on m.id=r.id where m.id=1) a right join (SELECT TO_CHAR(SDT + LEVEL - 1, 'YYYY-MM-DD') riding_dt, 0 as distance
   FROM (SELECT TO_DATE('2023-01-04', 'YYYY-MM-DD') SDT  -- 시작 일자
              , (TO_DATE('2023-01-10', 'YYYY-MM-DD')+6) EDT -- 종료일자
           FROM DUAL)
 CONNECT BY LEVEL <= EDT - SDT + 1) b on a.riding_dt = b.riding_dt order by b.riding_dt;
select * from member;
                


                
                