PAYMENTS_BY_LOAN_DB_VIEW = "           \
    CREATE OR REPLACE                  \
    VIEW payments_by_loan_db_view      \
    AS SELECT                          \
        row_number() OVER () as id,    \
        lp.loan_id as loan,            \
        SUM (lp.value) as total_payd   \
    FROM loans_payment lp              \
    GROUP BY loan;"
