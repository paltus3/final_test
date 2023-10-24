-- Задание1
SELECT
    c.login,
    COUNT(*)
FROM
    "Couriers" AS c
JOIN
    "Orders" AS o ON c.id = o."courierId"
WHERE
    o."inDelivery" = true
GROUP BY
    c.login;


-- Задание2
SELECT track,
CASE
    WHEN finished = true THEN 2
    WHEN cancelled = true THEN -1
    WHEN "inDelivery" = true THEN 1
    ELSE 0
END as status
FROM "Orders";
