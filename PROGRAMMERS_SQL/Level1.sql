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
https://programmers.co.kr/learn/courses/30/lessons/59036
SELECT ANIMAL_ID, NAME from ANIMAL_INS where INTAKE_CONDITION = 'SICK' order by ANIMAL_ID
'''