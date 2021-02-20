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


--없어진 기록 찾기
'''
https://programmers.co.kr/learn/courses/30/lessons/59042
SELECT A.ANIMAL_ID, A.NAME FROM ANIMAL_OUTS A
LEFT OUTER JOIN ANIMAL_INS AS B ON (A.ANIMAL_ID = B.ANIMAL_ID)
WHERE B.ANIMAL_ID IS NULL

--or 
SELECT animal_id , name from animal_outs where animal_id not in (select animal_id from animal_ins)
'''

--있었는데요 없었습니다
'''
https://programmers.co.kr/learn/courses/30/lessons/59043
-- 코드를 입력하세요
SELECT A.ANIMAL_ID, A.NAME FROM ANIMAL_INS AS A
LEFT JOIN ANIMAL_OUTS AS B ON A.ANIMAL_ID = B.ANIMAL_ID
WHERE A.DATETIME > B.DATETIME 
ORDER BY A.DATETIME;
'''