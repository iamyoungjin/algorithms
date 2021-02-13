--오랜 기간 보호한 동물(1)
'''
https://programmers.co.kr/learn/courses/30/lessons/59044
SELECT A.NAME, A.DATETIME FROM ANIMAL_INS A
LEFT JOIN ANIMAL_OUTS B ON A.ANIMAL_ID = B.ANIMAL_ID
WHERE B.ANIMAL_ID IS NULL ORDER BY A.DATETIME limit 3
'''

--오랜 기간 보호한 동물(2)
'''
https://programmers.co.kr/learn/courses/30/lessons/59411
-- 코드를 입력하세요
SELECT A.ANIMAL_ID , A.NAME FROM ANIMAL_OUTS as A
JOIN ANIMAL_INS as B ON A.ANIMAL_ID = B.ANIMAL_ID 
ORDER BY (A.DATETIME - B.DATETIME) desc LIMIT 2;
'''