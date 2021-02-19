-- 우유와 요거트가 담긴 장바구니
'''
https://programmers.co.kr/learn/courses/30/lessons/62284
-- 코드를 입력하세요
SELECT A.CART_ID FROM (SELECT CART_ID FROM CART_PRODUCTS WHERE NAME = 'Milk') AS A
JOIN (SELECT CART_ID FROM CART_PRODUCTS WHERE NAME = 'Yogurt') AS B
ON (A.CART_ID = B.CART_ID)ORDER BY A.CART_ID
'''

--보호소에서 중성화한 동물

'''
https://programmers.co.kr/learn/courses/30/lessons/59045
-- 코드를 입력하세요
SELECT A.ANIMAL_ID, A.ANIMAL_TYPE, A.NAME FROM ANIMAL_OUTS AS A
JOIN ANIMAL_INS AS B on A.ANIMAL_ID = B.ANIMAL_ID
WHERE A.SEX_UPON_OUTCOME IN ('Spayed Female', 'Neutered Male')
AND B.SEX_UPON_INTAKE IN ('Intact Male', 'Intact Female')
ORDER BY ANIMAL_ID;
'''

--입양 시각 구하기(2)----------->다시풀기
'''
https://programmers.co.kr/learn/courses/30/lessons/59413?language=oracle
-- 코드를 입력하세요
SELECT A.HOUR, COUNT(O.ANIMAL_ID) AS COUNT
FROM (SELECT ROWNUM - 1 AS HOUR FROM DUAL CONNECT BY LEVEL <= 24) A
LEFT JOIN ANIMAL_OUTS O ON (A.HOUR = EXTRACT(HOUR FROM CAST(O.DATETIME AS TIMESTAMP)))
GROUP BY A.HOUR
ORDER BY A.HOUR


'''
