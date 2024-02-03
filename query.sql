WITH query AS (
    SELECT
        total_money_amount * 0.01 AS amount,
        strftime('%Y-%m-%d', closed_at) AS date,
        strftime('%Y', closed_at) AS year,
        strftime('%m', closed_at) AS month,
        strftime('%d', closed_at) AS day
    FROM transactions
)

SELECT
    SUM(amount) AS total,
    month,
    year,
    day
FROM query
GROUP BY year, month, day
