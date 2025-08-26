"""
Configuration file for Entity Extractor
Customize settings here for different use cases
"""

# Scraping Configuration
SCRAPING_CONFIG = {
    # Request settings
    'REQUEST_TIMEOUT': 30,  # seconds
    'MAX_RETRIES': 3,
    'RETRY_DELAY': 2,  # seconds
    
    # Selenium settings
    'SELENIUM_WAIT_TIME': 3,  # seconds
    'SELENIUM_SCROLL_PAUSE': 2,  # seconds
    'CHROME_HEADLESS': True,
    'CHROME_WINDOW_SIZE': '1920,1080',
    
    # Data processing
    'MIN_ENTITY_NAME_LENGTH': 3,
    'MIN_ADDRESS_LENGTH': 10,
    'MAX_RESULTS_PER_SOURCE': 1000,
    
    # User agents (will be randomly selected)
    'USER_AGENTS': [
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
        'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    ]
}

# Predefined Sources for Different Entity Types
PREDEFINED_SOURCES = {
    'hospital': [
        {
            'name': 'NABH Accredited Hospitals',
            'url': 'https://nabh.co/hospitals-accredited-list/',
            'description': 'National Accreditation Board for Hospitals & Healthcare Providers',
            'requires_selenium': False
        },
        {
            'name': 'JCI Accredited Organizations',
            'url': 'https://www.jci.org/accredited-organizations',
            'description': 'Joint Commission International',
            'requires_selenium': True
        },
        {
            'name': 'Quality Check Hospitals',
            'url': 'https://www.qualitycheck.org/find-a-hospital/',
            'description': 'The Joint Commission Quality Check',
            'requires_selenium': True
        }
    ],
    
    'insurance': [
        {
            'name': 'IRDAI',
            'url': 'https://www.irdai.gov.in/',
            'description': 'Insurance Regulatory and Development Authority of India',
            'requires_selenium': False
        },
        {
            'name': 'PolicyBazaar',
            'url': 'https://www.policybazaar.com/',
            'description': 'Insurance comparison platform',
            'requires_selenium': True
        }
    ],
    
    'bank': [
        {
            'name': 'RBI',
            'url': 'https://rbi.org.in/',
            'description': 'Reserve Bank of India',
            'requires_selenium': False
        },
        {
            'name': 'BankBazaar',
            'url': 'https://www.bankbazaar.com/',
            'description': 'Banking and financial services',
            'requires_selenium': True
        }
    ],
    
    'school': [
        {
            'name': 'CBSE Schools',
            'url': 'https://cbse.gov.in/',
            'description': 'Central Board of Secondary Education',
            'requires_selenium': False
        }
    ],
    
    'pharmacy': [
        {
            'name': 'CDSCO',
            'url': 'https://cdsco.gov.in/',
            'description': 'Central Drugs Standard Control Organization',
            'requires_selenium': False
        }
    ]
}

# Address Pattern Recognition
ADDRESS_PATTERNS = {
    # Street patterns
    'streets': [
        r'\d+\s+[A-Za-z\s]+(?:Street|Road|Avenue|Lane|Drive|Boulevard|Colony|Nagar|Area|Sector|Phase)',
        r'[A-Za-z\s]+(?:Street|Road|Avenue|Lane|Drive|Boulevard|Colony|Nagar|Area|Sector|Phase)\s+\d+'
    ],
    
    # Building patterns
    'buildings': [
        r'\d+\s+[A-Za-z\s]+(?:Floor|Building|Complex|Mall|Plaza|Tower|Block)',
        r'[A-Za-z\s]+(?:Floor|Building|Complex|Mall|Plaza|Tower|Block)\s+\d+'
    ],
    
    # Location patterns
    'locations': [
        r'[A-Za-z\s]+(?:District|State|City|PIN|Postal Code|Zone|Ward)',
        r'\d{6}',  # PIN codes
        r'[A-Za-z\s]+(?:Mumbai|Delhi|Bangalore|Chennai|Kolkata|Hyderabad|Pune|Ahmedabad)'
    ]
}

# Data Cleaning Rules
CLEANING_RULES = {
    # Characters to remove
    'remove_chars': ['\n', '\r', '\t', '\xa0'],
    
    # Characters to replace
    'replace_chars': {
        '&amp;': '&',
        '&lt;': '<',
        '&gt;': '>',
        '&quot;': '"',
        '&#39;': "'"
    },
    
    # Text normalization
    'normalize_whitespace': True,
    'remove_extra_spaces': True,
    'strip_leading_trailing': True
}

# Export Configuration
EXPORT_CONFIG = {
    'excel': {
        'sheet_name': 'Scraped_Data',
        'include_index': False,
        'auto_adjust_columns': True
    },
    'csv': {
        'encoding': 'utf-8',
        'include_index': False
    },
    'filename_template': 'entities_{search_term}_{timestamp}'
}

# Logging Configuration
LOGGING_CONFIG = {
    'level': 'INFO',
    'format': '%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    'file': 'scraper.log',
    'max_file_size': 10 * 1024 * 1024,  # 10MB
    'backup_count': 5
}

# Rate Limiting
RATE_LIMITING = {
    'requests_per_minute': 30,
    'delay_between_requests': 2,  # seconds
    'respect_robots_txt': True
}

# Error Handling
ERROR_HANDLING = {
    'max_consecutive_errors': 5,
    'error_retry_delay': 5,  # seconds
    'continue_on_error': True,
    'log_errors': True
}
