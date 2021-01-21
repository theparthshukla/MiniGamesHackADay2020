"""
Stevedore extension for static annotation searching in Java files.
"""
import re

from code_annotations.extensions.base import SimpleRegexAnnotationExtension


class JavaAnnotationExtension(SimpleRegexAnnotationExtension):
    """
    Annotation extension for Java source files.
    """

    extension_name = 'java'

    lang_comment_definition = {
        'multi_start': re.escape('/*'),
        'multi_end': re.escape('*/'),
	'single': re.escape('@')
    }
