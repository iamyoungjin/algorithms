--모든 레코드 조회하기
문제
'''
https://programmers.co.kr/learn/courses/30/lessons/59034
-- 코드를 입력하세요
SELECT * from ANIMAL_INS order by ANIMAL_ID
'''

--최댓값 구하기
'''
https://programmers.co.kr/learn/courses/30/lessons/59415
-- 코드를 입력하세요
SELECT DATETIME AS 시간 FROM ANIMAL_INS
WHERE DATETIME = (SELECT MAX(DATETIME) from ANIMAL_INS)
'''

--역순 정렬하기
'''
https://programmers.co.kr/learn/courses/30/lessons/59035
-- 코드를 입력하세요
SELECT name, datetime from ANIMAL_INS order by ANIMAl_ID desc
'''

--아픈 동물 찾기
'''
-- 코드를 입력하세요

https://programmers.co.kr/learn/courses/30/lessons/59036
SELECT ANIMAL_ID, NAME from ANIMAL_INS where INTAKE_CONDITION = 'SICK' order by ANIMAL_ID
'''

--어린 동물 찾기
'''
https://programmers.co.kr/learn/courses/30/lessons/59037
-- 코드를 입력하세요
SELECT ANIMAL_ID, NAME  from ANIMAL_INS
where INTAKE_CONDITION != 'Aged' order by ANIMAL_ID

'''

--동물의 아이디와 이름
'''
https://programmers.co.kr/learn/courses/30/lessons/59403
-- 코드를 입력하세요
SELECT ANIMAL_ID, NAME FROM ANIMAL_INS ORDER BY ANIMAL_ID
'''

--여러 기준으로 정렬하기
'''
https://programmers.co.kr/learn/courses/30/lessons/59404
-- 코드를 입력하세요
SELECT ANIMAL_ID, NAME, DATETIME FROM ANIMAL_INS
ORDER BY NAME, DATETIME DESC
'''

--상위 n개 레코드
'''
https://programmers.co.kr/learn/courses/30/lessons/59405
-- 코드를 입력하세요
SELECT NAME FROM ANIMAL_INS ORDER BY DATETIME LIMIT 1
'''