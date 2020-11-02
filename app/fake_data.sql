INSERT INTO users (username, password)
VALUES
  ('user', 'pbkdf2:sha256:150000$n3M28Zto$1b41bf9f6dfc34985f3096bf117f3b42a69419e85a5fd3aa372d791e22a3259e'),
  ('user2', 'pbkdf2:sha256:150000$7wnYfrAt$8dcccddb3de01c352be30145d1f88e942e32fe82b3103caa3ee9b38445c28caf'
);


INSERT INTO customers (customer_id, customer_name, participation, document, adress, emails, phones)
VALUES
  (1, 'user name ', 'Titular', 'Y2224444K', "C/user street, 1", "user@test.com", "+3912312312"),
  (2, 'user2 name', 'Titular', 'Y3339999L', "C/user2, 2", "user2@test.com", "+3163568901");


INSERT INTO accounts (account_id, account_name, iban, currency)
VALUES
  (1, 'Personal Account', 'ES232100123303030000', "EUR"),
  (1, 'Savings Account', 'ES232100123303030001', "EUR"),
  (2, 'Personal Account', 'ES232100123303030088', "EUR");


INSERT INTO statements (statement_id, created, concept, amount, balance)
VALUES
  (1, '2018-01-02 00:01:00', 'Donation', 23.5, 173.5),
  (1, '2018-01-01 00:01:00', 'Supermarket', -20, 150),
  (1, '2018-01-01 00:00:00', 'Food', -10, 160),
  (2, '2018-01-01 00:01:00', 'Cash transfer', 100, 100),
  (2, '2018-01-01 00:00:00', 'Pharmacy', -20, 0);
  