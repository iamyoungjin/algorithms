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