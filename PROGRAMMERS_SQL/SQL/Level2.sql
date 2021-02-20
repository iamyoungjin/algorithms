--동명 동물 수 찾기
'''
https://programmers.co.kr/learn/courses/30/lessons/59041
-- 코드를 입력하세요
SELECT NAME, COUNT(NAME) AS COUNT FROM ANIMAL_INS
WHERE NAME IS NOT NULL GROUP BY NAME HAVING COUNT(NAME) > 1
ORDER BY NAME ASC;
'''

--NULL 처리하기
'''
https://programmers.co.kr/learn/courses/30/lessons/59410
SELECT ANIMAL_TYPE
      ,CASE WHEN NAME IS NULL THEN 'No name' else NAME END NAME
      ,SEX_UPON_INTAKE
FROM ANIMAL_INS

'''


--DATETIME에서 DATE로 형 변환
'''
https://programmers.co.kr/learn/courses/30/lessons/59414
-- 코드를 입력하세요
SELECT ANIMAL_ID, NAME, DATE_FORMAT(DATETIME,"%Y-%m-%d") as '날짜' FROM ANIMAL_INS ORDER BY ANIMAL_ID
'''

--이름에 el이 들어가는 동물 찾기
'''
https://programmers.co.kr/learn/courses/30/lessons/59047
-- 코드를 입력하세요
SELECT ANIMAL_ID, NAME FROM ANIMAL_INS
WHERE NAME LIKE '%EL%' AND ANIMAL_TYPE = 'Dog'
ORDER BY NAME
'''

--중성화 여부 파악하기
'''
https://programmers.co.kr/learn/courses/30/lessons/59409
-- 코드를 입력하세요
SELECT ANIMAL_ID, NAME
    , (CASE WHEN SEX_UPON_INTAKE LIKE '%ed%' THEN 'O' ELSE 'X'END) AS "중성화"
    FROM ANIMAL_INS
    ORDER BY ANIMAL_ID ASC;
'''

--입양 시각 구하기(1)
'''
https://programmers.co.kr/learn/courses/30/lessons/59412
-- 코드를 입력하세요
SELECT HOUR(datetime) AS HOUR, COUNT(HOUR(datetime)) AS COUNT FROM ANIMAL_OUTS
GROUP BY HOUR HAVING HOUR BETWEEN 9 AND 19
ORDER BY HOUR
'''

--루시와 엘라 찾기
'''
https://programmers.co.kr/learn/courses/30/lessons/59046
-- 코드를 입력하세요
select animal_id, name, sex_upon_intake
from animal_ins
where name in ('Lucy', 'Ella', 'Pickle', 'Sabrina', 'Mitty', 'Rogan')
order by animal_id

'''