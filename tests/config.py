"""
Test configuration - Update these values when template structure changes
"""

# 템플릿 변경시 여기만 수정하면 됩니다
TEMPLATE_CONFIG = {
    "min_sections": 7,  # 최소 예상 섹션 수
    "expected_keywords": ["overview", "tools", "example", "format", "logging"],  # 항상 있을 것으로 예상되는 키워드들
    "min_template_length": 1000,  # 최소 템플릿 길이
    "title_marker": "# MCP Airflow API",  # 예상 제목
    "section_headings_marker": "Section Headings:",  # 헤딩 모드 마커
}
