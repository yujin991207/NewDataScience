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
where '좌표정보X' is null;

SELECT count(*)
from drug_store
where '좌표정보X' is null and '좌표정보Y' is null;


SELECT *
from drug_store;


SELECT count(*)
from drug_store
where 좌표정보X is null and 좌표정보Y is null;

select count(*)
from drug_store
where 소재지전체주소 is null or 도로명전체주소 is null;

select 도로명전체주소
from drug_store
where 도로명전체주소 like '서울%';

select 관리번호, 상세영업상태명, nvl(폐업일자,'-') as 폐업일자, 
소재지전체주소, 도로명전체주소, 사업장명, 좌표정보X, 좌표정보Y
from drug_store;

select * from drug_store;

select * 
from drug_store
where 도로명전체주소 like '경기도%';

select 관리번호, 상세영업상태명, 폐업일자, 
    case when 도로명전체주소 like '서울%' then '서울특별시'
         when 도로명전체주소 like '경기도%' then '경기도'
         when 도로명전체주소 like '강원도%' then '강원도'
         when 도로명전체주소 like '경상남도%' then '경상남도'
         when 도로명전체주소 like '경상북도%' then '경상북도'
         when 도로명전체주소 like '충청남도%' then '충청남도'
         when 도로명전체주소 like '충청북도%' then '충청북도'
         when 도로명전체주소 like '전라남도%' then '전라남도'
         when 도로명전체주소 like '전라북도%' then '전라북도'
         when 도로명전체주소 like '광주광역시%' then '광주광역시'
         when 도로명전체주소 like '부산광역시%' then '부산광역시'
         when 도로명전체주소 like '대구광역시%' then '대구광역시'
         when 도로명전체주소 like '대전광역시%' then '대전광역시'
         when 도로명전체주소 like '울산광역시%' then '울산광역시'
         when 도로명전체주소 like '인천광역시%' then '인천광역시'
         when 도로명전체주소 like '세종%' then '세종특별자치시'
         when 도로명전체주소 like '제주%' then '제주특별시'
    else 도로명전체주소
    end as 시도별, 소재지전체주소, 도로명전체주소, 사업장명, 좌표정보X, 좌표정보Y
from drug_store;

select 관리번호, 상세영업상태명, 폐업일자, 
    case when 소재지전체주소 like '서울%' then '서울특별시'
         when 소재지전체주소 like '경기도%' then '경기도'
         when 소재지전체주소 like '강원도%' then '강원도'
         when 소재지전체주소 like '경상남도%' then '경상남도'
         when 소재지전체주소 like '경상북도%' then '경상북도'
         when 소재지전체주소 like '충청남도%' then '충청남도'
         when 소재지전체주소 like '충청북도%' then '충청북도'
         when 소재지전체주소 like '전라남도%' then '전라남도'
         when 소재지전체주소 like '전라북도%' then '전라북도'
         when 소재지전체주소 like '광주광역시%' then '광주광역시'
         when 소재지전체주소 like '부산광역시%' then '부산광역시'
         when 소재지전체주소 like '대구광역시%' then '대구광역시'
         when 소재지전체주소 like '대전광역시%' then '대전광역시'
         when 소재지전체주소 like '울산광역시%' then '울산광역시'
         when 소재지전체주소 like '인천광역시%' then '인천광역시'
         when 소재지전체주소 like '세종%' then '세종특별자치시'
         when 소재지전체주소 like '제주%' then '제주특별시'
    else 도로명전체주소
    end as 시도별, 소재지전체주소, 도로명전체주소, 사업장명, 좌표정보X, 좌표정보Y
from drug_store
where 도로명전체주소 is null;

select 관리번호, 상세영업상태명, 폐업일자, 
    case when 도로명전체주소 like '서울%' then '서울특별시'
         when 도로명전체주소 like '경기도%' then '경기도'
         when 도로명전체주소 like '강원도%' then '강원도'
         when 도로명전체주소 like '경상남도%' then '경상남도'
         when 도로명전체주소 like '경상북도%' then '경상북도'
         when 도로명전체주소 like '충청남도%' then '충청남도'
         when 도로명전체주소 like '충청북도%' then '충청북도'
         when 도로명전체주소 like '전라남도%' then '전라남도'
         when 도로명전체주소 like '전라북도%' then '전라북도'
         when 도로명전체주소 like '광주광역시%' then '광주광역시'
         when 도로명전체주소 like '부산광역시%' then '부산광역시'
         when 도로명전체주소 like '대구광역시%' then '대구광역시'
         when 도로명전체주소 like '대전광역시%' then '대전광역시'
         when 도로명전체주소 like '울산광역시%' then '울산광역시'
         when 도로명전체주소 like '인천광역시%' then '인천광역시'
         when 도로명전체주소 like '세종%' then '세종특별자치시'
         when 도로명전체주소 like '제주%' then '제주특별시'
         when 소재지전체주소 like '서울%' then '서울특별시'
         when 소재지전체주소 like '경기도%' then '경기도'
         when 소재지전체주소 like '강원도%' then '강원도'
         when 소재지전체주소 like '경상남도%' then '경상남도'
         when 소재지전체주소 like '경상북도%' then '경상북도'
         when 소재지전체주소 like '충청남도%' then '충청남도'
         when 소재지전체주소 like '충청북도%' then '충청북도'
         when 소재지전체주소 like '전라남도%' then '전라남도'
         when 소재지전체주소 like '전라북도%' then '전라북도'
         when 소재지전체주소 like '광주광역시%' then '광주광역시'
         when 소재지전체주소 like '부산광역시%' then '부산광역시'
         when 소재지전체주소 like '대구광역시%' then '대구광역시'
         when 소재지전체주소 like '대전광역시%' then '대전광역시'
         when 소재지전체주소 like '울산광역시%' then '울산광역시'
         when 소재지전체주소 like '인천광역시%' then '인천광역시'
         when 소재지전체주소 like '세종%' then '세종특별자치시'
         when 소재지전체주소 like '제주%' then '제주특별시'
    else 도로명전체주소
    end as 시도별, 소재지전체주소, 도로명전체주소, 사업장명, 좌표정보X, 좌표정보Y
from drug_store;


UPDATE drug_store
    set 상세영업상태명 = '폐업' 
WHERE 상세영업상태명 = '직권폐업';

select * from 
drug_store
where 소재지전체주소 like '황해도%' and 상세영업상태설명 = '영업중';