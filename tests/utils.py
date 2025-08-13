"""
Test utilities and fixtures for prompt template testing
"""
import pytest
from mcp_airflow_api.airflow_api import get_prompt_template
from mcp_airflow_api.functions import parse_prompt_sections


class TemplateAnalyzer:
    """Utility class for analyzing template structure during tests"""
    
    def __init__(self):
        self.template = get_prompt_template()
        self.headings, self.sections = parse_prompt_sections(self.template)
    
    def get_section_count(self):
        """Get the current number of sections"""
        return len(self.headings)
    
    def find_sections_by_keyword(self, keyword):
        """Find all sections that contain the keyword"""
        found_sections = []
        for i, heading in enumerate(self.headings):
            if keyword.lower() in heading.lower():
                found_sections.append({
                    'number': i + 1,
                    'heading': heading,
                    'content': self.sections[i + 1] if i + 1 < len(self.sections) else ""
                })
        return found_sections
    
    def get_template_stats(self):
        """Get template statistics for debugging"""
        return {
            'total_length': len(self.template),
            'section_count': len(self.headings),
            'headings': self.headings,
            'avg_section_length': sum(len(s) for s in self.sections[1:]) / max(1, len(self.sections) - 1)
        }
    
    def validate_section_numbering(self):
        """Validate that sections are properly numbered"""
        issues = []
        for i, heading in enumerate(self.headings, 1):
            if not heading.strip().startswith(str(i)):
                issues.append(f"Section {i} heading doesn't start with number: '{heading}'")
        return issues


# Global fixture that can be used across multiple test modules
@pytest.fixture(scope="session")
def template_analyzer():
    """Session-scoped template analyzer fixture"""
    return TemplateAnalyzer()


def print_template_info():
    """Utility function to print current template information"""
    analyzer = TemplateAnalyzer()
    stats = analyzer.get_template_stats()
    
    print("\n=== Current Template Information ===")
    print(f"Total length: {stats['total_length']} characters")
    print(f"Section count: {stats['section_count']}")
    print(f"Average section length: {stats['avg_section_length']:.1f} characters")
    print("\nSection headings:")
    for i, heading in enumerate(stats['headings'], 1):
        print(f"  {i}. {heading}")
    
    numbering_issues = analyzer.validate_section_numbering()
    if numbering_issues:
        print("\nNumbering issues found:")
        for issue in numbering_issues:
            print(f"  - {issue}")
    else:
        print("\n✓ Section numbering is consistent")
    print("=" * 40)


if __name__ == "__main__":
    # Run this script directly to get current template info
    print_template_info()
