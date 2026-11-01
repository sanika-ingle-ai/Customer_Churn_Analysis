SELECT
    PaperlessBilling,
    COUNT(*) AS Total_Customers,
    SUM(CASE WHEN Churn = 'Yes' THEN 1 ELSE 0 END) AS Churned_Customers,
    CAST(
        SUM(CASE WHEN Churn = 'Yes' THEN 1.0 ELSE 0 END) * 100 / COUNT(*)
        AS DECIMAL(5,2)
    ) AS Churn_Rate
FROM dbo.TelcoCustomerChurn
GROUP BY PaperlessBilling
ORDER BY Churn_Rate DESC;