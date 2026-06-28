# === Stage 51: Add unit tests for search and filter behavior ===
# Project: ClientDesk
from unittest.mock import patch, MagicMock
import pytest
from clientdesk.core.search_engine import SearchEngine
from clientdesk.models.contact import Contact
from datetime import date

@pytest.fixture
def mock_db():
    return {
        'contacts': [Contact(id=1, name='Alice', email='alice@test.com'), Contact(id=2, name='Bob', email='bob@test.com')],
        'meetings': [],
        'tasks': []
    }

@pytest.fixture
def search_engine(mock_db):
    return SearchEngine(mock_db)

class TestSearchAndFilter:
    def test_search_by_name(self, search_engine):
        results = search_engine.search('Alice', field='name')
        assert len(results['contacts']) == 1
        assert results['contacts'][0].id == 1
    
    def test_filter_meetings_by_date(self, search_engine):
        with patch.object(search_engine.db, 'meetings', [{'date': date(2023, 1, 1), 'client_id': 1}]):
            filtered = search_engine.filter('meetings', {'field': 'date', 'operator': 'gte', 'value': date(2023, 1, 1)})
            assert len(filtered['results']) == 1

    def test_search_no_matches(self, search_engine):
        results = search_engine.search('Charlie', field='name')
        assert len(results['contacts']) == 0
