INSERT INTO
    core_user (
        username,
        email,
        first_name,
        last_name,
        password,
        is_staff,
        is_superuser,
        is_active,
        date_joined
    )
SELECT 'user_' || i, 'user' || i || '@example.com', 'First Name ' || i, 'Last Name ' || i, md5(random()::TEXT), FALSE, FALSE, TRUE, NOW()
FROM generate_series(1, 100) AS i;

WITH
    posts AS (
        SELECT u.id, 'Random Post ' || i, 'Content of the post ' || i, NOW(), NOW()
        FROM generate_series(1, 100) AS i
            JOIN core_user u ON TRUE
        ORDER BY RANDOM()
        LIMIT 1000
    )
INSERT INTO
    core_post (
        author_id,
        title,
        content,
        created_at,
        updated_at
    )
SELECT *
FROM posts;

WITH
    comments AS (
        SELECT u.id, p.id, 'Comment ' || i, NOW(), NOW()
        FROM generate_series(1, 100) AS i
            JOIN core_user u ON TRUE
            JOIN core_post p ON TRUE
        ORDER BY RANDOM()
        LIMIT 10000
    )
INSERT INTO
    core_comment (
        author_id,
        post_id,
        content,
        created_at,
        updated_at
    )
SELECT *
FROM comments;

WITH
    pairs AS (
        SELECT p.id, u.id
        FROM generate_series(1, 100) AS i
            JOIN core_post p ON TRUE
            JOIN core_user u ON TRUE
        ORDER BY RANDOM()
        LIMIT 1000
    )
INSERT INTO
    core_post_likes (post_id, user_id)
SELECT *
FROM pairs
ON CONFLICT (post_id, user_id) DO NOTHING;

WITH
    pairs AS (
        SELECT c.id, u.id
        FROM
            generate_series(1, 100) AS i
            JOIN core_post p ON TRUE
            JOIN core_user u ON TRUE
            JOIN core_comment c ON c.post_id = p.id
        ORDER BY RANDOM()
        LIMIT 1000
    )
INSERT INTO
    core_comment_likes (comment_id, user_id)
SELECT *
FROM pairs
ON CONFLICT (comment_id, user_id) DO NOTHING;