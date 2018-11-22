from pydrag.lastfm.models.common import (
    AlbumList,
    ArtistList,
    ChartList,
    TagInfoList,
    TrackList,
)
from pydrag.lastfm.models.tag import Tag
from pydrag.lastfm.models.test import MethodTestCase, fixture


class TagServiceTests(MethodTestCase):
    def setUp(self):
        self.tag = Tag("rap")
        super(TagServiceTests, self).setUp()

    @fixture.use_cassette(path="tag/get_info")
    def test_find(self):
        result = Tag.find(name="rap", lang="en")
        expected_params = {"lang": "en", "method": "tag.getInfo", "tag": "rap"}

        self.assertEqual(expected_params, result.params)
        self.assertIsInstance(result, Tag)
        self.assertFixtureEqual("tag/get_info", result.to_dict())

    @fixture.use_cassette(path="tag/get_similar")
    def test_get_similar(self):
        self.tag.name = "Disco"
        result = self.tag.get_similar()
        expected_params = {"method": "tag.getSimilar", "tag": "Disco"}
        self.assertEqual(expected_params, result.params)
        self.assertIsInstance(result, TagInfoList)
        self.assertFixtureEqual("tag/get_similar", result.to_dict())

    @fixture.use_cassette(path="tag/get_top_albums")
    def test_get_top_albums(self):
        result = self.tag.get_top_albums(page=1, limit=2)
        expected_params = {
            "limit": 2,
            "method": "tag.getTopAlbums",
            "page": 1,
            "tag": "rap",
        }
        self.assertEqual(expected_params, result.params)

        self.assertIsInstance(result, AlbumList)
        self.assertFixtureEqual("tag/get_top_albums", result.to_dict())

    @fixture.use_cassette(path="tag/get_top_artists")
    def test_get_top_artists(self):
        result = self.tag.get_top_artists(page=1, limit=2)
        expected_params = {
            "limit": 2,
            "method": "tag.getTopArtists",
            "page": 1,
            "tag": "rap",
        }
        self.assertEqual(expected_params, result.params)

        self.assertIsInstance(result, ArtistList)
        self.assertFixtureEqual("tag/get_top_artists", result.to_dict())

        self.assertEqual(1, result.get_page())
        self.assertEqual(2, result.get_limit())
        self.assertEqual(61526, result.get_total())
        self.assertEqual(30763, result.get_total_pages())
        self.assertFalse(result.has_prev())
        self.assertTrue(result.has_next())

    @fixture.use_cassette(path="tag/get_top_tracks")
    def test_get_top_tracks(self):
        result = self.tag.get_top_tracks(page=1, limit=2)
        expected_params = {
            "limit": 2,
            "method": "tag.getTopTracks",
            "page": 1,
            "tag": "rap",
        }
        self.assertEqual(expected_params, result.params)

        self.assertIsInstance(result, TrackList)
        self.assertFixtureEqual("tag/get_top_tracks", result.to_dict())

    @fixture.use_cassette(path="tag/get_top_tags")
    def test_get_top_tags(self):
        result = Tag.get_top_tags(page=3, limit=10)
        expected_params = {
            "method": "tag.getTopTags",
            "num_res": 10,
            "offset": 20,
        }
        self.assertEqual(expected_params, result.params)
        self.assertEqual(10, len(result.tag))
        self.assertIsInstance(result, TagInfoList)
        self.assertFixtureEqual("tag/get_top_tags", result.to_dict())

    @fixture.use_cassette(path="tag/get_weekly_chart_list")
    def test_get_weekly_chart_list(self):
        result = self.tag.get_weekly_chart_list()
        expected_params = {"method": "tag.getWeeklyChartList", "tag": "rap"}
        self.assertEqual(expected_params, result.params)

        self.assertIsInstance(result, ChartList)
        self.assertFixtureEqual("tag/get_weekly_chart_list", result.to_dict())
