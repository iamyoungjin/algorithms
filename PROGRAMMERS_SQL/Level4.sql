-- 우유와 요거트가 담긴 장바구니
'''
https://programmers.co.kr/learn/courses/30/lessons/62284
-- 코드를 입력하세요
SELECT A.CART_ID FROM (SELECT CART_ID FROM CART_PRODUCTS WHERE NAME = 'Milk') AS A
JOIN (SELECT CART_ID FROM CART_PRODUCTS WHERE NAME = 'Yogurt') AS B
ON (A.CART_ID = B.CART_ID)ORDER BY A.CART_ID
'''