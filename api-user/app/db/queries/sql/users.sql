-- name: get-user-by-phone^
SELECT
    id,
    username,
    email,
    phone,
    wechat,
    salt,
    hashed_password,
    bio,
    image,
    created_at,
    updated_at
FROM
    users
WHERE
    phone = :phone
LIMIT
    1;

-- name: get-user-by-username^
SELECT
    id,
    username,
    email,
    phone,
    wechat,
    salt,
    hashed_password,
    bio,
    image,
    created_at,
    updated_at
FROM
    users
WHERE
    username = :username
LIMIT
    1;

-- name: create-new-user<!
INSERT INTO
    users (username, phone, wechat, salt, hashed_password)
VALUES
    (:username, :phone, :wechat :salt, :hashed_password) RETURNING id,
    created_at,
    updated_at;

-- name: update-user-by-username<!
UPDATE
    users
SET
    username = :new_username,
    email = :new_email,
    phone = :new_phone,
    wechat = :new_wechat,
    salt = :new_salt,
    hashed_password = :new_password,
    bio = :new_bio,
    image = :new_image
WHERE
    username = :username RETURNING updated_at;