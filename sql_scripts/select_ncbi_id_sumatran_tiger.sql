-- To find the nbci_id for the Sumatran tiger, we can use the LIKE statement 
-- and the biological species name (Panthera tigris sumatrae)

SELECT ncbi_id 
FROM taxonomy 
WHERE species LIKE 'Panthera tigris sumatrae%';