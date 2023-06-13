#!/usr/bin/python
import logging

###############################################################################
# TOOLS DEFINITIONS
###############################################################################
logger = logging.getLogger('django')

###############################################################################
# TOOLS DEFINITIONS
###############################################################################

NUCLEI_TEMPLATES_PATH = '/root/nuclei-templates/'
###############################################################################
# YAML CONFIG DEFINITIONS
###############################################################################

ALL = 'all'

SUBDOMAIN_DISCOVERY = 'subdomain_discovery'
PORT_SCAN = 'port_scan'
SCREENSHOT = 'screenshot'
DIR_FILE_FUZZ = 'dir_file_fuzz'
FETCH_URL = 'fetch_url'
INTENSITY = 'intensity'

USES_TOOLS = 'uses_tools'
THREADS = 'threads'
AMASS_WORDLIST = 'amass_wordlist'
NAABU_RATE = 'rate'
PORT = 'Port'
PORTS = 'ports'
EXCLUDE_PORTS = 'exclude_ports'

EXTENSIONS = 'extensions'
USE_EXTENSIONS = 'use_extensions'
EXCLUDE_EXTENSIONS = 'exclude_extensions'
STOP_ON_ERROR = 'stop_on_error'
DELAY = 'delay'
MATCH_HTTP_STATUS = 'match_http_status'
AUTO_CALIBRATION = 'auto_calibration'
FOLLOW_REDIRECT = 'follow_redirect'

RECURSIVE = 'recursive'
RECURSIVE_LEVEL = 'recursive_level'
WORDLIST = 'wordlist'

TIMEOUT = 'timeout'
MAX_TIME = 'max_time'
EXCLUDED_SUBDOMAINS = 'excluded_subdomains'
EXCLUDE_TEXT = 'exclude_text'
IGNORE_FILE_EXTENSION = 'ignore_file_extension'
GF_PATTERNS = 'gf_patterns'

VULNERABILITY_SCAN = 'vulnerability_scan'
CUSTOM_NUCLEI_TEMPLATE = 'custom_templates'
NUCLEI_TEMPLATE = 'templates'
NUCLEI_SEVERITY = 'severity'
NUCLEI_CONCURRENCY = 'concurrency'
RATE_LIMIT = 'rate_limit'
RETRIES = 'retries'

OSINT = 'osint'
OSINT_DOCUMENTS_LIMIT = 'documents_limit'
OSINT_DISCOVER = 'discover'
OSINT_DORK = 'dork'

USE_AMASS_CONFIG = 'use_amass_config'
USE_SUBFINDER_CONFIG = 'use_subfinder_config'
USE_NUCLEI_CONFIG = 'use_nuclei_config'
USE_NAABU_CONFIG = 'use_naabu_config'

CUSTOM_HEADER = 'custom_header'

###############################################################################
# Wordlist DEFINITIONS
###############################################################################
AMASS_DEFAULT_WORDLIST_PATH = 'wordlist/default_wordlist/deepmagic.com-prefixes-top50000.txt'


###############################################################################
# Logger DEFINITIONS
###############################################################################

CONFIG_FILE_NOT_FOUND = 'Config file not found'

###############################################################################
# Preferences DEFINITIONS
###############################################################################

SMALL = '100px'
MEDIM = '200px'
LARGE = '400px'
XLARGE = '500px'

###############################################################################
# Interesting Subdomain DEFINITIONS
###############################################################################
MATCHED_SUBDOMAIN = 'Subdomain'
MATCHED_PAGE_TITLE = 'Page Title'

###############################################################################
# Celery Task Status CODES
###############################################################################
INITIATED_TASK = -1
FAILED_TASK = 0
RUNNING_TASK = 1
SUCCESS_TASK = 2
ABORTED_TASK = 3
###############################################################################
# Uncommon Ports
# Source: https://github.com/six2dez/reconftw/blob/main/reconftw.cfg
###############################################################################
UNCOMMON_WEB_PORTS = [
    7,
    19,
    21,
    22,
    23,
    37,
    79,
    81,
    135,
    137,
    139,
    445,
    801,
    1433,
    1434,
    2000,
    2001,
    2003,
    2041,
    2200,
    2222,
    3000,
    3306,
    3389,
    3390,
    4000,
    4444,
    4445,
    5000,
    5001,
    5002,
    5100,
    5432,
    6000,
    6668,
    6879,
    6881,
    7001,
    7002,
    7676,
    8000,
    8080,
    8081,
    8443,
    9877,
    9878,
    10000,
    20000]

###############################################################################
# WHOIS DEFINITIONS
# IGNORE_WHOIS_RELATED_KEYWORD: To ignore and disable finding generic related domains
###############################################################################

IGNORE_WHOIS_RELATED_KEYWORD = [
    'Registration Private',
    'Domains By Proxy Llc',
    'Redacted For Privacy',
    'Digital Privacy Corporation',
    'Private Registrant',
    'Domain Administrator',
    'Administrator',
]
