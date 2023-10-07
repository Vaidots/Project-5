import os
# List of environment variables that are used by the script,
# and their values
ENVIRONMENT_VARIABLES = {
    'AWS_ACCESS_KEY_ID': 'AKIA2JYRTZN3V4YY4DY4',
    'AWS_SECRET_ACCESS_KEY': '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',
    'DATABASE_URL': 'postgres://gchlemjl:680tpDyJh1LfFn-cHnP1JEY4LhySkJE1@horton.db.elephantsql.com/gchlemjl',
    'EMAIL_HOST_PASS': 'ylapagkkbjahunbu',
    'EMAIL_HOST_USER': 'vaidots30@gmail.com',
    'STRIPE_PUBLIC_KEY': 'pk_test_51NCR5jEMWAjbu1sbkqpOnXIrATOjJKgXcOADVghOr4ZRgJTet051tFnRIBT90LNrCl1G1sAPNjj96lszflmVxtRw00kcI2umBo',
    'STRIPE_SECRET_KEY': 'sk_test_51NCR5jEMWAjbu1sb5YA9WWIPURwZ2iX63l1cPzwJ5iLGqJSWIBHZoKPWlnlZDD54GKMhHj6E9NgpLjRDjR6QDkEu00CPWi00zT',
    'STRIPE_WH_SECRET': 'whsec_O0ZrBWKsCcaBIJ2D8QcgO34lLkMFMmFW',
    'USE_AWS': 'True',
    'DJANGO_SECRET_KEY': 'asdswr*zz3u4yie-$()@cy^l(+x9&@6ypx+r0lmhardsehbd'

}


# For all the environment variables above, add them to the Python environment
for variable_key, variable_value in ENVIRONMENT_VARIABLES.items():
    os.environ.setdefault(variable_key, variable_value)