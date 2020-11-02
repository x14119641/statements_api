INSERT INTO users (username, password)
VALUES
  ('test', 'pbkdf2:sha256:50000$TCI4GzcX$0de171a4f4dac32e3364c7ddc7c14f3e2fa61f2d17574483f7ffbb431b4acb2f'),
  ('other', 'pbkdf2:sha256:50000$kJPKsz6N$d2d4784f1b030a9761f5ccaeeaca413f27f2ecb76d6168407af962ddce849f79');


INSERT INTO customers (customer_id, customer_name, participation, document, adress, emails, phones)
VALUES
  (1, 'test user', 'Titular', 'Y3334444K', "C/test, 1", "test@test.com", "+3312312312"),
  (2, 'other user', 'Titular', 'Y3335555T', "C/other, 2", "other@test.com", "+3823568901");

INSERT INTO accounts (account_id, account_name, iban, currency)
VALUES
  (1, 'Personal Account', 'ES232100123303030000', "EUR"),
  (1, 'Savings Account', 'ES232100123303030001', "EUR"),
  (2, 'Personal Account', 'ES232100123303030088', "EUR");

INSERT INTO statements (statement_id, created, concept, amount, balance)
VALUES
  (1, '2018-01-01 00:01:00', 'test concept', 23.5, 173.5),
  (1, '2018-01-01 00:00:00', 'test concept 2', -20, 150),
  (2, '2018-01-01 00:01:00', 'other concept', 100, 100),
  (2, '2018-01-01 00:00:00', 'other concept 2', -20, 0);
  