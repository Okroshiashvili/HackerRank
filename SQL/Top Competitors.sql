


SELECT s.hacker_id, h.name
FROM Submissions s
JOIN Challenges c
ON s.challenge_id = c.challenge_id
JOIN difficulty d
ON c.difficulty_level = d.difficulty_level 
AND s.score = d.score 
JOIN Hackers h
ON s.hacker_id = h.hacker_id
GROUP BY h.hacker_id, h.name
HAVING count(h.hacker_id) > 1
ORDER BY count(h.hacker_id) DESC, h.hacker_id ASC;




