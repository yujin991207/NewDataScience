create table oldman_job (
    수행기관 varchar2(80),
    사업명 varchar2(80), 
    사업구분 varchar2(36),
    사업주요활동내용 varchar2(180), 
    인원 number(8),
    구군명 varchar2(60), 
    전화번호 varchar2(20),
    사업시작일 date,
    사업종료일 date, 
    데이터기준일자 date
);

select * from oldman_job;

select count(*) from oldman_job;