-- 테스트용 테이블 생성
create table test_table(
    deptno number(2),
    dname varchar2(14),
    loc varchar2(13)
);

-- 테이블 스키마 조회
describe test_table;

-- 샘플 데이터 입력테스트
insert into test_table values(1,'IT개발','서울');

select * from test_table;

-- 테이블의 열 추가
alter table test_table
add (job varchar2(10));

describe test_table;

-- 열이름 변경
alter table test_table
rename column deptno to department_no;

select * from test_table;

alter table test_table
rename column dname to department_name;

select * from test_table;
describe test_table;

-- 열속성 변경
-- 제약사항 : 사이즈를 크게 변경하는 것은 문제가 없으나 작게는 허용이 안됨.
alter table test_table
modify (department_name varchar2(20));

describe test_table;

-- 열 삭제
alter table test_table
drop column job;

describe test_table;

-- 테이블 삭제
drop table test_table;
-- 변경사항은 새로고침 또는 Ctrl+R
describe test_table;
