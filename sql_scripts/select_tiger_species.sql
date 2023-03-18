-- The biological species name for tigers is Panthera tigris
-- Using this, we can identify different sub-species of tigers in the database

SELECT COUNT(*) AS num_unique_tiger_species
FROM taxonomy
WHERE species LIKE 'Panthera tigris%';