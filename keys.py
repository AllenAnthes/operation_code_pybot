from decouple import config

# app verification tokens
# VERIFICATION_TOKEN = config('OPCODE_VERIFICATION_TOKEN')
VERIFICATION_TOKEN = config('APP_VERIFICATION_TOKEN')

# from src.airtable_handling import airtable

# Workspace token selection
TOKEN = config('PERSONAL_APP_TOKEN')
# TOKEN = config('OPCODE_APP_TOKEN')

# community channel selections
COMMUNITY_CHANNEL = config('PERSONAL_PRIVATE_CHANNEL')
# COMMUNITY_CHANNEL = config('OPCODE_REWRITE_CHANNEL')
# PROJECTS_CHANNEL = config('OPCODE_OC_PROJECTS_CHANNEL')
# COMMUNITY_CHANNEL = config('OPCODE_COMMUNITY_ID')
# COMMUNITY_CHANNEL = config('OPCODE_BOT_TESTING_CHANNEL')

# airtable config selectrions
AIRTABLE_BASE_KEY = config('PERSONAL_AIRTABLE_BASE_KEY')
AIRTABLE_API_KEY = config('PERSONAL_AIRTABLE_TOKEN')
AIRTABLE_TABLE_NAME = 'Mentor Request'
#AIRTABLE_BASE_KEY = config('OPCODE__AIRTABLE_BASE_KEY')
#AIRTABLE_API_KEY = config('OPCODE_AIRTABLE_TOKEN')
#AIRTABLE_TABLE_NAME = 'Mentor Request'