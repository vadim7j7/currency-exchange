select_bank_by__id = '''SELECT banks.* FROM banks WHERE banks._id = $1'''
insert_bank = '''INSERT INTO banks (_id, name) VALUES ($1, $2)'''
update_bank = '''UPDATE banks SET name = $2 WHERE banks.id = $1'''

select_current_currency_by_bank_id_and_code = (
    '''SELECT * FROM current_currencies
WHERE current_currencies.bank_id = $1 AND current_currencies.code = $2''')

insert_current_currency = (
    '''INSERT INTO current_currencies (bank_id, code, value)
VALUES ($1, $2, $3)''')

update_current_currency = (
    '''UPDATE current_currencies SET value = $2
WHERE current_currencies.id = $1'''
)
