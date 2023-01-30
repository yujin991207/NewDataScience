create table WEATHER_RAIN(
    AREANAME varchar2(15),
    
    RAIN_1_AM number(10),
    WEATHER_1_AM varchar2(80),
    RAIN_1_PM number(10),
    WEATHER_1_PM varchar2(80),
    
    RAIN_2_AM number(10),
    WEATHER_2_AM varchar2(80),
    RAIN_2_PM number(10),
    WEATHER_2_PM varchar2(80),
    
    RAIN_3_AM number(10),
    WEATHER_3_AM varchar2(80),
    RAIN_3_PM number(10),
    WEATHER_3_PM varchar2(80),
    
    RAIN_4_AM number(10),
    WEATHER_4_AM varchar2(80),
    RAIN_4_PM number(10),
    WEATHER_4_PM varchar2(80),
                
    RAIN_5_AM number(10),
    WEATHER_5_AM varchar2(80),
    RAIN_5_PM number(10),
    WEATHER_5_PM varchar2(80),
    
    UPDATETIME DATE
);

SELECT * FROM WEATHER_RAIN;
