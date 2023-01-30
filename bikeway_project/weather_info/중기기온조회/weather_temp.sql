create table WEATHER_TEMP(
        AREANAME varchar2(15), 
        LOWTEMP_1 number(10), 
        HIGHTEMP_1 number(10),
        LOWTEMP_2 number(10),
        HIGHTEMP_2 number(10),
        LOWTEMP_3 number(10),
        HIGHTEMP_3 number(10),
        LOWTEMP_4 number(10),
        HIGHTEMP_4 number(10),
        LOWTEMP_5 number(10),
        HIGHTEMP_5 number(10),
	
        UPDATETIME DATE
);

select * from weather_temp;
DROP TABLE weather_temp;
commit;
