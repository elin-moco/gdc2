.headers on
.mode csv

-- Gets the top 200 repos by number of forks
SELECT repo_url, COUNT(repo_url) AS cnt
FROM event
WHERE 
  -- Some URLs are in the database with the username
  -- incorrectly stripped
  repo_url NOT LIKE 'https://github.com//%'
GROUP BY repo_url
ORDER BY cnt DESC
LIMIT 200;
