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
