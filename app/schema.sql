DROP TABLE IF EXISTS users;
DROP TABLE IF EXISTS customers;
DROP TABLE IF EXISTS accounts;
DROP TABLE IF EXISTS statements;


CREATE TABLE users (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  username TEXT UNIQUE NOT NULL,
  password TEXT NOT NULL
);


CREATE TABLE customers (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  customer_id INTEGER NOT NULL,
  customer_name TEXT NOT NULL,
  participation TEXT NOT NULL,
  document TEXT NOT NULL,
  adress TEXT NOT NULL,
  emails TEXT NOT NULL,
  phones TEXT NOT NULL,
  FOREIGN KEY (customer_id) REFERENCES user (id)
);


CREATE TABLE accounts (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  account_id INTEGER NOT NULL,
  account_name TEXT NOT NULL,
  iban TEXT NOT NULL,
  currency TEXT NOT NULL,
  FOREIGN KEY (account_id) REFERENCES user (id)
);


CREATE TABLE statements (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  statement_id INTEGER NOT NULL,
  created TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
  concept TEXT NOT NULL,
  amount INTEGER NOT NULL,
  balance INTEGER NOT NULL,
  FOREIGN KEY (statement_id) REFERENCES user (id)
);