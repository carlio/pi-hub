# taken from https://github.com/perone/stallion/blob/master/stallion/metadata.py

# Tuple metadata format
# (Field Name, lowered field name, Optional)

# Based on the PEP-0241
HEADER_META_1_0 = (
    'metadata-version',
    'name',
    'version',
    'platform',
    'supported-platform',
    'summary',
    'description',
    'keywords',
    'home-page',
    'author',
    'author-email',
    'license',
    # Not part of PEP, but PEP-0314 (everyone uses anyway in 1.0)
    'classifier'
)

# Based on the PEP-0314
HEADER_META_1_1 = HEADER_META_1_0 + (
    'download-url',
    'requires',
    'provides',
    'obsoletes',
)

# Based on the PEP-0345
HEADER_META_1_2 = HEADER_META_1_1 + (
    'maintainer',
    'maintainer-email',
    'requires-python',
    'requires-external',
    'requires-dist',
    'provides-dist',
    'obsoletes-dist',
    'project-url',
)
    
HEADER_META_ALL = HEADER_META_1_2