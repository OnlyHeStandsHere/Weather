-- replace all nan with NULL
UPDATE weather.raw
  SET Rain1h = NULL
WHERE Rain1h = 'nan'

UPDATE weather.raw
  SET Rain3h = NULL
WHERE Rain3h = 'nan'

UPDATE weather.raw
  SET Rain24h = NULL
WHERE Rain24h = 'nan'

UPDATE weather.raw
  SET RainToday = NULL
WHERE RainToday = 'nan'

UPDATE weather.raw
  SET Snow1h = NULL
WHERE Snow1h = 'nan'

UPDATE weather.raw
  SET Snow3h = NULL
WHERE Snow3h = 'nan'


-- look for duplicate records, there sould only be one time stamp per hour in the raw table
  SELECT COUNT(LinuxTime),
	     LinuxTime
    FROM weather.raw
GROUP BY LinuxTime
  HAVING COUNT(LinuxTime) > 4

-- check for duplicates one more time
; WITH CTE AS
(
  SELECT *,  ROW_NUMBER() OVER (PARTITION BY LinuxTime ORDER BY ID) AS RowNum
  FROM weather.raw
)
SELECT * FROM CTE ORDER BY ID

--explore what the duplicates look like
SELECT r.*,
      ROW_NUMBER() OVER (PARTITION BY r.LinuxTime ORDER BY ID) AS RowNum
  FROM weather.raw r
       INNER JOIN (
         SELECT COUNT(LinuxTime) AS dupCount,
                LinuxTime
            FROM weather.raw
        GROUP BY LinuxTime
          HAVING COUNT(LinuxTime) > 2
      ) duplicates ON duplicates.LinuxTime = r.LinuxTime









select * from weather.raw r inner join weather.main m on r.LinuxTime = m.LinuxTime order by r.LinuxTime


select left(dtos, 20) from weather.raw

select * from weather.raw