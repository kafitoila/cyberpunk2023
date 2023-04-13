/* DO $$ BEGIN
    CREATE TYPE insurance AS ENUM ('Нет', 'Серебро', 'Золото', 'Платина');
EXCEPTION
    WHEN duplicate_object THEN null;
END $$; */

CREATE TABLE IF NOT EXISTS users(
    user_id     INTEGER PRIMARY KEY,
    secret_id   CHAR(6),
    tg_id       BIGINT,
    user_name   VARCHAR(128),
    ref_name    VARCHAR(128),
    irl_name    VARCHAR(128),
    is_dead     BOOLEAN,
    is_test     BOOLEAN,
    addiction   SMALLINT,  /* 0 - no addiction; 1, 2, etc - amount of doses required */
    insurance   VARCHAR(32),
    group_id    SMALLINT,
    group_name  VARCHAR(128),
    cyberpsycho SMALLINT
);

/* DO $$ BEGIN
    IF NOT EXISTS (SELECT user_id FROM users) THEN COPY users FROM 'users.csv' DELIMITER ',' CSV HEADER;
	END IF;
END $$; */

CREATE TABLE IF NOT EXISTS accounts(
    account_id SMALLSERIAL PRIMARY KEY,
    user_id    INTEGER,
    balance    INTEGER,
    is_blocked BOOLEAN,
    salary     INTEGER
);

/* DO $$ BEGIN
    IF NOT EXISTS (SELECT account_id FROM accounts) THEN COPY accounts FROM 'accounts.csv' DELIMITER ',' CSV HEADER;
	END IF;
END $$; */

CREATE TABLE IF NOT EXISTS organizations(
    account_id SMALLSERIAL PRIMARY KEY,
    user_id         INTEGER,
    balance         INTEGER,
    is_blocked      BOOLEAN,
    user1           INTEGER,
    user2           INTEGER,
    user3           INTEGER,
    group_id        SMALLINT,
    org_name        VARCHAR(128),
    special_balance INTEGER
);

/* DO $$ BEGIN
    IF NOT EXISTS (SELECT account_id FROM organizations) THEN COPY organizations FROM 'organizations.csv' DELIMITER ',' CSV HEADER;
	END IF;
END $$; */

CREATE TABLE IF NOT EXISTS transactions(
    transaction_id      SERIAL PRIMARY KEY,
    sender_id           INTEGER,
    sender_account_id   INTEGER,
    receiver_id         INTEGER,
    receiver_account_id INTEGER,
    amount              INTEGER,
    created_at          TIMESTAMPTZ,
    comment             VARCHAR(1024)
);